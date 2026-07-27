import re

# Fix generate-pages.js
with open('generate-pages.js', 'r', encoding='utf-8') as f:
    c = f.read()
c = re.sub(r'<p><strong>FIDE ID:</strong>.*?25971115.*?</a></p>', '<div class="fide-badge">FIDE ID: 25971115 &nbsp;|&nbsp; Peak FIDE Rating: 1729</div>', c, flags=re.DOTALL)
with open('generate-pages.js', 'w', encoding='utf-8') as f:
    f.write(c)
print("Updated generate-pages.js")

# Now re-run JS generator
import os
os.system("node generate-pages.js")

