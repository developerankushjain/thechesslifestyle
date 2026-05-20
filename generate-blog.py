#!/usr/bin/env python3
"""
TheChessLifestyle — Blog Generator
===================================
Usage:
  python3 generate-blog.py          # generate all blog posts + index
  python3 generate-blog.py --new    # scaffold a new blank post

Pipeline:
  1. Write a Markdown post in content/posts/your-slug.md
  2. Run: python3 generate-blog.py
  3. Deploy — done!

The script auto-updates public/sitemap.xml with all blog URLs.
"""

import os, re, glob, json, sys
from datetime import date
import markdown

# ─── CONFIG ────────────────────────────────────────────────────────────────
CONTENT_DIR  = "content/posts"
BLOG_OUT_DIR = "blog"
SITE_URL     = "https://www.thechesslifestyle.com"
SITEMAP_PATH = "public/sitemap.xml"
TODAY        = date.today().isoformat()

# ─── FRONTMATTER PARSER ────────────────────────────────────────────────────
def parse_frontmatter(text):
    """Parse YAML-style --- frontmatter from markdown file."""
    meta = {}
    body = text
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            for line in parts[1].strip().splitlines():
                if ":" in line:
                    k, _, v = line.partition(":")
                    meta[k.strip()] = v.strip().strip('"').strip("'")
            body = parts[2].strip()
    return meta, body

# ─── HTML TEMPLATE ─────────────────────────────────────────────────────────
def render_post(meta, html_content):
    title    = meta.get("title", "Chess Blog")
    desc     = meta.get("description", "")
    slug     = meta.get("slug", "post")
    author   = meta.get("author", "Chirag Soni")
    pub_date = meta.get("date", TODAY)
    image    = meta.get("image", "/og_banner_1200x630.png")
    category = meta.get("category", "Chess")
    tags     = meta.get("tags", "chess, coaching, FIDE")
    read_min = meta.get("read_min", "5")

    canonical = f"{SITE_URL}/blog/{slug}/"
    og_image  = f"{SITE_URL}{image}"

    schema = json.dumps({
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": title,
      "description": desc,
      "author": {
        "@type": "Person",
        "name": author,
        "sameAs": [
          "https://ratings.fide.com/profile/25971115/statistics",
          "https://www.linkedin.com/in/chirag48438/"
        ]
      },
      "publisher": {
        "@type": "Organization",
        "name": "TheChessLifestyle",
        "logo": {"@type": "ImageObject", "url": f"{SITE_URL}/favicon.png"}
      },
      "datePublished": pub_date,
      "dateModified": TODAY,
      "image": og_image,
      "mainEntityOfPage": canonical
    }, ensure_ascii=False)

    # Breadcrumb schema
    breadcrumb = json.dumps({
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL},
        {"@type": "ListItem", "position": 2, "name": "Blog", "item": f"{SITE_URL}/blog/"},
        {"@type": "ListItem", "position": 3, "name": title, "item": canonical}
      ]
    })

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <!-- Google Analytics GA4 -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-GGZHBK0Y4P"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-GGZHBK0Y4P');
  </script>
  <link rel="icon" type="image/png" sizes="192x192" href="/favicon.png">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | TheChessLifestyle</title>
  <meta name="description" content="{desc}">
  <meta name="keywords" content="{tags}">
  <meta name="author" content="{author}">
  <link rel="canonical" href="{canonical}">
  <meta name="robots" content="index, follow">
  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{og_image}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="article:published_time" content="{pub_date}">
  <meta property="article:author" content="{author}">
  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{og_image}">
  <meta property="og:site_name" content="TheChessLifestyle">
  <meta property="og:locale" content="en_IN">
  <meta name="twitter:site" content="@thechesslifestyle">
  <!-- Schema -->
  <script type="application/ld+json">{schema}</script>
  <script type="application/ld+json">{breadcrumb}</script>
  <!-- Fonts (non-blocking) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Outfit:wght@400;600;700;900&display=swap" onload="this.rel='stylesheet'">
  <noscript><link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Outfit:wght@400;600;700;900&display=swap" rel="stylesheet"></noscript>
  <link rel="stylesheet" href="../../style.css">
  <style>
    .blog-post-wrap {{
      max-width: 780px;
      margin: 0 auto;
      padding: 120px 5% 5rem;
    }}
    .blog-breadcrumb {{
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 2rem;
    }}
    .blog-breadcrumb a {{ color: var(--primary); text-decoration: none; }}
    .blog-meta {{
      display: flex;
      align-items: center;
      gap: 1rem;
      flex-wrap: wrap;
      margin: 1.5rem 0 2.5rem;
      font-size: 0.88rem;
      color: var(--text-muted);
    }}
    .blog-tag {{
      background: rgba(245,158,11,.12);
      color: var(--primary);
      padding: 0.2rem 0.75rem;
      border-radius: 2rem;
      font-size: 0.8rem;
    }}
    .blog-hero-img {{
      width: 100%;
      border-radius: 1rem;
      margin-bottom: 2.5rem;
      max-height: 420px;
      object-fit: cover;
    }}
    .blog-body h2 {{
      font-size: 1.8rem;
      margin: 2.5rem 0 1rem;
      color: var(--text-primary);
    }}
    .blog-body h3 {{
      font-size: 1.35rem;
      margin: 2rem 0 0.75rem;
      color: var(--primary);
    }}
    .blog-body p {{
      font-size: 1.05rem;
      line-height: 1.85;
      color: var(--text-secondary);
      margin-bottom: 1.25rem;
    }}
    .blog-body ul, .blog-body ol {{
      margin: 0 0 1.5rem 1.5rem;
      color: var(--text-secondary);
      line-height: 1.9;
    }}
    .blog-body blockquote {{
      border-left: 4px solid var(--primary);
      padding: 0.75rem 1.5rem;
      margin: 2rem 0;
      background: rgba(245,158,11,.06);
      border-radius: 0 0.5rem 0.5rem 0;
      font-style: italic;
      color: var(--text-secondary);
    }}
    .blog-body strong {{ color: var(--text-primary); }}
    .blog-body a {{ color: var(--primary); }}
    .blog-cta {{
      background: linear-gradient(135deg, rgba(245,158,11,.12), rgba(245,158,11,.04));
      border: 1px solid rgba(245,158,11,.25);
      border-radius: 1rem;
      padding: 2.5rem;
      text-align: center;
      margin: 3rem 0 0;
    }}
    .blog-cta h3 {{ margin-bottom: 0.75rem; }}
    .blog-cta p {{ color: var(--text-muted); margin-bottom: 1.5rem; }}
    .author-card {{
      display: flex;
      align-items: center;
      gap: 1.25rem;
      background: rgba(255,255,255,.04);
      border: 1px solid rgba(255,255,255,.08);
      border-radius: 1rem;
      padding: 1.5rem;
      margin: 3rem 0;
    }}
    .author-card img {{
      width: 64px;
      height: 64px;
      border-radius: 50%;
      object-fit: cover;
      object-position: center 10%;
      border: 2px solid var(--primary);
    }}
    .author-card h4 {{ margin: 0 0 0.25rem; font-size: 1rem; }}
    .author-card p {{ margin: 0; font-size: 0.88rem; color: var(--text-muted); }}
  </style>
