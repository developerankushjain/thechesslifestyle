import os, glob

BASE = "/Users/apple/Desktop/Projects/thechesslifestyle"

for fpath in glob.glob(f"{BASE}/**/*.html", recursive=True):
    if "dist/" in fpath or ".gemini" in fpath or "node_modules" in fpath:
        continue

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    original = content
    
    # We will just replace the .cc-select and .phone-combo input[type="tel"] selectors
    # to be more specific and include !important to override the general form CSS.
    
    old_cc_select = ".cc-select {\n      flex: 0 0 auto;\n      width: 130px;"
    new_cc_select = ".cc-select {\n      flex: 0 0 auto !important;\n      width: 150px !important;"
    
    if old_cc_select in content:
        content = content.replace(old_cc_select, new_cc_select)
        
    # Let's just find `.cc-select {` and make sure it has !important for width
    # Actually, we can use regex to inject !important if it's missing.
    import re
    content = re.sub(r'width:\s*130px;', 'width: 150px !important;', content)
    
    # Make sure phone input is flex 1 and width auto!
    content = content.replace('.phone-combo input[type="tel"] {', '.phone-combo input[type="tel"] {\n      width: 100% !important;\n      flex: 1 1 auto !important;')
    
    # Wait, width: 100% with flex: 1 might overflow, width: auto or min-width: 0 is better for flex child.
    content = content.replace('width: 100% !important;\n      flex: 1 1 auto !important;\n      flex: 1;', 'min-width: 0 !important;\n      flex: 1 1 auto !important;')
    content = content.replace('.phone-combo input[type="tel"] {\n      flex: 1;', '.phone-combo input[type="tel"] {\n      flex: 1 1 auto !important;\n      min-width: 0 !important;')

    if content != original:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Fixed CSS: {fpath}")

print("Done fixing CSS.")
