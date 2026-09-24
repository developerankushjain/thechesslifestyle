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

# 1. Remove paragraph
para_to_remove = r'<p style="color:var\(--text-muted\);font-size:0\.9rem;margin-top:0\.75rem;">Prices shown in INR.*?month USD</strong>\.</p>'
pricing_html = re.sub(para_to_remove, '', pricing_html, flags=re.DOTALL)

# 2. Make currency selector smaller
old_selector = r'<div class="currency-selector-wrapper scroll-reveal">'
new_selector = r'<div class="currency-selector-wrapper scroll-reveal" style="text-align: right; margin-top: -3rem; margin-bottom: 2rem; max-width: 1200px; margin-left: auto; margin-right: auto; padding-right: 5%;">'
pricing_html = pricing_html.replace(old_selector, new_selector)

old_select = r'<select id="currency-selector" class="currency-select">'
new_select = r'<select id="currency-selector" class="currency-select" style="padding: 0.2rem 0.5rem; font-size: 0.8rem; background: var(--bg-alt); border-radius: 4px; box-shadow: none;">'
pricing_html = pricing_html.replace(old_select, new_select)

old_label = r'<label for="currency-selector" style="margin-right:10px; font-weight:500;">Select Currency:</label>'
new_label = r'<label for="currency-selector" style="margin-right:5px; font-weight:500; font-size: 0.8rem; color: var(--text-muted);">Currency:</label>'
pricing_html = pricing_html.replace(old_label, new_label)

# 3. Replace coach and testimonial sections
# The old coach section starts with <section>\s*<div class="coach-section" and ends with </section>
pricing_html = re.sub(r'<section>\s*<div class="coach-section".*?</section>', coaches_html, pricing_html, flags=re.DOTALL)

# The old review section starts with <section class="scroll-reveal" style="padding-top: 2rem;"> and ends with </section>
pricing_html = re.sub(r'<section class="scroll-reveal" style="padding-top: 2rem;">.*?</section>', test_html, pricing_html, flags=re.DOTALL)

with open("pricing/index.html", "w") as f:
    f.write(pricing_html)

print("Pricing page details updated!")
