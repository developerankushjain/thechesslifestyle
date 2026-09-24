import re, os

# ─────────────────────────────────────────────
# TASK 1: Fix H1 on home page to include keyword
# ─────────────────────────────────────────────
with open('index.html', 'r') as f:
    index_html = f.read()

old_h1 = '<h1>Master the Board. <br/><span class="highlight">Master your Mind.</span></h1>'
new_h1 = '<h1>Online Chess Classes — <br/><span class="highlight">Master your Mind.</span></h1>'
index_html = index_html.replace(old_h1, new_h1)
with open('index.html', 'w') as f:
    f.write(index_html)
print("✅ Task 1: H1 updated on home page")


# ─────────────────────────────────────────────
# TASK 2: Fix duplicate city cannibalisation
# Point /online-chess-classes-[city]/ canonical → /usa/[city]/ (the richer page)
# ─────────────────────────────────────────────
cannibal_map = {
    'online-chess-classes-chicago': ('https://www.thechesslifestyle.com/usa/chicago/', 'usa/chicago'),
    'online-chess-classes-houston': ('https://www.thechesslifestyle.com/usa/houston/', 'usa/houston'),
    'online-chess-classes-los-angeles': ('https://www.thechesslifestyle.com/usa/los-angeles/', 'usa/los-angeles'),
    'online-chess-classes-new-york': ('https://www.thechesslifestyle.com/usa/new-york-city/', 'usa/new-york-city'),
}

for slug, (canonical_url, _) in cannibal_map.items():
    path = f'{slug}/index.html'
    if not os.path.exists(path):
        continue
    with open(path, 'r') as f:
        html = f.read()
    # Replace the self-pointing canonical with the canonical of the richer page
    html = re.sub(
        r'<link rel="canonical" href="https://www\.thechesslifestyle\.com/[^"]*/"',
        f'<link rel="canonical" href="{canonical_url}"',
        html
    )
    # Also add a noindex note in meta robots to prevent the thin page from ranking
    html = html.replace(
        '<meta name="robots" content="index, follow">',
        '<meta name="robots" content="noindex, follow">'
    )
    with open(path, 'w') as f:
        f.write(html)
    print(f"✅ Task 2: Canonicalized {slug} → {canonical_url}")


# ─────────────────────────────────────────────
# TASK 3: Add internal links from every blog post to 2 relevant pages
# ─────────────────────────────────────────────
blog_link_map = {
    'how-to-improve-chess-rating-fast': [
        ('online chess classes', '/online-chess-classes/'),
        ('FIDE rated coaches', '/online-chess-classes-for-kids/'),
    ],
    'best-chess-openings-for-beginners': [
        ('online chess classes for beginners', '/online-chess-classes-for-kids/'),
        ('book a free trial', '/#trial'),
    ],
    'does-chess-help-with-adhd-in-kids': [
        ('online chess classes for kids', '/online-chess-classes-for-kids/'),
        ('FIDE rated online coaching', '/online-chess-classes/'),
    ],
    'chess-improves-academic-performance': [
        ('online chess classes for kids', '/online-chess-classes-for-kids/'),
        ('structured chess coaching', '/pricing/'),
    ],
    'how-to-teach-chess-to-a-child': [
        ('online chess classes for kids', '/online-chess-classes-for-kids/'),
        ('FIDE rated chess instructor', '/online-chess-classes/'),
    ],
    'online-chess-coach-vs-self-study': [
        ('online chess coaching', '/online-chess-classes/'),
        ('structured pricing and plans', '/pricing/'),
    ],
    'chess-classes-for-kids-near-me': [
        ('online chess classes for kids', '/online-chess-classes-for-kids/'),
        ('chess classes in the USA', '/online-chess-classes-usa/'),
    ],
    'local-us-chess-club-vs-online-fide-coach': [
        ('online chess classes in the USA', '/online-chess-classes-usa/'),
        ('New York chess students', '/usa/new-york-city/'),
    ],
    'chess-com-lessons-vs-thechesslifestyle': [
        ('book a free trial class', '/online-chess-classes/'),
        ('pricing plans', '/pricing/'),
    ],
    'best-online-chess-classes-kids-usa': [
        ('chess classes in New York', '/usa/new-york-city/'),
        ('chess classes in Los Angeles', '/usa/los-angeles/'),
    ],
    'chess-classes-dubai-expat-families': [
        ('online chess classes in Dubai', '/online-chess-classes-dubai/'),
        ('online chess classes in UAE', '/online-chess-classes-uae/'),
    ],
    'chess-saudi-arabia-vision-2030': [
        ('online chess classes in Saudi Arabia', '/online-chess-classes-saudi-arabia/'),
        ('online chess classes in Riyadh', '/online-chess-classes-riyadh/'),
    ],
}

cta_snippet = """
    <div style="background: rgba(245,158,11,0.08); border: 1px solid rgba(245,158,11,0.3); border-radius: 12px; padding: 1.2rem 1.5rem; margin: 2rem 0; font-size: 0.95rem;">
      <strong>📍 Also Explore:</strong> {links}
    </div>"""

for slug, links in blog_link_map.items():
    path = f'blog/{slug}/index.html'
    if not os.path.exists(path):
        continue
    with open(path, 'r') as f:
        html = f.read()

    link_html = ' · '.join([f'<a href="{url}" style="color:var(--primary);font-weight:600;">{text}</a>' for text, url in links])
    snippet = cta_snippet.format(links=link_html)

    # Inject before the closing </main> tag (before the blog-cta div)
    html = html.replace('    <div class="blog-cta">', snippet + '\n    <div class="blog-cta">')
    with open(path, 'w') as f:
        f.write(html)
    print(f"✅ Task 3: Added internal links to blog/{slug}")

print("\nAll Phase 2 tasks complete!")
