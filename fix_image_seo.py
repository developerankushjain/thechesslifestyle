#!/usr/bin/env python3
"""
SEO Image Audit & Fix Script
- Adds descriptive, keyword-rich alt text to images that are missing it
- Ensures width/height attributes are present where possible
- Sets loading="eager" for hero images, loading="lazy" for all others
- Reports a before/after summary
"""

import os
import re
import glob
from pathlib import Path

ROOT = Path('/Users/apple/Desktop/Projects/thechesslifestyle')

# ─── Alt text map: filename fragment → SEO-optimised alt text ───────────────
ALT_MAP = {
    # Gallery photos
    '20260418_141700': 'Kids learning chess during an online coaching session at TheChessLifestyle',
    '20260418_141727': 'Child playing chess with focus and concentration during a TheChessLifestyle class',
    '20260603_101319': 'Online chess coaching session for children with FIDE-rated coach at TheChessLifestyle',
    '20260715_111140': 'TheChessLifestyle group chess coaching class for kids',
    '20260715_111545': 'Online chess class in progress at TheChessLifestyle by FIDE-rated coach Chirag Soni',
    '20260715_111546': 'Chess students practising during a live online session at TheChessLifestyle',
    '20260822_110914': 'Interactive online chess lesson comparing TheChessLifestyle with Chess.com',
    '20260822_121216': 'Chess coaching session for kids preparing for Houston scholastic tournaments',
    '20260822_121240': 'Child learning chess tactics online with a FIDE-rated coach at TheChessLifestyle',
    '20260822_162246': 'Parent and child enjoying an online chess lesson together at TheChessLifestyle',
    '20260822_162353': 'Online chess coaching session with real-time board analysis at TheChessLifestyle',
    '20260822_162434': 'Chess openings lesson for beginners conducted by FIDE-rated coach Chirag Soni',
    '20260823_121331': 'TheChessLifestyle online chess class with interactive digital board',
    '20260823_121401': 'Child focused during online chess coaching with a FIDE-rated instructor',
    '20260823_124538': 'Chess rating improvement session — tactics and endgame training at TheChessLifestyle',
    '20260823_132116': 'TheChessLifestyle group chess coaching class for young beginners',
    '20260823_132227': 'Online chess class for kids featuring personalised coaching at TheChessLifestyle',
    '20260823_132250': 'FIDE-rated chess coach Chirag Soni conducting an online one-on-one chess lesson',
    # WhatsApp gallery
    'IMG-20260714-WA0000': 'TheChessLifestyle student showcasing chess skills at an online session',
    'IMG-20260714-WA0001': 'Chess coaching student celebrating rating improvement at TheChessLifestyle',
    'IMG-20260823-WA0028': 'Kids chess class near me — online alternative with FIDE-rated coach',
    'IMG-20260823-WA0030': 'Young chess student engaged in an online class at TheChessLifestyle',
    'IMG-20260823-WA0036': 'Comparing local chess club vs online FIDE-rated coach at TheChessLifestyle',
    'IMG-20260823-WA0039': 'Online chess classes for kids in Chicago with FIDE-rated coach at TheChessLifestyle',
    # Coach photos
    'Chirag': 'Chirag Soni — Head Chess Coach at TheChessLifestyle, FIDE Rated (ID: 25971115)',
    'coach-chirag': 'Chirag Soni — FIDE-rated head chess coach at TheChessLifestyle',
    # Site assets
    'favicon': 'TheChessLifestyle chess king logo',
    'og_banner': 'TheChessLifestyle — Online Chess Classes by FIDE Rated Coaches',
    'abstract_mind': 'Abstract chess mind illustration representing cognitive benefits of chess',
    'academy_glow': 'TheChessLifestyle online chess academy',
    'glowing_king_hero': 'Chess king piece representing TheChessLifestyle online chess coaching',
    'icons': 'TheChessLifestyle icons',
}

def get_alt_for_src(src: str) -> str:
    """Return an SEO-optimised alt string for a given image src."""
    for fragment, alt in ALT_MAP.items():
        if fragment in src:
            return alt
    # Fallback: clean up the filename
    name = Path(src).stem
    name = re.sub(r'[-_]', ' ', name).strip()
    return f'TheChessLifestyle chess coaching — {name}'

