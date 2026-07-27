#!/usr/bin/env python3
"""SEO Fix Sprint v2 — remaining issues after v1."""
import os, re, glob

ROOT = '/Users/apple/Desktop/Projects/thechesslifestyle'

def read(p):
    with open(p, 'r', encoding='utf-8') as f: return f.read()

def write(p, c):
    with open(p, 'w', encoding='utf-8') as f: f.write(c)

# ───────────────────────────────────────────
# FIX A: og:locale on ALL blog posts: en_IN → en_US
# ───────────────────────────────────────────
print("\n=== FIX A: og:locale en_IN → en_US on all blog posts ===")
for path in glob.glob(f'{ROOT}/blog/*/index.html'):
    c = read(path)
    if 'og:locale" content="en_IN"' in c:
        c = c.replace('og:locale" content="en_IN"', 'og:locale" content="en_US"')
        write(path, c)
        print(f"  ✅ Fixed: {path.split('/')[-2]}")

# ───────────────────────────────────────────
# FIX B: Blog CTA links — US city guides → /online-chess-classes-usa/ not /#enrol
# ───────────────────────────────────────────
print("\n=== FIX B: Fix CTA links in US city blog posts ===")
us_city_blogs = [
    'online-chess-classes-new-york-city-guide',
    'online-chess-classes-los-angeles-guide',
    'online-chess-classes-chicago-guide',
    'online-chess-classes-houston-guide',
    'best-online-chess-classes-kids-usa',
]
for slug in us_city_blogs:
    path = f'{ROOT}/blog/{slug}/index.html'
    if not os.path.exists(path): continue
    c = read(path)
    # Update the bottom blog CTA to go to USA page
    c = c.replace(
        '<a href="/#enrol" class="btn-primary" style="display:inline-block;">Book Free Trial Class →</a>',
        '<a href="/online-chess-classes-usa/" class="btn-primary" style="display:inline-block;">Book Free Trial (USA) →</a>'
    )
    # Update the in-text CTA link
    c = c.replace('href="/#enrol"><strong>Book Your Free Trial Class Today</strong></a>', 
                  'href="/online-chess-classes-usa/"><strong>Book Your Free Trial Class Today</strong></a>')
    write(path, c)
    print(f"  ✅ Updated CTA: {slug}")

# ───────────────────────────────────────────
# FIX C: Homepage author meta — remove "Noida"
# ───────────────────────────────────────────
print("\n=== FIX C: Remove 'Noida' from homepage author meta ===")
idx = f'{ROOT}/index.html'
c = read(idx)
c = c.replace('content="TheChessLifestyle Noida"', 'content="TheChessLifestyle"')
write(idx, c)
print("  ✅ Removed Noida from meta author")

# ───────────────────────────────────────────
# FIX D: Homepage title — add "for Kids" keyword
# ───────────────────────────────────────────
print("\n=== FIX D: Optimize homepage title tag for US traffic ===")
c = read(idx)
c = c.replace(
    '<title>Online Chess Classes | Free Trial | TheChessLifestyle</title>',
    '<title>Online Chess Classes for Kids &amp; Adults | FIDE Rated Coaches | Free Trial | TheChessLifestyle</title>'
)
# Also update og:title to match
c = c.replace(
    'content="Online Chess Classes | Free Trial | TheChessLifestyle"',
    'content="Online Chess Classes for Kids &amp; Adults | FIDE Rated Coaches | Free Trial | TheChessLifestyle"'
)
write(idx, c)
print("  ✅ Updated homepage title to include 'for Kids & Adults'")

# ───────────────────────────────────────────
# FIX E: USA page font — still blocking render (rel=stylesheet, not preload)
# ───────────────────────────────────────────
print("\n=== FIX E: Make Google Fonts non-blocking on USA page ===")
usa = f'{ROOT}/online-chess-classes-usa/index.html'
c = read(usa)
old_font = '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Outfit:wght@400;600;700;900&display=swap" rel="stylesheet">'
new_font = '''<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Outfit:wght@400;600;700;900&display=swap" onload="this.rel='stylesheet'">
  <noscript><link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Outfit:wght@400;600;700;900&display=swap" rel="stylesheet"></noscript>'''
