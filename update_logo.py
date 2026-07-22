import os

countries = [
    "online-chess-classes-usa",
    "online-chess-classes-uk",
    "online-chess-classes-canada",
    "online-chess-classes-australia",
    "online-chess-classes-saudi-arabia",
    "online-chess-classes-uae"
]

# We want to replace:
#       <div class="logo">
#         <img src="/favicon.svg" alt="TheChessLifestyle" class="logo-icon" width="28" height="31" loading="lazy"/>
#         <a href="/" style="color: white; text-decoration: none"
#           >TheChessLifestyle</a
#         >
#       </div>
# with the proper flex link.

import re

for country in countries:
    file_path = f"{country}/index.html"
    if not os.path.exists(file_path):
        continue
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # The HTML parser might format it differently, so we use a regex to match the entire .logo div inside <nav>
    pattern = re.compile(r'<div class="logo">.*?</div>', re.DOTALL)
    replacement = '''<a href="/" class="logo">
        <img src="/favicon.svg" alt="TheChessLifestyle Chess King Logo" class="logo-icon" width="32" height="35" loading="eager"/>
        TheChessLifestyle
      </a>'''
    
    new_content = pattern.sub(replacement, content, count=1)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print(f"Updated logo in {file_path}")
