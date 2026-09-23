css_add = """

/* --- MOBILE OPTIMIZATIONS (ADDED FOR PREMIUM UX) --- */
@media (max-width: 768px) {
  /* 1. Typography & Spacing */
  .hero-content h1 {
    font-size: 2.2rem !important;
  }
  .section-title {
    font-size: 1.8rem;
  }
  .hero, #why-us, .section-alt, #coaches, #gallery {
    padding-top: 4rem !important;
    padding-bottom: 4rem !important;
  }
  
  /* 2. Edge-to-edge Horizontal Scrolling */
  .horizontal-scroll-container {
    width: calc(100% + 3rem) !important;
    margin-left: -1.5rem;
    margin-right: -1.5rem;
    padding: 1rem 1.5rem 2rem 1.5rem !important;
  }
  
  .gallery-scroll-container {
    width: calc(100% + 3rem) !important;
    margin-left: -1.5rem;
    margin-right: -1.5rem;
    padding: 0 1.5rem 2rem 1.5rem !important;
  }
  
  .benefit-card, .coach-card, .gallery-scroll-container .gallery-item {
    flex: 0 0 280px !important; /* Slimmer width so the next card peeks */
  }
  
  /* 3. Forms & Buttons */
  .btn, .cta-btn, button[type="submit"] {
    width: 100%;
    text-align: center;
    justify-content: center;
    padding: 1rem 1.5rem !important;
  }
  
  .phone-input-group {
    flex-direction: column;
    gap: 0.75rem;
  }
  .phone-input-group select, .phone-input-group input {
    width: 100% !important;
    min-width: 100% !important;
  }
}
"""

with open("style.css", "a") as f:
    f.write(css_add)

print("CSS appended successfully!")