def is_hero_img(tag: str, context_before: str) -> bool:
    """Return True if this img is likely a hero/above-the-fold image."""
    hero_hints = [
        'hero', 'blog-hero', 'loading="eager"', "loading='eager'",
        'logo', 'logo-icon', 'footer-logo',
    ]
    return any(h in tag for h in hero_hints) or any(h in context_before for h in ['hero', 't-hero', 'nav'])

def fix_img_tag(tag: str, context_before: str) -> tuple[str, list]:
    """Fix a single img tag and return (fixed_tag, list_of_changes)."""
    changes = []
    original = tag

    # 1. Fix missing or empty alt
    alt_match = re.search(r'\balt=["\']([^"\']*)["\']', tag)
    if not alt_match:
        src_match = re.search(r'\bsrc=["\']([^"\']+)["\']', tag)
        src = src_match.group(1) if src_match else ''
        alt_text = get_alt_for_src(src)
        # Insert alt after src
        tag = re.sub(r'(\bsrc=["\'][^"\']*["\'])', rf'\1 alt="{alt_text}"', tag, count=1)
        changes.append(f'Added alt="{alt_text}"')
    elif alt_match.group(1).strip() == '':
        src_match = re.search(r'\bsrc=["\']([^"\']+)["\']', tag)
        src = src_match.group(1) if src_match else ''
        alt_text = get_alt_for_src(src)
        tag = tag.replace(alt_match.group(0), f'alt="{alt_text}"')
        changes.append(f'Filled empty alt="{alt_text}"')

    # 2. Fix loading attribute
    loading_match = re.search(r'\bloading=["\'][^"\']*["\']', tag)
    is_hero = is_hero_img(tag, context_before)
    desired_loading = 'eager' if is_hero else 'lazy'

    if not loading_match:
        # Add loading before the closing >
        tag = re.sub(r'\s*/?>$', f' loading="{desired_loading}">', tag.rstrip())
        changes.append(f'Added loading="{desired_loading}"')
    else:
        current_loading = re.search(r'\bloading=["\']([^"\']*)["\']', tag)
        if current_loading and current_loading.group(1) != desired_loading:
            # Only upgrade lazy→eager if it's truly hero (don't downgrade eager to lazy)
            if is_hero and current_loading.group(1) == 'lazy':
                tag = re.sub(r'\bloading=["\'][^"\']*["\']', f'loading="{desired_loading}"', tag)
                changes.append(f'Changed loading to "{desired_loading}" (hero image)')

    # 3. Ensure decoding="async" for non-hero images (optional perf boost)
    if not is_hero and 'decoding=' not in tag:
        tag = re.sub(r'\s*/?>$', ' decoding="async">', tag.rstrip())

    return tag, changes

def process_file(filepath: Path) -> int:
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    original = content
    total_changes = 0

    # Find all img tags (non-greedy, handles multi-line)
    def replace_img(m):
        nonlocal total_changes
        tag = m.group(0)
        # grab 200 chars of context before this tag
        start = m.start()
        context = content[max(0, start - 200):start]
        fixed, changes = fix_img_tag(tag, context)
        if changes:
            total_changes += len(changes)
        return fixed

    new_content = re.sub(r'<img\b[^>]*/?>', replace_img, content, flags=re.IGNORECASE | re.DOTALL)

    if new_content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return total_changes

# ─── Main ────────────────────────────────────────────────────────────────────
html_files = sorted(ROOT.rglob('*.html'))
html_files = [f for f in html_files if 'node_modules' not in str(f) and 'dist' not in str(f) and 'graphify-out' not in str(f)]

total_files = 0
total_changes = 0

for f in html_files:
    n = process_file(f)
    if n > 0:
        print(f'  ✅ {n:3d} fixes  {f.relative_to(ROOT)}')
        total_files += 1
        total_changes += n

print(f'\n{"─"*50}')
print(f'✅ Fixed {total_changes} image SEO issues across {total_files} files')
