import os
import re

def process_city_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'style-city.css' in content: return
    content = content.replace('href="../style.css"', 'href="../style-city.css"')
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        print(f"Updated {filepath}")

def process_blog_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'style-blog.css' in content: return
    content = content.replace('href="../../style.css"', 'href="../../style-blog.css"')
    content = content.replace('href="../style.css"', 'href="../style-blog.css"')
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        print(f"Updated {filepath}")

for root, dirs, files in os.walk('.'):
    if 'node_modules' in dirs: dirs.remove('node_modules')
    if '.git' in dirs: dirs.remove('.git')
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            if '/blog' in path or '/dist/blog' in path:
                process_blog_file(path)
            elif '/online-chess-classes' in path or 'noida' in path:
                process_city_file(path)

# Update generators
with open('generate-cities.py', 'r', encoding='utf-8') as f:
    c = f.read()
c = c.replace('href="../style.css"', 'href="../style-city.css"')
with open('generate-cities.py', 'w', encoding='utf-8') as f:
    f.write(c)
print("Updated generate-cities.py")

with open('generate-blog.py', 'r', encoding='utf-8') as f:
    b = f.read()
b = b.replace('href="../../style.css"', 'href="../../style-blog.css"')
b = b.replace('href="../style.css"', 'href="../style-blog.css"')
with open('generate-blog.py', 'w', encoding='utf-8') as f:
    f.write(b)
print("Updated generate-blog.py")

