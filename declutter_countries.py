import os

countries = [
    "online-chess-classes-usa",
    "online-chess-classes-uk",
    "online-chess-classes-canada",
    "online-chess-classes-australia",
    "online-chess-classes-saudi-arabia",
    "online-chess-classes-uae"
]

def remove_block(content, start_marker, end_marker):
    start_idx = content.find(start_marker)
    if start_idx == -1:
        return content
    end_idx = content.find(end_marker, start_idx)
    if end_idx == -1:
        return content
    # Remove from start_idx to end_idx + len(end_marker)
    return content[:start_idx] + content[end_idx + len(end_marker):]

for country in countries:
    file_path = f"{country}/index.html"
    if not os.path.exists(file_path):
        print(f"Skipping {file_path}")
        continue
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Reduce padding
    content = content.replace("padding: 6rem 5%;", "padding: 4rem 5%;")
    content = content.replace("padding:6rem 5%;", "padding:4rem 5%;")

    # 2. Remove first coach section (redundant)
    # Finding exact string since it might vary slightly with whitespace
    coach_start = '      <!-- Coach Section -->\n      <section\n        id="coach"\n        class="coach-profile section-alt scroll-reveal"\n      >'
    if coach_start not in content:
        coach_start = '      <!-- Coach Section -->\n      <section id="coach" class="coach-profile section-alt scroll-reveal">'
        if coach_start not in content:
            # Let's try to find it more dynamically
            idx = content.find('<!-- Coach Section -->')
            if idx != -1:
                end_idx = content.find('</section>', idx)
                if end_idx != -1:
                    content = content[:idx] + content[end_idx+10:]
                    
    # 3. Remove second generic testimonials
    # In USA it's: <section class="scroll-reveal" style="padding-top: 2rem;"> ... What Parents Say ... </section>
    test_start_idx = content.find('<section class="scroll-reveal" style="padding-top: 2rem;">\n      <h2 style="margin-bottom: 2rem;">What Parents Say</h2>')
    if test_start_idx != -1:
        test_end_idx = content.find('</section>', test_start_idx)
        if test_end_idx != -1:
            content = content[:test_start_idx] + content[test_end_idx+10:]

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Processed {file_path}")