</head>
<body>
  <div class="glow-tracker" id="cursor-glow"></div>
  <nav class="navbar">
    <div class="logo"><a href="/" style="color:white;text-decoration:none;">TheChessLifestyle</a></div>
    <ul class="nav-links">
      <li><a href="/#philosophy">Our Philosophy</a></li>
      <li><a href="/#benefits">Benefits</a></li>
      <li><a href="/blog/">Blog</a></li>
      <li><a href="/#contact">Contact</a></li>
    </ul>
    <a href="/#trial" class="cta-btn">Free Trial</a>
  </nav>

  <main class="blog-post-wrap">
    <nav class="blog-breadcrumb">
      <a href="/">Home</a> › <a href="/blog/">Blog</a> › {title}
    </nav>

    <h1>{title}</h1>

    <div class="blog-meta">
      <span>📅 {pub_date}</span>
      <span>✍️ {author}</span>
      <span>⏱ {read_min} min read</span>
      <span class="blog-tag">{category}</span>
    </div>

    <picture>
      <source srcset="{image.replace('.png','.webp').replace('.jpg','.webp')}" type="image/webp">
      <img src="{image}" alt="{title}" class="blog-hero-img" width="780" height="420" loading="eager">
    </picture>

    <article class="blog-body">
      {html_content}
    </article>

    <div class="author-card">
      <picture>
        <source srcset="/coach-chirag.webp" type="image/webp">
        <img src="/coach-chirag.jpg" alt="Author Chirag Soni - Head Chess Coach">
      </picture>
      <div>
        <h4>{author}</h4>
        <p>Head Chess Coach at TheChessLifestyle · FIDE Rated · <a href="https://ratings.fide.com/profile/25971115/statistics" target="_blank" style="color:var(--primary);">FIDE ID 25971115</a> · <a href="https://www.linkedin.com/in/chirag48438/" target="_blank" style="color:var(--primary);">LinkedIn</a></p>
      </div>
    </div>

    <div class="blog-cta">
      <h3>Ready to Start Your <span class="highlight">Chess Journey?</span></h3>
      <p>Book a free 45-minute trial class with Chirag Soni — no credit card, no commitment.</p>
      <a href="/#enrol" class="btn-primary" style="display:inline-block;">Book Free Trial Class →</a>
    </div>
  </main>

  <footer id="contact">
    <div class="footer-container">
      <div class="footer-col"><h2 class="logo">TheChessLifestyle</h2><p class="footer-tagline">Chess for Mental &amp; Cognitive Health.</p></div>
      <div class="footer-col"><h3>Online Classes</h3><ul>
        <li><a href="/online-chess-classes/">Online Chess Classes</a></li>
        <li><a href="/online-chess-classes-for-kids/">For Kids</a></li>
        <li><a href="/online-chess-classes-usa/">USA</a></li>
        <li><a href="/online-chess-classes-uk/">UK</a></li>
        <li><a href="/online-chess-classes-canada/">Canada</a></li>
        <li><a href="/online-chess-classes-australia/">Australia</a></li>
        <li><a href="/online-chess-classes-saudi-arabia/">Saudi Arabia</a></li>
      </ul></div>
      <div class="footer-col"><h3>In-Person (Noida)</h3><ul>
        <li><a href="/chess-classes-noida/">Chess Classes in Noida</a></li>
        <li><a href="/chess-home-tutor-noida/">Chess Home Tutor Noida</a></li>
      </ul></div>
      <div class="footer-col contact-info"><h3>Contact</h3>
        <p>Sector 120, Noida</p>
        <p><a href="tel:+917206789979">7206789979</a></p>
        <a href="mailto:hello@thechesslifestyle.com">hello@thechesslifestyle.com</a>
      </div>
    </div>
    <div class="footer-bottom"><p>&copy; 2026 TheChessLifestyle.</p></div>
  </footer>
  <script src="../../main.js" type="module"></script>
