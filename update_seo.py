import os
import re

updates = [
    {
        "file": "index.html",
        "old_title": r'<title>.*?</title>',
        "new_title": r'<title>Online Chess Classes for Kids &amp; Adults | Free Trial | TheChessLifestyle</title>',
        "old_desc": r'<meta name="description" content=".*?">',
        "new_desc": r'<meta name="description" content="Learn chess online from FIDE Rated coaches. Structured classes for ages 5–adult. 4.9★ rated. Free 45-min trial — no credit card. Flexible EST/GMT/AEST slots. Book today.">',
        "old_og_title": r'<meta property="og:title" content=".*?">',
        "new_og_title": r'<meta property="og:title" content="Online Chess Classes for Kids &amp; Adults | Free Trial | TheChessLifestyle">',
        "old_og_desc": r'<meta property="og:description" content=".*?">',
        "new_og_desc": r'<meta property="og:description" content="Learn chess online from FIDE Rated coaches. Structured classes for ages 5–adult. 4.9★ rated. Free 45-min trial — no credit card. Flexible EST/GMT/AEST slots. Book today.">',
    },
    {
        "file": "online-chess-classes-usa/index.html",
        "old_title": r'<title>.*?</title>',
        "new_title": r'<title>Online Chess Classes for Kids in USA | FIDE Coaches | Free Trial</title>',
        "old_desc": r'<meta name="description" content=".*?">',
        "new_desc": r'<meta name="description" content="Live 1-on-1 chess coaching for US students (ages 5–adult). FIDE Rated instructors. All 4 US timezones covered. USCF tournament prep. Free 45-min trial — no commitment.">',
        "old_og_title": r'<meta property="og:title" content=".*?">',
        "new_og_title": r'<meta property="og:title" content="Online Chess Classes for Kids in USA | FIDE Coaches | Free Trial">',
        "old_og_desc": r'<meta property="og:description" content=".*?">',
        "new_og_desc": r'<meta property="og:description" content="Live 1-on-1 chess coaching for US students (ages 5–adult). FIDE Rated instructors. All 4 US timezones covered. USCF tournament prep. Free 45-min trial — no commitment.">',
        "add_geo": r'<meta name="geo.region" content="US">\n  <meta name="geo.placename" content="United States">',
    },
    {
        "file": "online-chess-classes-uk/index.html",
        "old_title": r'<title>.*?</title>',
        "new_title": r'<title>Online Chess Classes for Kids in the UK | FIDE Coaches | Free Trial</title>',
        "old_desc": r'<meta name="description" content=".*?">',
        "new_desc": r'<meta name="description" content="Live chess coaching for UK students (ages 5–adult). FIDE Rated instructors. ECF grading prep. GMT/BST friendly slots. 4.9★ rated. Book your free 45-min trial today.">',
        "old_og_title": r'<meta property="og:title" content=".*?">',
        "new_og_title": r'<meta property="og:title" content="Online Chess Classes for Kids in the UK | FIDE Coaches | Free Trial">',
        "old_og_desc": r'<meta property="og:description" content=".*?">',
        "new_og_desc": r'<meta property="og:description" content="Live chess coaching for UK students (ages 5–adult). FIDE Rated instructors. ECF grading prep. GMT/BST friendly slots. 4.9★ rated. Book your free 45-min trial today.">',
        "add_geo": r'<meta name="geo.region" content="GB">',
    },
    {
        "file": "online-chess-classes-canada/index.html",
        "old_title": r'<title>.*?</title>',
        "new_title": r'<title>Online Chess Lessons for Kids in Canada | FIDE Coaches | Free Trial</title>',
        "old_desc": r'<meta name="description" content=".*?">',
        "new_desc": r'<meta name="description" content="Live chess coaching for Canadian students across all provinces. CFC tournament prep. FIDE Rated instructors. ET/CT/MT/PT slots. Free 45-min trial — no obligation.">',
        "old_og_title": r'<meta property="og:title" content=".*?">',
        "new_og_title": r'<meta property="og:title" content="Online Chess Lessons for Kids in Canada | FIDE Coaches | Free Trial">',
        "old_og_desc": r'<meta property="og:description" content=".*?">',
        "new_og_desc": r'<meta property="og:description" content="Live chess coaching for Canadian students across all provinces. CFC tournament prep. FIDE Rated instructors. ET/CT/MT/PT slots. Free 45-min trial — no obligation.">',
        "add_geo": r'<meta name="geo.region" content="CA">',
    },
    {
        "file": "online-chess-classes-australia/index.html",
        "old_title": r'<title>.*?</title>',
        "new_title": r'<title>Online Chess Classes for Kids in Australia | FIDE Coaches | Free Trial</title>',
        "old_desc": r'<meta name="description" content=".*?">',
        "new_desc": r'<meta name="description" content="Live chess coaching for Australian students. FIDE Rated instructors. AEST/ACST/AWST friendly slots. ACF rating prep. Free 45-min trial — no credit card needed.">',
        "old_og_title": r'<meta property="og:title" content=".*?">',
        "new_og_title": r'<meta property="og:title" content="Online Chess Classes for Kids in Australia | FIDE Coaches | Free Trial">',
        "old_og_desc": r'<meta property="og:description" content=".*?">',
        "new_og_desc": r'<meta property="og:description" content="Live chess coaching for Australian students. FIDE Rated instructors. AEST/ACST/AWST friendly slots. ACF rating prep. Free 45-min trial — no credit card needed.">',
        "add_geo": r'<meta name="geo.region" content="AU">',
    }
]

schema_rating = """
          "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "4.9",
            "reviewCount": "47",
            "bestRating": "5"
          },
"""

for page in updates:
    filepath = page["file"]
    if not os.path.exists(filepath):
        print(f"Skipping {filepath}")
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    content = re.sub(page["old_title"], page["new_title"], content)
    content = re.sub(page["old_desc"], page["new_desc"], content)
    content = re.sub(page["old_og_title"], page["new_og_title"], content)
    content = re.sub(page["old_og_desc"], page["new_og_desc"], content)
    
    # Add geo tags if not present
    if "add_geo" in page and "geo.region" not in content:
        content = content.replace('</title>', f'</title>\n  {page["add_geo"]}')
        
    # Inject AggregateRating into Course schema on country pages
    if "aggregateRating" not in content and '"@type":"Course"' in content:
        # Simple injection right after "@type":"Course",
        content = content.replace('"@type":"Course",', '"@type":"Course",' + schema_rating)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        print(f"Updated SEO tags in {filepath}")

