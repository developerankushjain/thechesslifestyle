import re

html_path = "index.html"
with open(html_path, "r") as f:
    content = f.read()

images = [
    "20260418_141700.jpg",
    "20260418_141727.jpg",
    "20260603_101319.jpg",
    "20260715_111140.jpg",
    "20260715_111545.jpg",
    "20260715_111546.jpg",
    "20260822_110914.jpg",
    "20260822_121216.jpg",
    "20260822_121240.jpg",
]

def replacement(match):
    img = images.pop(0) if images else "IMG-20260714-WA0001.jpg"
    img_tag = f'\n            <img src="./gallery/{img}" alt="Benefit" class="benefit-img" loading="lazy" />'
    return match.group(0) + img_tag

if "class=\"benefit-img\"" not in content:
    content = re.sub(r'<div class="benefit-card">', replacement, content)

with open(html_path, "w") as f:
    f.write(content)

css_add = """

/* --- IMAGE-FIRST MOBILE OVERHAUL --- */
.benefit-img {
  width: 100%;
  height: 160px;
  object-fit: cover;
  border-radius: var(--radius-md);
  margin-bottom: 1rem;
}

@media (max-width: 768px) {
  /* Restructure Hero */
  .hero {
    display: flex;
    flex-direction: column;
    padding-top: 5rem !important; /* Nav spacing */
    padding-bottom: 2rem !important;
  }
  .hero::before {
    display: none !important; /* Rip out the gradient */
  }
  .hero-bg-img {
    position: relative !important;
    width: 100% !important;
    height: 300px !important;
    border-radius: var(--radius-lg) !important;
    margin-bottom: 2rem !important;
    margin-top: 1rem !important;
    object-position: center !important;
    box-shadow: var(--shadow-md) !important;
  }

  /* Restructure Why Us */
  #why-us {
    display: flex !important;
    flex-direction: column !important;
    padding-top: 2rem !important;
  }
  #why-us::before {
    display: none !important; /* Rip out gradient */
  }
  .why-us-bg-img {
    position: relative !important;
    width: 100% !important;
    height: 250px !important;
    border-radius: var(--radius-lg) !important;
    margin-bottom: 2rem !important;
    object-position: center !important;
    box-shadow: var(--shadow-md) !important;
  }
  #why-us .container {
    padding-top: 0 !important;
  }
}
"""

with open("style.css", "a") as f:
    f.write(css_add)

print("Visual overhaul complete!")
