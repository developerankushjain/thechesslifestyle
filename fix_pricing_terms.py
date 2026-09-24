import re

css_additions = """
/* Pricing Terms & Bonuses Styling */
.terms-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  max-width: 1200px;
  margin: 4rem auto 0;
  padding: 0 5%;
}
.term-card {
  background: var(--bg-card);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  padding: 2rem;
  box-shadow: var(--shadow-sm);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  text-align: center;
}
.term-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-md);
  border-color: var(--primary);
}
.term-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}
.term-card h4 {
  font-size: 1.3rem;
  color: var(--text-main);
  margin-bottom: 0.5rem;
}
.term-card p {
  color: var(--text-muted);
  font-size: 0.95rem;
  margin-bottom: 1.5rem;
}
.highlight-box {
  background: rgba(245, 158, 11, 0.1);
  color: var(--primary);
  padding: 1rem;
  border-radius: var(--radius-sm);
  font-weight: 600;
  font-size: 0.9rem;
  border: 1px dashed var(--primary);
}
.discount-list {
  list-style: none;
  padding: 0;
  margin: 0;
  text-align: left;
}
.discount-list li {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.8rem 0;
  border-bottom: 1px solid var(--border-light);
  color: var(--text-main);
  font-weight: 500;
}
.discount-list li:last-child {
  border-bottom: none;
}
.discount-list .pct {
  background: var(--primary);
  color: #fff;
  padding: 0.2rem 0.6rem;
  border-radius: 12px;
  font-size: 0.85rem;
  font-weight: 700;
}
"""

with open("style.css", "r") as f:
    style_css = f.read()
if "/* Pricing Terms & Bonuses Styling */" not in style_css:
    with open("style.css", "a") as f:
        f.write("\n" + css_additions)

with open("pricing/index.html", "r") as f:
    pricing_html = f.read()

# Fix currency selector wrapper style
old_wrapper_style = r'<div class="currency-selector-wrapper scroll-reveal" style="text-align: right; margin-top: -3rem; margin-bottom: 2rem; max-width: 1200px; margin-left: auto; margin-right: auto; padding-right: 5%;">'
new_wrapper_style = r'<div class="currency-selector-wrapper scroll-reveal" style="display: flex; justify-content: flex-end; max-width: 1200px; margin: -2rem auto 2rem; padding: 0 5%;">'
pricing_html = pricing_html.replace(old_wrapper_style, new_wrapper_style)

with open("pricing/index.html", "w") as f:
    f.write(pricing_html)

print("Pricing terms styled and selector fixed!")
