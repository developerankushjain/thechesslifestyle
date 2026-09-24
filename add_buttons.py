import re

with open('pricing/index.html', 'r') as f:
    content = f.read()

def inject_button(match):
    return match.group(0) + '\n            <a href="/#trial" class="btn-primary" style="margin-top: auto; text-align: center; display: block; padding: 1rem; border-radius: 8px; font-weight: 600;">Book Trial Class</a>'

content = re.sub(r'<ul class="pricing-features">.*?</ul>', inject_button, content, flags=re.DOTALL)

with open('pricing/index.html', 'w') as f:
    f.write(content)

print("Buttons added successfully!")
