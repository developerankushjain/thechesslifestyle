import re

with open("index.html", "r") as f:
    index_html = f.read()

# Extract Coaches Section
coaches_match = re.search(r'(<section id="coaches".*?</section>)', index_html, re.DOTALL)
coaches_html = coaches_match.group(1)

# Extract Testimonials Section
test_match = re.search(r'(<section id="testimonials".*?</section>)', index_html, re.DOTALL)
test_html = test_match.group(1)

with open("pricing/index.html", "r") as f:
    pricing_html = f.read()

# Fix coaches section replacement
pricing_html = re.sub(r'<section[^>]*>\s*<div class="coach-section".*?</section>', coaches_html, pricing_html, flags=re.DOTALL)

# Fix testimonials section replacement
pricing_html = re.sub(r'<section[^>]*>\s*<h2[^>]*>What Parents Say.*?</div>\s*</section>', test_html, pricing_html, flags=re.DOTALL)

# Also need to inject the scrolling JS since we added horizontal carousels!
scroll_script = """
<script>
      const coachesScroll = document.getElementById('coaches-scroll');
      const cPrev = document.getElementById('coaches-prev');
      const cNext = document.getElementById('coaches-next');
      if (coachesScroll && cPrev && cNext) {
        cPrev.addEventListener('click', () => coachesScroll.scrollBy({ left: -320, behavior: 'smooth' }));
        cNext.addEventListener('click', () => coachesScroll.scrollBy({ left: 320, behavior: 'smooth' }));
      }
      
      const testimonialsScroll = document.getElementById('testimonials-scroll');
      const tPrev = document.getElementById('testimonials-prev');
      const tNext = document.getElementById('testimonials-next');
      if (testimonialsScroll && tPrev && tNext) {
        tPrev.addEventListener('click', () => testimonialsScroll.scrollBy({ left: -320, behavior: 'smooth' }));
        tNext.addEventListener('click', () => testimonialsScroll.scrollBy({ left: 320, behavior: 'smooth' }));
      }
</script>
"""
if "coachesScroll" not in pricing_html:
    pricing_html = pricing_html.replace('</body>', scroll_script + '\n</body>')

with open("pricing/index.html", "w") as f:
    f.write(pricing_html)

print("Pricing page sections replaced!")
