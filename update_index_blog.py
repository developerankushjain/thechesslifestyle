import re

# 1. Read blog cards from blog/index.html
with open("blog/index.html", "r") as f:
    blog_html = f.read()

cards = re.findall(r"(<a[^>]*class=\"[^\"]*blog-card[^\"]*\"[^>]*>.*?</a>)", blog_html, re.DOTALL)
cards_html = "\n          ".join(cards)

# 2. Prepare new blog section HTML
new_blog_html = f"""<div class="scroll-wrapper">
          <div class="scroll-nav prev" id="blog-prev">&#10094;</div>
          <div class="blog-grid horizontal-scroll-container" id="blog-scroll">
          {cards_html}
          </div>
          <div class="scroll-nav next" id="blog-next">&#10095;</div>
        </div>"""

# 3. Read and update index.html
with open("index.html", "r") as f:
    index_html = f.read()

index_html = re.sub(r'<div class="blog-grid">.*?</div>\s*</div>\s*</section>', new_blog_html + '\n      </div>\n    </section>', index_html, flags=re.DOTALL)

# Add blog scroll script if not exists
blog_script = """
      const blogScroll = document.getElementById('blog-scroll');
      const blPrev = document.getElementById('blog-prev');
      const blNext = document.getElementById('blog-next');
      if (blogScroll && blPrev && blNext) {
        blPrev.addEventListener('click', () => blogScroll.scrollBy({ left: -320, behavior: 'smooth' }));
        blNext.addEventListener('click', () => blogScroll.scrollBy({ left: 320, behavior: 'smooth' }));
      }
"""
if "blogScroll.scrollBy" not in index_html:
    index_html = index_html.replace("</script>\n  </body>", blog_script + "</script>\n  </body>")

with open("index.html", "w") as f:
    f.write(index_html)

# 4. Update style.css
with open("style.css", "r") as f:
    css = f.read()

css = css.replace(".benefit-card, .coach-card {", ".benefit-card, .coach-card, .blog-card {")

with open("style.css", "w") as f:
    f.write(css)

print("Blog section updated in index.html and style.css!")