</body>
</html>'''

# ─── BLOG INDEX PAGE ───────────────────────────────────────────────────────
def render_index(posts):
    cards = ""
    for p in posts:
        m = p["meta"]
        slug     = m.get("slug", "post")
        title    = m.get("title", "")
        desc     = m.get("description", "")
        pub_date = m.get("date", TODAY)
        category = m.get("category", "Chess")
        read_min = m.get("read_min", "5")
        image    = m.get("image", "/og_banner_1200x630.png")
        cards += f'''
        <a href="/blog/{slug}/" class="blog-card tilt-card" style="text-decoration:none; color:inherit; display:block;">
          <picture>
            <source srcset="{image.replace('.png','.webp').replace('.jpg','.webp')}" type="image/webp">
            <img src="{image}" alt="{title}" class="blog-card-img" loading="lazy" width="400" height="220">
          </picture>
          <div class="blog-card-body">
            <span class="blog-tag" style="display:inline-block; margin-bottom:.75rem;">{category}</span>
            <h2 class="blog-card-title">{title}</h2>
            <p class="blog-card-desc">{desc}</p>
            <div class="blog-card-meta">📅 {pub_date} &nbsp;·&nbsp; ⏱ {read_min} min read</div>
          </div>
        </a>'''

    schema = json.dumps({
      "@context": "https://schema.org",
      "@type": "Blog",
      "name": "TheChessLifestyle Blog",
      "description": "Expert chess coaching tips, strategies, and guides by FIDE Rated coach Chirag Soni.",
      "url": f"{SITE_URL}/blog/",
      "publisher": {
        "@type": "Organization",
        "name": "TheChessLifestyle",
        "logo": {"@type": "ImageObject", "url": f"{SITE_URL}/favicon.png"}
      }
    })

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <!-- Google Analytics GA4 -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-GGZHBK0Y4P"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-GGZHBK0Y4P');
  </script>
  <link rel="icon" type="image/png" sizes="192x192" href="/favicon.png">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chess Blog | Expert Tips &amp; Guides | TheChessLifestyle</title>
  <meta name="description" content="Learn chess strategies, tips and insights from FIDE Rated coach Chirag Soni. Articles on chess for kids, improvement guides, and coaching insights.">
  <meta name="author" content="TheChessLifestyle">
  <link rel="canonical" href="{SITE_URL}/blog/">
  <meta name="robots" content="index, follow">
  <meta property="og:type" content="website">
  <meta property="og:title" content="Chess Blog | Expert Tips &amp; Guides | TheChessLifestyle">
  <meta property="og:description" content="Learn chess strategies, tips and insights from FIDE Rated coach Chirag Soni.">
  <meta property="og:url" content="{SITE_URL}/blog/">
  <meta property="og:image" content="{SITE_URL}/og_banner_1200x630.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Chess Blog | TheChessLifestyle">
  <meta name="twitter:description" content="Expert chess coaching tips by FIDE Rated coach Chirag Soni.">
  <meta name="twitter:image" content="{SITE_URL}/og_banner_1200x630.png">
  <meta property="og:site_name" content="TheChessLifestyle">
  <meta property="og:locale" content="en_IN">
  <meta name="twitter:site" content="@thechesslifestyle">
  <script type="application/ld+json">{schema}</script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Outfit:wght@400;600;700;900&display=swap" onload="this.rel='stylesheet'">
  <noscript><link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Outfit:wght@400;600;700;900&display=swap" rel="stylesheet"></noscript>
  <link rel="stylesheet" href="../style.css">
  <style>
    .blog-index-wrap {{ max-width: 1100px; margin: 0 auto; padding: 120px 5% 5rem; }}
    .blog-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 2rem; margin-top: 3rem; }}
    .blog-card {{
      background: rgba(255,255,255,.04);
      border: 1px solid rgba(255,255,255,.08);
      border-radius: 1rem;
      overflow: hidden;
      transition: transform .3s, box-shadow .3s;
    }}
    .blog-card:hover {{ transform: translateY(-6px); box-shadow: 0 20px 40px rgba(245,158,11,.15); border-color: rgba(245,158,11,.3); }}
    .blog-card-img {{ width: 100%; height: 200px; object-fit: cover; display: block; }}
    .blog-card-body {{ padding: 1.5rem; }}
    .blog-card-title {{ font-size: 1.15rem; font-weight: 700; margin: 0 0 0.75rem; line-height: 1.4; color: var(--text-primary); }}
    .blog-card-desc {{ font-size: 0.9rem; color: var(--text-muted); margin: 0 0 1rem; line-height: 1.6; }}
    .blog-card-meta {{ font-size: 0.8rem; color: var(--text-muted); }}
    .blog-tag {{ background: rgba(245,158,11,.12); color: var(--primary); padding: .2rem .75rem; border-radius: 2rem; font-size: .8rem; }}
  </style>
</head>
<body>
  <div class="glow-tracker" id="cursor-glow"></div>
  <nav class="navbar">
    <div class="logo"><a href="/" style="color:white;text-decoration:none;">TheChessLifestyle</a></div>
    <ul class="nav-links">
      <li><a href="/#philosophy">Our Philosophy</a></li>
      <li><a href="/#benefits">Benefits</a></li>
      <li><a href="/blog/">Blog</a></li>
      <li><a href="/#contact">Contact</a></li>
    </ul>
    <a href="/#trial" class="cta-btn">Free Trial</a>
  </nav>

  <main class="blog-index-wrap">
    <h1>Chess <span class="highlight">Blog</span></h1>
    <p style="color:var(--text-muted); margin-top:.75rem; max-width:560px; font-size:1.05rem;">Expert guides, coaching tips, and insights from FIDE Rated coach Chirag Soni.</p>
    <div class="blog-grid">{cards}</div>
  </main>

  <footer id="contact">
    <div class="footer-container">
      <div class="footer-col"><h2 class="logo">TheChessLifestyle</h2><p class="footer-tagline">Chess for Mental &amp; Cognitive Health.</p></div>
      <div class="footer-col"><h3>Online Classes</h3><ul>
        <li><a href="/online-chess-classes/">Online Chess Classes</a></li>
        <li><a href="/online-chess-classes-for-kids/">For Kids</a></li>
        <li><a href="/online-chess-classes-usa/">USA</a></li>
        <li><a href="/online-chess-classes-uk/">UK</a></li>
        <li><a href="/online-chess-classes-canada/">Canada</a></li>
        <li><a href="/online-chess-classes-australia/">Australia</a></li>
        <li><a href="/online-chess-classes-saudi-arabia/">Saudi Arabia</a></li>
      </ul></div>
      <div class="footer-col"><h3>In-Person (Noida)</h3><ul>
        <li><a href="/chess-classes-noida/">Chess Classes in Noida</a></li>
        <li><a href="/chess-home-tutor-noida/">Chess Home Tutor Noida</a></li>
      </ul></div>
      <div class="footer-col contact-info"><h3>Contact</h3>
        <p>Sector 120, Noida</p>
        <p><a href="tel:+917206789979">7206789979</a></p>
        <a href="mailto:hello@thechesslifestyle.com">hello@thechesslifestyle.com</a>
      </div>
    </div>
    <div class="footer-bottom"><p>&copy; 2026 TheChessLifestyle.</p></div>
  </footer>
  <script src="../main.js" type="module"></script>
</body>
</html>'''

