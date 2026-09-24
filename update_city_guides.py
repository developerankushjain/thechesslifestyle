import os
import re

directories = [d for d in os.listdir('.') if os.path.isdir(d) and d.startswith('online-chess-classes-')]

with open('index.html', 'r') as f:
    index_html = f.read()

# Extract Sections
coaches_match = re.search(r'(<section id="coaches".*?</section>)', index_html, re.DOTALL)
coaches_html = coaches_match.group(1) if coaches_match else ""

gallery_match = re.search(r'(<section id="gallery".*?</section>)', index_html, re.DOTALL)
gallery_html = gallery_match.group(1) if gallery_match else ""

test_match = re.search(r'(<section id="testimonials".*?</section>)', index_html, re.DOTALL)
test_html = test_match.group(1) if test_match else ""

combined_sections = coaches_html + "\n\n" + gallery_html + "\n\n" + test_html

# Fix relative paths to absolute paths
combined_sections = combined_sections.replace('src="./', 'src="/').replace('href="./', 'href="/')

scroll_script = """
<script>
      const coachesScroll = document.getElementById('coaches-scroll');
      const cPrev = document.getElementById('coaches-prev');
      const cNext = document.getElementById('coaches-next');
      if (coachesScroll && cPrev && cNext) {
        cPrev.addEventListener('click', () => coachesScroll.scrollBy({ left: -320, behavior: 'smooth' }));
        cNext.addEventListener('click', () => coachesScroll.scrollBy({ left: 320, behavior: 'smooth' }));
      }
      
      const galleryScroll = document.getElementById('gallery-scroll');
      const gPrev = document.getElementById('gallery-prev');
      const gNext = document.getElementById('gallery-next');
      if (galleryScroll && gPrev && gNext) {
        gPrev.addEventListener('click', () => galleryScroll.scrollBy({ left: -320, behavior: 'smooth' }));
        gNext.addEventListener('click', () => galleryScroll.scrollBy({ left: 320, behavior: 'smooth' }));
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

for directory in directories:
    file_path = os.path.join(directory, "index.html")
    if not os.path.exists(file_path):
        continue

    with open(file_path, 'r') as f:
        html = f.read()

    # 1. Remove glow-tracker
    html = re.sub(r'<div class="glow-tracker".*?</div>', '', html, flags=re.DOTALL)

    # 2. Replace old sections with combined global sections
    pattern = r'<!-- HIGH DWELL TIME SECTION -->.*?<section id="enrol"'
    replacement = combined_sections + '\n\n    <section id="enrol"'
    html = re.sub(pattern, replacement, html, flags=re.DOTALL)
    
    # 3. Inject JS if not present
    if "coachesScroll" not in html:
        html = html.replace('</body>', scroll_script + '\n</body>')

    with open(file_path, 'w') as f:
        f.write(html)

print("Batch update completed!")
