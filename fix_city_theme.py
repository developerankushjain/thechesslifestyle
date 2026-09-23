import re

with open("style-city.css", "r") as f:
    css = f.read()

with open("style.css", "r") as f:
    style_css = f.read()

# 1. Extract the :root from style.css
root_match = re.search(r'(:root\s*\{[^}]+\})', style_css)
if root_match:
    root_css = root_match.group(1)
    # Replace :root in style-city.css
    css = re.sub(r':root\s*\{[^}]+\}', root_css, css)

# 2. Extract the body from style.css
body_match = re.search(r'(body\s*\{[^}]+\})', style_css)
if body_match:
    body_css = body_match.group(1)
    # Replace body in style-city.css
    css = re.sub(r'body\s*\{[^}]+\}', body_css, css)

# 3. Completely delete body::before
css = re.sub(r'body::before\s*\{[^}]+\}', '', css)

# 4. Fix .navbar
css = css.replace("background: rgba(7, 9, 14, 0.8);", "background: rgba(255, 255, 255, 0.9);")
css = css.replace("color: #fff;", "color: var(--text-main);")

with open("style-city.css", "w") as f:
    f.write(css)

print("style-city.css patched for light mode!")
