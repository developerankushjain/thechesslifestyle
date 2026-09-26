#!/usr/bin/env python3
"""
Inject country-code selector before phone input fields across all forms.
Skips index.html (already done), dist/, and .gemini directories.
"""
import os, glob, re

BASE = "/Users/apple/Desktop/Projects/thechesslifestyle"

# The country code dropdown + phone input HTML block to inject
PHONE_BLOCK = '''<div class="fg phone-row">
              <div class="phone-combo">
                <select name="Country Code" aria-label="Country Code" class="cc-select">
                  <option value="+91">&#x1F1EE;&#x1F1F3; +91 (India)</option>
                  <option value="+1">&#x1F1FA;&#x1F1F8; +1 (USA/Canada)</option>
                  <option value="+44">&#x1F1EC;&#x1F1E7; +44 (UK)</option>
                  <option value="+971">&#x1F1E6;&#x1F1EA; +971 (UAE)</option>
                  <option value="+966">&#x1F1F8;&#x1F1E6; +966 (Saudi Arabia)</option>
                  <option value="+61">&#x1F1E6;&#x1F1FA; +61 (Australia)</option>
                  <option value="+1-CA">&#x1F1E8;&#x1F1E6; +1 (Canada)</option>
                  <option value="+65">&#x1F1F8;&#x1F1EC; +65 (Singapore)</option>
                  <option value="+64">&#x1F1F3;&#x1F1FF; +64 (New Zealand)</option>
                  <option value="+49">&#x1F1E9;&#x1F1EA; +49 (Germany)</option>
                  <option value="+33">&#x1F1EB;&#x1F1F7; +33 (France)</option>
                  <option value="+39">&#x1F1EE;&#x1F1F9; +39 (Italy)</option>
                  <option value="+34">&#x1F1EA;&#x1F1F8; +34 (Spain)</option>
                  <option value="+31">&#x1F1F3;&#x1F1F1; +31 (Netherlands)</option>
                  <option value="+46">&#x1F1F8;&#x1F1EA; +46 (Sweden)</option>
                  <option value="+47">&#x1F1F3;&#x1F1F4; +47 (Norway)</option>
                  <option value="+41">&#x1F1E8;&#x1F1ED; +41 (Switzerland)</option>
                  <option value="+27">&#x1F1FF;&#x1F1E6; +27 (South Africa)</option>
                  <option value="+55">&#x1F1E7;&#x1F1F7; +55 (Brazil)</option>
                  <option value="+52">&#x1F1F2;&#x1F1FD; +52 (Mexico)</option>
                  <option value="+81">&#x1F1EF;&#x1F1F5; +81 (Japan)</option>
                  <option value="+82">&#x1F1F0;&#x1F1F7; +82 (South Korea)</option>
                  <option value="+86">&#x1F1E8;&#x1F1F3; +86 (China)</option>
                  <option value="+353">&#x1F1EE;&#x1F1EA; +353 (Ireland)</option>
                  <option value="Other">Other</option>
                </select>
                <input type="tel" name="Phone Number" placeholder="WhatsApp / Phone Number *" required>
              </div>
            </div>'''

# The CSS to inject once per file (before </style> or in <head>)
PHONE_CSS = """
    /* Country code phone combo */
    .phone-row { margin-bottom: 0 !important; }
    .phone-combo { display: flex; gap: 0; width: 100%; }
    .cc-select {
      flex: 0 0 auto;
      width: 185px;
      padding: .8rem .6rem .8rem .9rem;
      border: 1.5px solid #e2e8f0;
      border-right: none;
      border-radius: 10px 0 0 10px;
      font-size: .82rem;
      font-family: 'Inter', sans-serif;
      color: #0f172a;
      background: #f8fafc;
      outline: none;
      cursor: pointer;
      appearance: auto;
      transition: border-color .2s, box-shadow .2s;
    }
    .cc-select:focus {
      border-color: var(--primary, #f59e0b);
      box-shadow: 0 0 0 3px rgba(245,158,11,.1);
      background: #fff;
    }
    .phone-combo input[type="tel"] {
      flex: 1;
      border-radius: 0 10px 10px 0 !important;
    }
    @media(max-width:480px) {
      .phone-combo { flex-direction: column; }
      .cc-select { width: 100%; border-right: 1.5px solid #e2e8f0; border-bottom: none; border-radius: 10px 10px 0 0; }
      .phone-combo input[type="tel"] { border-radius: 0 0 10px 10px !important; }
    }
"""

# Old phone input pattern (single line in city pages)
OLD_PATTERN = r'<div class="fg"><input\s+type="tel"\s+name="Phone Number"\s+placeholder="WhatsApp / Phone Number \*"\s+required\s*></div>'
# Also variant without space before >
OLD_PATTERN2 = r'<div class="fg"><input type="tel" name="Phone Number" placeholder="WhatsApp / Phone Number \*" required></div>'

def process_file(fpath):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    changed = False

    # Skip if already has cc-select
    if 'cc-select' in content:
        print(f'  SKIP (already done): {fpath}')
        return False

    # Skip if no phone input to replace
    if 'name="Phone Number"' not in content and 'name="Phone"' not in content:
        return False

    # --- Inject CSS ---
    if '<style>' in content and 'cc-select' not in content:
        # Find last </style> and insert before it
        content = content.replace('</style>', PHONE_CSS + '  </style>', 1)
        changed = True
    elif '</head>' in content and 'cc-select' not in content:
        content = content.replace('</head>', f'<style>{PHONE_CSS}</style>\n</head>', 1)
        changed = True

    # --- Replace phone input field ---
    # Pattern for city pages: <div class="fg"><input type="tel" ...></div>
    new_content = re.sub(
        r'<div class="fg">\s*<input\s+type="tel"\s+name="Phone Number"\s+placeholder="WhatsApp / Phone Number \*"\s+required\s*>\s*</div>',
        PHONE_BLOCK,
        content,
        flags=re.DOTALL
    )
    if new_content != content:
        content = new_content
        changed = True

    if changed and content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


# Find all HTML files
html_files = []
for root, dirs, files in os.walk(BASE):
    # Skip unwanted dirs
    dirs[:] = [d for d in dirs if d not in ['dist', 'node_modules', '.gemini', 'graphify-out', 'rebuild_city_pages.py']]
    for fname in files:
        if fname.endswith('.html'):
            fpath = os.path.join(root, fname)
            html_files.append(fpath)

count = 0
for fpath in html_files:
    rel = os.path.relpath(fpath, BASE)
    # Skip homepage (already done), dist
    if rel == 'index.html':
        print(f'  SKIP (homepage already has it): {rel}')
        continue
    if process_file(fpath):
        print(f'✓ {rel}')
        count += 1

print(f'\nDone — {count} files updated.')
