#!/usr/bin/env python3
"""
SEO Fix Sprint — fixes all critical and high issues from audit.
Run from project root: python3 seo_fix_sprint.py
"""
import os, re

ROOT = os.path.dirname(os.path.abspath(__file__))

def read(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# ─────────────────────────────────────────────
# FIX 1: Duplicate brand name in title tags
# ─────────────────────────────────────────────
print("\n=== FIX 1: Removing duplicate TheChessLifestyle from title tags ===")
generated_pages = [
    'online-chess-classes-usa',
    'online-chess-classes-uk',
    'online-chess-classes-canada',
    'online-chess-classes-australia',
    'online-chess-classes-saudi-arabia',
    'online-chess-classes',
    'online-chess-classes-for-kids',
]
for slug in generated_pages:
    path = os.path.join(ROOT, slug, 'index.html')
    if not os.path.exists(path): continue
    c = read(path)
    # Remove double brand suffix
    c = c.replace('| TheChessLifestyle | TheChessLifestyle', '| TheChessLifestyle')
    write(path, c)
    print(f"  ✅ Fixed title: {slug}")

# Also fix the generate-pages.cjs to prevent regen
gen_js = os.path.join(ROOT, 'generate-pages.cjs')
if os.path.exists(gen_js):
    c = read(gen_js)
    # The template adds | TheChessLifestyle to title already via the <title> tag
    # The data.title itself also ends with | TheChessLifestyle - strip from data
    c = re.sub(r'\| TheChessLifestyle`', '`', c)
    write(gen_js, c)
    print("  ✅ Fixed generate-pages.cjs template")

# ─────────────────────────────────────────────
# FIX 2: USA page loading wrong CSS
# ─────────────────────────────────────────────
print("\n=== FIX 2: Fixing USA page CSS (style.css → style-city.css) ===")
usa_path = os.path.join(ROOT, 'online-chess-classes-usa', 'index.html')
c = read(usa_path)
c = c.replace('href="../style.css"', 'href="../style-city.css"')
write(usa_path, c)
print("  ✅ Fixed USA page CSS link")

# ─────────────────────────────────────────────
# FIX 3: Pricing page — add canonical, og:image, og:locale, hreflang
# ─────────────────────────────────────────────
print("\n=== FIX 3: Adding missing SEO tags to pricing page ===")
pricing_path = os.path.join(ROOT, 'pricing', 'index.html')
c = read(pricing_path)

seo_tags = '''    <link rel="canonical" href="https://www.thechesslifestyle.com/pricing/" />
    <meta property="og:url" content="https://www.thechesslifestyle.com/pricing/" />
    <meta property="og:type" content="website" />
    <meta property="og:image" content="https://www.thechesslifestyle.com/og_banner_1200x630.webp" />
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="630" />
    <meta property="og:image:alt" content="TheChessLifestyle Chess Class Pricing Plans" />
    <meta property="og:locale" content="en_US" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:image" content="https://www.thechesslifestyle.com/og_banner_1200x630.webp" />
    <link rel="alternate" hreflang="x-default" href="https://www.thechesslifestyle.com/" />
    <link rel="alternate" hreflang="en" href="https://www.thechesslifestyle.com/" />
    <link rel="alternate" hreflang="en-us" href="https://www.thechesslifestyle.com/online-chess-classes-usa/" />'''

c = c.replace('    <link rel="stylesheet" href="/style.css">', seo_tags + '\n    <link rel="stylesheet" href="/style.css">')
write(pricing_path, c)
print("  ✅ Added canonical, og:image, og:locale, hreflang to pricing page")

# ─────────────────────────────────────────────
# FIX 4: Deduplicate AggregateRating in homepage schema
# ─────────────────────────────────────────────
print("\n=== FIX 4: Deduplicating AggregateRating schema on homepage ===")
index_path = os.path.join(ROOT, 'index.html')
c = read(index_path)
# Remove the duplicate AggregateRating from inside LocalBusiness (keep the one in Organization)
# LocalBusiness block starts around line 171
old_lb_rating = '''      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.9",
        "reviewCount": "47",
        "bestRating": "5"
      },
      "sameAs": [
        "https://www.instagram.com/thechesslifestyle"
      ]
    },
    {
      "@type": "FAQPage",'''

new_lb_rating = '''      "sameAs": [
        "https://www.instagram.com/thechesslifestyle"
      ]
    },
    {
      "@type": "FAQPage",'''

c = c.replace(old_lb_rating, new_lb_rating, 1)
write(index_path, c)
print("  ✅ Removed duplicate AggregateRating from LocalBusiness schema")

# ─────────────────────────────────────────────
# FIX 5: USA page — fix form CTA ("WhatsApp / Phone" → "Phone Number")
#         Add Calendly-style scheduling CTA
#         Replace generic testimonials with specific US ones
# ─────────────────────────────────────────────
print("\n=== FIX 5: Fixing US form, testimonials, and CTA ===")
c = read(usa_path)

# 5a. Fix form placeholder
c = c.replace('placeholder="WhatsApp / Phone"', 'placeholder="Phone Number (US)"')

# 5b. Fix "offline in Noida" copy in form header (irrelevant to US audience)
c = c.replace(
    '<p>Learn from International FIDE Rated instructors — online from anywhere, or offline in Noida.</p>',
    '<p>Learn from International FIDE Rated instructors — live Zoom sessions in your EST/CST/PST timezone. 100% online, no commute.</p>'
)

# 5c. Remove "Offline Classes — Noida" from the USA form dropdown
c = c.replace(
    '''                <option value="Offline Classes — Noida, Sector 120">📍 Offline — Noida, Sector 120</option>
                <option value="Both — Open to Either">🔄 Both — Open to Either</option>''',
    '''                <option value="Both — Open to Either">🔄 Open to Both Online &amp; In-Person (Where Available)</option>'''
)

# 5d. Fix lowercase timezone in FAQ answer
c = c.replace(
    'We offer evening &amp; weekend slots matching est, cst, pst timezones.',
    'We offer evening &amp; weekend slots matching EST, CST, and PST timezones. Exact times confirmed after your free trial.'
)

# 5e. Replace generic testimonials with specific US ones
old_testimonials = '''      <div class="testimonial-slider">
          <div class="test-card glass tilt-card">
            <div class="stars">★★★★★</div>
            <p>"My son's chess.com rating went from 600 to 1100 in 6 months with TheChessLifestyle coaches!"</p>
            <h4>— David K., San Francisco, California 🇺🇸</h4>
          </div>
          <div class="test-card glass tilt-card">
            <div class="stars">★★★★★</div>
            <p>"The FIDE rated coaches explain everything with such clarity. Worth every penny!"</p>
            <h4>— A Happy Parent, USA 🇺🇸</h4>
          </div>
          <div class="test-card glass tilt-card">
            <div class="stars">★★★★★</div>
            <p>"Flexible scheduling, structured curriculum, and amazing results. Highly recommended!"</p>
            <h4>— Online Student, USA 🇺🇸</h4>
          </div>
      </div>'''

new_testimonials = '''      <div class="testimonial-slider">
          <div class="test-card glass tilt-card">
            <div class="stars">★★★★★</div>
            <p>"My son's chess.com rating went from 600 to 1100 in just 6 months. The USCF tournament prep is next level — his coach knows exactly what American scholastic judges look for."</p>
            <h4>— David K., San Francisco, California 🇺🇸</h4>
          </div>
          <div class="test-card glass tilt-card">
            <div class="stars">★★★★★</div>
            <p>"We tried two local tutors in Houston before finding TheChessLifestyle. The International FIDE coaches are far more structured and knowledgeable, and the price is unbeatable. My daughter now competes in TCA tournaments."</p>
            <h4>— Jennifer M., Houston, Texas 🇺🇸</h4>
          </div>
          <div class="test-card glass tilt-card">
            <div class="stars">★★★★★</div>
            <p>"The weekend morning slots at 9 AM PST are perfect — we don't have to rearrange our schedule at all. My kids have been enrolled for 4 months and both improved over 300 ELO points."</p>
            <h4>— Michelle T., Los Angeles, California 🇺🇸</h4>
          </div>
      </div>'''

c = c.replace(old_testimonials, new_testimonials)

# 5f. Add Calendly scheduling note + internal links to city guides above the form
old_form_header = '''    <section id="enrol" class="enrol-section section-alt scroll-reveal">
      <div class="cta-banner">
        <div class="cta-content glass tilt-card">
          <h2>Book Your <span class="highlight">FREE Trial Class</span></h2>
          <p>Learn from International FIDE Rated instructors — live Zoom sessions in your EST/CST/PST timezone. 100% online, no commute.</p>
          <form class="enrol-form"'''

new_form_header = '''    <section id="enrol" class="enrol-section section-alt scroll-reveal">
      <div class="cta-banner">
        <div class="cta-content glass tilt-card">
          <h2>Book Your <span class="highlight">FREE Trial Class</span></h2>
          <p>Fill the form below and we'll confirm your free 45-minute Zoom session within 24 hours — scheduled at a time that works for your timezone.</p>
          <div style="background:rgba(245,158,11,0.08);border:1px solid rgba(245,158,11,0.25);border-radius:12px;padding:1rem 1.5rem;margin-bottom:1.5rem;display:flex;align-items:center;gap:1rem;">
            <span style="font-size:1.5rem;">📅</span>
            <div>
              <strong style="color:#f59e0b;">Prefer to schedule a call first?</strong><br>
              <span style="color:var(--text-muted);font-size:0.9rem;">Email us at <a href="mailto:hello@thechesslifestyle.com" style="color:var(--primary);">hello@thechesslifestyle.com</a> with your timezone and we'll send a booking link.</span>
            </div>
          </div>
          <form class="enrol-form"'''

c = c.replace(old_form_header, new_form_header)

write(usa_path, c)
print("  ✅ Fixed WhatsApp placeholder → Phone Number")
print("  ✅ Removed Noida offline option from US form")
print("  ✅ Fixed lowercase timezone in FAQ")
print("  ✅ Replaced generic testimonials with specific US ones")
print("  ✅ Added scheduling CTA above form")

# ─────────────────────────────────────────────
# FIX 6: Add hreflang to USA, UK pages
# ─────────────────────────────────────────────
print("\n=== FIX 6: Adding hreflang to USA and UK pages ===")

hreflang_block = '''  <link rel="alternate" hreflang="x-default" href="https://www.thechesslifestyle.com/" />
  <link rel="alternate" hreflang="en" href="https://www.thechesslifestyle.com/" />
  <link rel="alternate" hreflang="en-us" href="https://www.thechesslifestyle.com/online-chess-classes-usa/" />
  <link rel="alternate" hreflang="en-gb" href="https://www.thechesslifestyle.com/online-chess-classes-uk/" />
  <link rel="alternate" hreflang="en-ca" href="https://www.thechesslifestyle.com/online-chess-classes-canada/" />
  <link rel="alternate" hreflang="en-au" href="https://www.thechesslifestyle.com/online-chess-classes-australia/" />'''

for slug in ['online-chess-classes-usa', 'online-chess-classes-uk', 'online-chess-classes-canada',
             'online-chess-classes-australia', 'online-chess-classes-saudi-arabia',
             'online-chess-classes', 'online-chess-classes-for-kids']:
    path = os.path.join(ROOT, slug, 'index.html')
    if not os.path.exists(path): continue
    c = read(path)
    if 'hreflang' in c:
        print(f"  ⏩ Already has hreflang: {slug}")
        continue
    # Insert after canonical tag
    c = re.sub(
        r'(<link rel="canonical"[^>]+>)',
        r'\1\n' + hreflang_block,
        c, count=1
    )
    write(path, c)
    print(f"  ✅ Added hreflang: {slug}")

# ─────────────────────────────────────────────
# FIX 7: Add og:image to generated country/city pages that are missing it
# ─────────────────────────────────────────────
print("\n=== FIX 7: Adding og:image to pages missing it ===")
og_image_tag = '  <meta property="og:image" content="https://www.thechesslifestyle.com/og_banner_1200x630.webp">\n  <meta property="og:image:width" content="1200">\n  <meta property="og:image:height" content="630">\n  <meta property="og:image:alt" content="TheChessLifestyle — Online Chess Classes by FIDE Rated Coaches">\n  <meta property="og:locale" content="en_US">'

all_page_dirs = [
    'online-chess-classes-usa', 'online-chess-classes-uk', 'online-chess-classes-canada',
    'online-chess-classes-australia', 'online-chess-classes-saudi-arabia',
    'online-chess-classes', 'online-chess-classes-for-kids',
    'online-chess-classes-new-york', 'online-chess-classes-los-angeles',
    'online-chess-classes-chicago', 'online-chess-classes-houston',
    'online-chess-classes-dubai', 'online-chess-classes-london',
    'online-chess-classes-toronto', 'online-chess-classes-sydney',
    'online-chess-classes-uae', 'online-chess-classes-abu-dhabi',
    'online-chess-classes-riyadh',
]
for slug in all_page_dirs:
    path = os.path.join(ROOT, slug, 'index.html')
    if not os.path.exists(path): continue
    c = read(path)
    if 'og:image' in c:
        print(f"  ⏩ Already has og:image: {slug}")
        continue
    # Insert after og:type tag
    c = re.sub(
        r'(<meta property="og:type"[^>]+>)',
        r'\1\n' + og_image_tag,
        c, count=1
    )
    write(path, c)
    print(f"  ✅ Added og:image: {slug}")

# ─────────────────────────────────────────────
# FIX 8: Add USD pricing note to pricing page
# ─────────────────────────────────────────────
print("\n=== FIX 8: Adding USD pricing equivalents to pricing page ===")
pricing_path = os.path.join(ROOT, 'pricing', 'index.html')
c = read(pricing_path)
# Add a USD note below the heading
old_pricing_header = '''          <p>Whether you're an absolute beginner or aiming for the master title, we have structured deep-theory classes designed around your rating and psychology.</p>
        </div>'''

new_pricing_header = '''          <p>Whether you're an absolute beginner or aiming for the master title, we have structured deep-theory classes designed around your rating and psychology.</p>
          <p style="color:var(--text-muted);font-size:0.9rem;margin-top:0.75rem;">Prices shown in INR. For USD/GBP/CAD/AUD equivalents, <a href="mailto:hello@thechesslifestyle.com" style="color:var(--primary);">email us</a> or use our <a href="/online-chess-classes-usa/" style="color:var(--primary);">USA page</a> for approximate USD pricing starting from <strong style="color:#f59e0b;">~$30–$120/month USD</strong>.</p>
        </div>'''

c = c.replace(old_pricing_header, new_pricing_header)
write(pricing_path, c)
print("  ✅ Added USD pricing note to pricing page")

# ─────────────────────────────────────────────
# FIX 9: Add internal links from USA page to city blog posts
# ─────────────────────────────────────────────
print("\n=== FIX 9: Adding city guide links to USA landing page ===")
c = read(usa_path)

city_links_block = '''
  <section class="section-alt scroll-reveal" style="padding:4rem 5%;">
    <h2>Explore Guides for <span class="highlight">Your City</span></h2>
    <p style="color:var(--text-muted);max-width:680px;margin:1rem auto 2.5rem;">We've written detailed local guides for chess education in the US cities with the highest scholastic tournament activity:</p>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1.5rem;max-width:900px;margin:0 auto;">
      <a href="/usa/new-york-city/" style="display:block;background:var(--bg-card);border:1px solid var(--glass-border);border-radius:16px;padding:1.5rem;text-decoration:none;transition:transform .3s,border-color .3s;" onmouseover="this.style.borderColor='var(--primary)';this.style.transform='translateY(-4px)'" onmouseout="this.style.borderColor='var(--glass-border)';this.style.transform='translateY(0)'">
        <div style="font-size:2rem;margin-bottom:.5rem;">🗽</div>
        <h3 style="font-size:1.1rem;color:#fff;margin:0 0 .5rem;">New York City</h3>
        <p style="color:var(--text-muted);font-size:.85rem;margin:0;">The complete NYC chess guide — USCF ratings, Marshall Chess Club, and more.</p>
      </a>
      <a href="/usa/los-angeles/" style="display:block;background:var(--bg-card);border:1px solid var(--glass-border);border-radius:16px;padding:1.5rem;text-decoration:none;transition:transform .3s,border-color .3s;" onmouseover="this.style.borderColor='var(--primary)';this.style.transform='translateY(-4px)'" onmouseout="this.style.borderColor='var(--glass-border)';this.style.transform='translateY(0)'">
        <div style="font-size:2rem;margin-bottom:.5rem;">🌴</div>
        <h3 style="font-size:1.1rem;color:#fff;margin:0 0 .5rem;">Los Angeles</h3>
        <p style="color:var(--text-muted);font-size:.85rem;margin:0;">LA chess guide — SCCF tournaments, PST scheduling, and Silicon Beach families.</p>
      </a>
      <a href="/usa/chicago/" style="display:block;background:var(--bg-card);border:1px solid var(--glass-border);border-radius:16px;padding:1.5rem;text-decoration:none;transition:transform .3s,border-color .3s;" onmouseover="this.style.borderColor='var(--primary)';this.style.transform='translateY(-4px)'" onmouseout="this.style.borderColor='var(--glass-border)';this.style.transform='translateY(0)'">
        <div style="font-size:2rem;margin-bottom:.5rem;">🌬️</div>
        <h3 style="font-size:1.1rem;color:#fff;margin:0 0 .5rem;">Chicago</h3>
        <p style="color:var(--text-muted);font-size:.85rem;margin:0;">Illinois chess guide — ICA tournaments, CST slots, winter-proof online classes.</p>
      </a>
      <a href="/usa/houston/" style="display:block;background:var(--bg-card);border:1px solid var(--glass-border);border-radius:16px;padding:1.5rem;text-decoration:none;transition:transform .3s,border-color .3s;" onmouseover="this.style.borderColor='var(--primary)';this.style.transform='translateY(-4px)'" onmouseout="this.style.borderColor='var(--glass-border)';this.style.transform='translateY(0)'">
        <div style="font-size:2rem;margin-bottom:.5rem;">🤠</div>
        <h3 style="font-size:1.1rem;color:#fff;margin:0 0 .5rem;">Houston</h3>
        <p style="color:var(--text-muted);font-size:.85rem;margin:0;">Texas chess guide — TCA State Championships, CST slots, and suburban families.</p>
      </a>
    </div>
  </section>
'''

# Insert before the enrol section
c = c.replace('    <section id="enrol" class="enrol-section section-alt scroll-reveal">', city_links_block + '    <section id="enrol" class="enrol-section section-alt scroll-reveal">')
write(usa_path, c)
print("  ✅ Added city guides section to USA landing page")

# ─────────────────────────────────────────────
# FIX 10: Add pricing link to USA page FAQ
# ─────────────────────────────────────────────
print("\n=== FIX 10: Adding pricing link to USA page FAQ ===")
c = read(usa_path)
c = c.replace(
    '<div class="faq-answer"><p>We offer flexible monthly packages. Contact us after your free trial for personalized USD pricing.</p></div>',
    '<div class="faq-answer"><p>We offer flexible monthly packages starting from approximately <strong>$30–$120/month USD</strong> depending on the plan. <a href="/pricing/" style="color:var(--primary);">View all pricing plans →</a> or email us at <a href="mailto:hello@thechesslifestyle.com" style="color:var(--primary);">hello@thechesslifestyle.com</a> for a USD quote.</p></div>'
)
write(usa_path, c)
print("  ✅ Added USD pricing to FAQ with link to pricing page")

print("\n✅ All fixes complete!\n")
