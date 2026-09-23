import os
import re

with open("index.html", "r") as f:
    index_html = f.read()

navbar_match = re.search(r'(<nav class="navbar">.*?</nav>)', index_html, re.DOTALL)
new_navbar = navbar_match.group(1)
new_navbar = new_navbar.replace('href="#', 'href="/#')
new_navbar = new_navbar.replace('href="./index.html"', 'href="/"')
new_navbar = new_navbar.replace('src="./', 'src="/')

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

directories = ["blog", "usa"]
for item in os.listdir("."):
    if item.startswith("online-chess-classes") and os.path.isdir(item):
        directories.append(item)
    if item.startswith("chess-") and os.path.isdir(item):
        directories.append(item)

# add set to avoid duplicates
directories = list(set(directories))

count = 0
for d in directories:
    if not os.path.exists(d): continue
    for root, dirs, files in os.walk(d):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                with open(filepath, "r") as f:
                    content = f.read()
                
                # Remove any existing mobile menu scripts to avoid duplication
                content = re.sub(r'<!-- Mobile Menu Script -->.*?</script>', '', content, flags=re.DOTALL)
                
                # Replace navbar and footer
                content = re.sub(r'<nav class="navbar">.*?</nav>', new_navbar, content, flags=re.DOTALL)
                content = re.sub(r'<footer[^>]*>.*?</footer>', new_footer, content, flags=re.DOTALL)
                
                with open(filepath, "w") as f:
                    f.write(content)
                count += 1

print(f"Navbar and Footer updated globally in {count} files!")