# ─── SITEMAP UPDATER ───────────────────────────────────────────────────────
def update_sitemap(posts):
    """Append blog URLs to sitemap, removing stale blog entries first."""
    with open(SITEMAP_PATH, "r") as f:
        content = f.read()

    # Remove existing blog entries
    content = re.sub(r'\s*<url>\s*<loc>[^<]*/blog/[^<]*</loc>.*?</url>', '', content, flags=re.DOTALL)
    # Add blog index + posts
    new_urls = f"""
  <url>
    <loc>{SITE_URL}/blog/</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>"""
    for p in posts:
        slug = p["meta"].get("slug", "post")
        pub  = p["meta"].get("date", TODAY)
        new_urls += f"""
  <url>
    <loc>{SITE_URL}/blog/{slug}/</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>"""

    content = content.replace("</urlset>", new_urls + "\n</urlset>")
    with open(SITEMAP_PATH, "w") as f:
        f.write(content)
    print(f"  Updated sitemap with {len(posts)+1} blog URLs")

# ─── NEW POST SCAFFOLD ─────────────────────────────────────────────────────
def scaffold_new_post():
    os.makedirs(CONTENT_DIR, exist_ok=True)
    slug = input("Post slug (e.g. chess-improves-focus): ").strip().replace(" ", "-")
    title = input("Title: ").strip()
    desc  = input("Meta description (≤160 chars): ").strip()
    cat   = input("Category (e.g. Chess for Kids): ").strip() or "Chess"
    path  = f"{CONTENT_DIR}/{slug}.md"
    with open(path, "w") as f:
        f.write(f"""---
title: {title}
description: {desc}
date: {TODAY}
author: Chirag Soni
slug: {slug}
category: {cat}
tags: chess, coaching, FIDE rated
image: /glowing_king_hero_1775631608464.webp
read_min: 7
---

## Introduction

Write your opening paragraph here. Hook the reader immediately.

## Section 1 Heading

Your content here.

## Section 2 Heading

Your content here.

## Key Takeaways

- Point 1
- Point 2
- Point 3

## Conclusion

Wrap up and include a soft CTA linking back to the free trial.
""")
    print(f"\n✅ Created: {path}")
    print(f"   Edit it, then run: python3 generate-blog.py")

