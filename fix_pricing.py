import re

# --- 1. CSS UPDATES ---
css_additions = """
/* Pricing Section Styles */
.pricing-section {
  padding: 120px 5% 4rem;
  background-color: var(--bg-alt);
}
.pricing-header {
  text-align: center;
  max-width: 800px;
  margin: 0 auto 4rem;
}
.pricing-header h1 {
  font-size: 3rem;
  margin-bottom: 1rem;
}
.pricing-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}
.pricing-card {
  background: var(--bg-card);
  border-radius: var(--radius-lg);
  border: 1px solid var(--border-light);
  padding: 2.5rem;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  position: relative;
  display: flex;
  flex-direction: column;
}
.pricing-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-lg);
}
.pricing-card.popular {
  border: 2px solid var(--primary);
  box-shadow: var(--shadow-md);
}
.pricing-badge {
  position: absolute;
  top: -15px;
  left: 50%;
  transform: translateX(-50%);
  background: var(--primary);
  color: #fff;
  padding: 0.4rem 1.2rem;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
}
.pricing-card h3 {
  font-size: 1.6rem;
  margin-bottom: 0.5rem;
  color: var(--text-main);
}
.rating-target {
  font-size: 0.9rem;
  color: var(--text-muted);
  margin-bottom: 1.5rem;
  font-weight: 500;
}
.price {
  font-size: 2.5rem;
  font-weight: 900;
  color: var(--text-main);
  margin-bottom: 0.5rem;
  font-family: 'Outfit', sans-serif;
}
.price span {
  font-size: 1rem;
  font-weight: 400;
  color: var(--text-muted);
}
.pricing-features {
  list-style: none;
  padding: 0;
  margin: 1.5rem 0 0 0;
  flex-grow: 1;
}
.pricing-features li {
  position: relative;
  padding-left: 1.8rem;
  margin-bottom: 1rem;
  color: var(--text-main);
  line-height: 1.5;
}
.pricing-features li::before {
  content: "✓";
  position: absolute;
  left: 0;
  color: var(--primary);
  font-weight: 900;
}
.inclusion {
  font-weight: 600;
  color: var(--primary) !important;
}
.inclusion::before {
  content: "★" !important;
}
"""

with open("style.css", "r") as f:
    style_css = f.read()
if "/* Pricing Section Styles */" not in style_css:
    with open("style.css", "a") as f:
        f.write("\n" + css_additions)

# --- 2. HTML UPDATES ---

with open("index.html", "r") as f:
    index_html = f.read()

# Extract Navbar
navbar_match = re.search(r'(<nav class="navbar">.*?</nav>)', index_html, re.DOTALL)
new_navbar = navbar_match.group(1)
new_navbar = new_navbar.replace('href="#', 'href="/#')
new_navbar = new_navbar.replace('href="./index.html"', 'href="/"')
new_navbar = new_navbar.replace('src="./', 'src="/')

# Extract Footer
footer_match = re.search(r'(<footer>.*?</footer>)', index_html, re.DOTALL)
new_footer = footer_match.group(1)
new_footer = new_footer.replace('href="#', 'href="/#')
new_footer = new_footer.replace('href="./', 'href="/')
new_footer = new_footer.replace('src="./', 'src="/')

mobile_menu_script = """
    <!-- Mobile Menu Script -->
    <script>
      const toggle = document.getElementById('mobile-menu-toggle');
      if (toggle) {
        toggle.addEventListener('click', function() {
          document.getElementById('nav-links').classList.toggle('active');
        });
      }
      document.querySelectorAll('.nav-links a').forEach(link => {
        link.addEventListener('click', () => {
          const navLinks = document.getElementById('nav-links');
          if(navLinks) navLinks.classList.remove('active');
        });
      });
    </script>
"""
new_footer += "\n" + mobile_menu_script

with open("pricing/index.html", "r") as f:
    pricing_html = f.read()

# Remove old navbar and footer
pricing_html = re.sub(r'<nav class="navbar">.*?</nav>', new_navbar, pricing_html, flags=re.DOTALL)
pricing_html = re.sub(r'<footer[^>]*>.*?</footer>', new_footer, pricing_html, flags=re.DOTALL)

# Remove svg-floater, glow-tracker, mobile-sticky-cta
pricing_html = re.sub(r'<div class="svg-floater".*?</div>', '', pricing_html, flags=re.DOTALL)
pricing_html = re.sub(r'<div class="glow-tracker".*?</div>', '', pricing_html, flags=re.DOTALL)
pricing_html = re.sub(r'<div class="mobile-sticky-cta".*?</div>', '', pricing_html, flags=re.DOTALL)
pricing_html = re.sub(r'<!-- Mobile Menu Script -->.*?</script>', '', pricing_html, flags=re.DOTALL)

# Fix class names
pricing_html = pricing_html.replace(' tilt-card mobile-glow', '')
pricing_html = pricing_html.replace('mobile-glow', '')

with open("pricing/index.html", "w") as f:
    f.write(pricing_html)

print("Pricing page updated successfully!")