c = c.replace(old_font, new_font)
write(usa, c)
print("  ✅ Made Google Fonts non-blocking on USA page")

# ───────────────────────────────────────────
# FIX F: Add Twitter card tags to geo pages missing them
# ───────────────────────────────────────────
print("\n=== FIX F: Add Twitter card meta to geo pages ===")
pages_needing_twitter = [
    'online-chess-classes-usa',
    'online-chess-classes-uk',
    'online-chess-classes-for-kids',
    'online-chess-classes',
    'online-chess-classes-canada',
    'online-chess-classes-australia',
    'online-chess-classes-saudi-arabia',
]
for slug in pages_needing_twitter:
    path = f'{ROOT}/{slug}/index.html'
    if not os.path.exists(path): continue
    c = read(path)
    if 'twitter:card' in c:
        print(f"  ⏩ Already has Twitter card: {slug}"); continue
    # Insert after og:locale
    twitter_block = '''
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:site" content="@thechesslifestyle">
  <meta name="twitter:title" content="TheChessLifestyle — Online Chess Classes by FIDE Rated Coaches">
  <meta name="twitter:description" content="Online chess classes for kids &amp; adults. International FIDE Rated coaches. Book your FREE 45-min trial today.">
  <meta name="twitter:image" content="https://www.thechesslifestyle.com/og_banner_1200x630.webp">'''
    c = re.sub(r'(<meta property="og:locale"[^>]+>)', r'\1' + twitter_block, c, count=1)
    write(path, c)
    print(f"  ✅ Added Twitter card: {slug}")

# ───────────────────────────────────────────
# FIX G: USA page schema FAQ — fix lowercase timezone
#         (the JSON-LD still has lowercase "est, cst, pst")
# ───────────────────────────────────────────
print("\n=== FIX G: Fix lowercase timezone in USA page JSON-LD schema ===")
c = read(usa)
c = c.replace(
    '"We offer evening \\u0026 weekend slots matching est, cst, pst timezones.',
    '"We offer evening \\u0026 weekend slots matching EST, CST, and PST timezones.'
)
# Also the plain text version
c = c.replace(
    'evening &amp; weekend slots matching est, cst, pst timezones.',
    'evening &amp; weekend slots matching EST, CST, and PST timezones.'
)
write(usa, c)
print("  ✅ Fixed lowercase timezone in USA page schema")

# ───────────────────────────────────────────
# FIX H: Add preload link for og_banner on USA page (was removed)
# ───────────────────────────────────────────
print("\n=== FIX H: Add hero image preload to USA page ===")
c = read(usa)
if 'preload' not in c:
    c = c.replace(
        '<link rel="stylesheet" href="../style-city.css">',
        '<link rel="preload" as="image" href="/og_banner_1200x630.webp" fetchpriority="high">\n  <link rel="stylesheet" href="../style-city.css">'
    )
    write(usa, c)
    print("  ✅ Added og_banner preload to USA page")
else:
    print("  ⏩ USA page already has preload")

# ───────────────────────────────────────────
# FIX I: generate-cities.py — add Twitter cards to template
# ───────────────────────────────────────────
print("\n=== FIX I: Add Twitter card to generate-cities.py template ===")
gen_cities = f'{ROOT}/generate-cities.py'
c = read(gen_cities)
if 'twitter:card' not in c:
    c = c.replace(
        "  <meta property=\"og:locale\" content=\"en_US\">",
        "  <meta property=\"og:locale\" content=\"en_US\">\n  <meta name=\"twitter:card\" content=\"summary_large_image\">\n  <meta name=\"twitter:site\" content=\"@thechesslifestyle\">\n  <meta name=\"twitter:image\" content=\"https://www.thechesslifestyle.com/og_banner_1200x630.webp\">"
    )
    write(gen_cities, c)
    print("  ✅ Added Twitter card to generate-cities.py template")
else:
    print("  ⏩ generate-cities.py already has Twitter card")

print("\n✅ All v2 fixes complete!\n")