# ─── MAIN ──────────────────────────────────────────────────────────────────
def main():
    if "--new" in sys.argv:
        scaffold_new_post()
        return

    os.makedirs(CONTENT_DIR, exist_ok=True)
    md_files = sorted(glob.glob(f"{CONTENT_DIR}/*.md"), reverse=True)

    if not md_files:
        print("No posts found in content/posts/. Run with --new to create one.")
        return

    posts = []
    md_parser = markdown.Markdown(extensions=["extra", "toc", "nl2br"])

    for md_path in md_files:
        with open(md_path, "r", encoding="utf-8") as f:
            raw = f.read()
        meta, body = parse_frontmatter(raw)
        slug = meta.get("slug", os.path.splitext(os.path.basename(md_path))[0])
        meta["slug"] = slug

        md_parser.reset()
        html_body = md_parser.convert(body)
        posts.append({"meta": meta, "html": html_body})

        # Write post
        out_dir = f"{BLOG_OUT_DIR}/{slug}"
        os.makedirs(out_dir, exist_ok=True)
        with open(f"{out_dir}/index.html", "w", encoding="utf-8") as f:
            f.write(render_post(meta, html_body))
        print(f"  Created /blog/{slug}/index.html")

    # Write blog index
    os.makedirs(BLOG_OUT_DIR, exist_ok=True)
    with open(f"{BLOG_OUT_DIR}/index.html", "w", encoding="utf-8") as f:
        f.write(render_index(posts))
    print(f"  Created /blog/index.html ({len(posts)} posts)")

    # Update sitemap
    update_sitemap(posts)
    print(f"\nDone! {len(posts)} post(s) generated.")

if __name__ == "__main__":
    main()
