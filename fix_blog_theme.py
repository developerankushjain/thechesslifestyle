import re

with open("style-blog.css", "r") as f:
    old_css = f.read()

# Extract .footer-container and related classes
footer_pattern = r'(\.footer-container\s*\{[^}]+\})'
footer_col_pattern = r'(\.footer-col\s*\{[^}]+\})'
footer_tagline_pattern = r'(\.footer-tagline\s*\{[^}]+\})'
footer_bottom_pattern = r'(\.footer-bottom\s*\{[^}]+\})'
contact_info_pattern = r'(\.contact-info\s*\{[^}]+\})'
footer_h3_pattern = r'(\.footer-col\s+h3\s*\{[^}]+\})'
footer_ul_pattern = r'(\.footer-col\s+ul\s*\{[^}]+\})'
footer_li_pattern = r'(\.footer-col\s+li\s*\{[^}]+\})'
footer_a_pattern = r'(\.footer-col\s+a\s*\{[^}]+\})'
footer_a_hover_pattern = r'(\.footer-col\s+a:hover\s*\{[^}]+\})'
footer_p_pattern = r'(\.footer-col\s+p\s*\{[^}]+\})'

# Actually, the footer classes start around "footer {" to the end of the footer section.
# Let's just extract all CSS rules that start with .footer or footer
footer_blocks = re.findall(r'(\.footer-[a-zA-Z0-9_-]+(?:\s+[a-zA-Z0-9_-]+)*\s*\{[^}]+\})', old_css)
contact_blocks = re.findall(r'(\.contact-info\s*\{[^}]+\})', old_css)
footer_tag_blocks = re.findall(r'(footer\s*\{[^}]+\})', old_css)

extra_css = "\n\n/* --- LEGACY FOOTER CLASSES FOR BLOG --- */\n"
for b in footer_blocks + contact_blocks + footer_tag_blocks:
    extra_css += b + "\n"

# Now copy style.css to style-blog.css
with open("style.css", "r") as f:
    new_css = f.read()

# Write both to style-blog.css
with open("style-blog.css", "w") as f:
    f.write(new_css + extra_css)

print("style-blog.css has been fully synchronized with style.css!")
