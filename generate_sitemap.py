from datetime import date

today = date.today().strftime("%Y-%m-%d")
base = "https://www.thechesslifestyle.com"

# Priority and changefreq configuration
pages = [
    # (path, priority, changefreq)
    ("", "1.0", "weekly"),               # Home
    ("online-chess-classes/", "0.9", "monthly"),
    ("online-chess-classes-for-kids/", "0.9", "monthly"),
    ("pricing/", "0.9", "monthly"),
    ("blog/", "0.8", "weekly"),

    # USA city guides (long-form)
    ("usa/new-york-city/", "0.8", "monthly"),
    ("usa/chicago/", "0.8", "monthly"),
    ("usa/houston/", "0.8", "monthly"),
    ("usa/los-angeles/", "0.8", "monthly"),

    # City landing pages
    ("online-chess-classes-usa/", "0.8", "monthly"),
    ("online-chess-classes-new-york/", "0.7", "monthly"),
    ("online-chess-classes-chicago/", "0.7", "monthly"),
    ("online-chess-classes-houston/", "0.7", "monthly"),
    ("online-chess-classes-los-angeles/", "0.7", "monthly"),
    ("online-chess-classes-london/", "0.7", "monthly"),
    ("online-chess-classes-uk/", "0.7", "monthly"),
    ("online-chess-classes-dubai/", "0.7", "monthly"),
    ("online-chess-classes-uae/", "0.7", "monthly"),
    ("online-chess-classes-abu-dhabi/", "0.7", "monthly"),
    ("online-chess-classes-australia/", "0.7", "monthly"),
    ("online-chess-classes-sydney/", "0.7", "monthly"),
    ("online-chess-classes-canada/", "0.7", "monthly"),
    ("online-chess-classes-toronto/", "0.7", "monthly"),
    ("online-chess-classes-saudi-arabia/", "0.7", "monthly"),
    ("online-chess-classes-riyadh/", "0.7", "monthly"),

    # Noida local
    ("chess-classes-noida/", "0.6", "monthly"),
    ("chess-home-tutor-noida/", "0.6", "monthly"),

    # Blog posts
    ("blog/how-to-improve-chess-rating-fast/", "0.7", "monthly"),
    ("blog/best-chess-openings-for-beginners/", "0.7", "monthly"),
    ("blog/how-to-teach-chess-to-a-child/", "0.7", "monthly"),
    ("blog/chess-improves-academic-performance/", "0.7", "monthly"),
    ("blog/does-chess-help-with-adhd-in-kids/", "0.7", "monthly"),
    ("blog/online-chess-coach-vs-self-study/", "0.7", "monthly"),
    ("blog/chess-classes-for-kids-near-me/", "0.7", "monthly"),
    ("blog/local-us-chess-club-vs-online-fide-coach/", "0.7", "monthly"),
    ("blog/chess-com-lessons-vs-thechesslifestyle/", "0.7", "monthly"),
    ("blog/best-online-chess-classes-kids-usa/", "0.7", "monthly"),
    ("blog/chess-classes-dubai-expat-families/", "0.7", "monthly"),
    ("blog/chess-saudi-arabia-vision-2030/", "0.6", "monthly"),

    # Legal
    ("terms.html", "0.3", "yearly"),
    ("privacy.html", "0.3", "yearly"),
    ("refund.html", "0.3", "yearly"),
]

sitemap = ['<?xml version="1.0" encoding="UTF-8"?>']
sitemap.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

for path, priority, changefreq in pages:
    url = f"{base}/{path}"
    sitemap.append(f"""  <url>
    <loc>{url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
  </url>""")

sitemap.append('</urlset>')

with open('sitemap.xml', 'w') as f:
    f.write('\n'.join(sitemap))

print(f"sitemap.xml created with {len(pages)} URLs")
