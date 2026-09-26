import os, glob, re

BASE = "/Users/apple/Desktop/Projects/thechesslifestyle"

for fpath in glob.glob(f"{BASE}/**/*.html", recursive=True):
    if "dist/" in fpath or ".gemini" in fpath or "node_modules" in fpath:
        continue

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    original = content
    
    # 1. Simplify phone combo CSS and layout to be foolproof
    # In CSS, remove the tight combo styling and add a gap
    content = content.replace(".phone-combo { display: flex; gap: 0; width: 100%; }", ".phone-combo { display: flex; gap: 0.5rem; width: 100%; }")
    content = content.replace("border-radius: 10px 0 0 10px;", "border-radius: 10px;")
    content = content.replace("border-right: none;", "")
    content = content.replace("border-radius: 0 10px 10px 0 !important;", "border-radius: 10px !important;")
    content = content.replace("border-radius: 10px 10px 0 0;", "border-radius: 10px;")
    content = content.replace("border-radius: 0 0 10px 10px !important;", "border-radius: 10px !important;")
    content = content.replace("border-right: 1.5px solid #e2e8f0; border-bottom: none;", "")

    # Make the input take full remaining width properly
    content = content.replace("width: 185px;", "width: 130px;")

    # Rename 'Phone Number' to 'WhatsApp Number' to be explicit
    content = content.replace('name="Phone Number" placeholder="WhatsApp / Phone Number *"', 'name="WhatsApp Number" placeholder="WhatsApp Number *"')

    # 2. Remove "Country" and "City" fields
    # Pattern for City/Country row
    content = re.sub(
        r'<div class="form-row">\s*<div class="fg" style="margin-bottom:0;"><input type="text" name="Age or Class" placeholder="Age / Grade \*" required></div>\s*<div class="fg" style="margin-bottom:0;"><input type="text" name="(Country|City)" placeholder="[^"]*"></div>\s*</div>',
        r'<div class="fg"><input type="text" name="Age or Class" placeholder="Age / Grade *" required></div>',
        content
    )

    if content != original:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Fixed: {fpath}")

print("Done fixing forms.")
