import os
import re

directories = ["blog", "usa"]
for item in os.listdir("."):
    if item.startswith("online-chess-classes") and os.path.isdir(item):
        directories.append(item)

for d in directories:
    if not os.path.exists(d): continue
    for root, dirs, files in os.walk(d):
        for f in files:
            if f.endswith(".html"):
                path = os.path.join(root, f)
                with open(path, "r") as html_file:
                    content = html_file.read()
                
                # Replace inline dark mode text variables
                content = content.replace("var(--text-primary)", "var(--text-main)")
                content = content.replace("var(--text-secondary)", "var(--text-muted)")
                
                # Replace glassmorphism background and borders
                content = content.replace("background: rgba(255,255,255,.04);", "background: var(--bg-card);")
                content = content.replace("background: rgba(255, 255, 255, 0.04);", "background: var(--bg-card);")
                content = content.replace("border: 1px solid rgba(255,255,255,.08);", "border: 1px solid var(--border-light);")
                content = content.replace("border: 1px solid rgba(255, 255, 255, 0.08);", "border: 1px solid var(--border-light);")
                
                # Fix blockquote background (can stay slightly tinted amber)
                # content = content.replace("background: rgba(245,158,11,.06);", "background: rgba(245,158,11,.06);") 
                
                with open(path, "w") as html_file:
                    html_file.write(content)

print("Inline styles updated for light theme!")
