import re

# 1. Update style.css
css_additions = """
/* Pricing WOW Enhancements */
.pricing-card {
  background: linear-gradient(145deg, #ffffff, #fafafa);
  position: relative;
  overflow: visible;
}
.pricing-card::before {
  content: "";
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  border-radius: var(--radius-lg);
  box-shadow: inset 0 0 0 1px rgba(255,255,255,0.5);
  pointer-events: none;
}
.pricing-card:hover {
  transform: translateY(-8px) scale(1.02);
  box-shadow: 0 20px 40px rgba(245, 158, 11, 0.15), 0 10px 15px -3px rgba(0,0,0,0.1);
  border-color: rgba(245, 158, 11, 0.3);
}
@media (min-width: 1024px) {
  .pricing-card.popular {
    transform: scale(1.05);
    z-index: 10;
  }
  .pricing-card.popular:hover {
    transform: translateY(-8px) scale(1.07);
  }
}
@keyframes pulse-badge {
  0% { box-shadow: 0 0 0 0 rgba(245, 158, 11, 0.4); }
  70% { box-shadow: 0 0 0 10px rgba(245, 158, 11, 0); }
  100% { box-shadow: 0 0 0 0 rgba(245, 158, 11, 0); }
}
.pricing-badge {
  animation: pulse-badge 2s infinite;
  box-shadow: 0 4px 10px rgba(245, 158, 11, 0.3);
}
.currency-selector-wrapper {
  text-align: center;
  margin-bottom: 3rem;
}
.currency-select {
  padding: 0.6rem 1.2rem;
  border-radius: 8px;
  border: 1px solid var(--border-light);
  background: var(--bg-card);
  font-family: 'Inter', sans-serif;
  font-size: 1rem;
  font-weight: 500;
  color: var(--text-main);
  cursor: pointer;
  outline: none;
  box-shadow: var(--shadow-sm);
  transition: all 0.2s;
}
.currency-select:hover {
  border-color: var(--primary);
}
"""

with open("style.css", "r") as f:
    style_css = f.read()
if "/* Pricing WOW Enhancements */" not in style_css:
    with open("style.css", "a") as f:
        f.write("\n" + css_additions)

# 2. Update pricing/index.html
with open("pricing/index.html", "r") as f:
    html = f.read()

# Inject currency selector
selector_html = """
        <div class="currency-selector-wrapper scroll-reveal">
          <label for="currency-selector" style="margin-right:10px; font-weight:500;">Select Currency:</label>
          <select id="currency-selector" class="currency-select">
            <option value="INR">🇮🇳 INR (₹)</option>
            <option value="USD">🇺🇸 USD ($)</option>
            <option value="GBP">🇬🇧 GBP (£)</option>
            <option value="EUR">🇪🇺 EUR (€)</option>
            <option value="AUD">🇦🇺 AUD (A$)</option>
            <option value="CAD">🇨🇦 CAD (C$)</option>
          </select>
        </div>
"""
if "currency-selector-wrapper" not in html:
    html = html.replace('<div class="pricing-grid scroll-reveal">', selector_html + '\n        <div class="pricing-grid scroll-reveal">')

# Map pricing tiers
# 4999 -> 60 USD
# 3999 -> 50 USD
# 5999 -> 75 USD
# 6999 -> 85 USD
# 9999 -> 120 USD

pricing_map = {
    "4,999": 'data-inr="4,999" data-usd="60" data-gbp="45" data-eur="55" data-aud="80" data-cad="80"',
    "3,999": 'data-inr="3,999" data-usd="50" data-gbp="40" data-eur="45" data-aud="65" data-cad="65"',
    "5,999": 'data-inr="5,999" data-usd="75" data-gbp="55" data-eur="65" data-aud="100" data-cad="100"',
    "6,999": 'data-inr="6,999" data-usd="85" data-gbp="65" data-eur="75" data-aud="115" data-cad="115"',
    "9,999": 'data-inr="9,999" data-usd="120" data-gbp="90" data-eur="110" data-aud="160" data-cad="160"',
}

for inr_val, attrs in pricing_map.items():
    old_tag = f'<div class="price">₹{inr_val}'
    new_tag = f'<div class="price" {attrs}>₹{inr_val}'
    html = html.replace(old_tag, new_tag)

# Inject JS
js_logic = """
<script>
document.addEventListener("DOMContentLoaded", function() {
  const currencySelector = document.getElementById("currency-selector");
  const prices = document.querySelectorAll(".price");
  
  const currencySymbols = {
    "INR": "₹", "USD": "$", "GBP": "£", "EUR": "€", "AUD": "A$", "CAD": "C$"
  };

  function updatePrices(currency) {
    prices.forEach(priceEl => {
      const val = priceEl.getAttribute(`data-${currency.toLowerCase()}`);
      if (val) {
        priceEl.innerHTML = `${currencySymbols[currency]}${val}<span> / month</span>`;
      }
    });
  }

  if (currencySelector) {
    currencySelector.addEventListener("change", function(e) {
      updatePrices(e.target.value);
    });
  }

  fetch("https://ipapi.co/json/")
    .then(response => response.json())
    .then(data => {
      let detectedCurrency = "INR";
      const country = data.country_code;
      if (country === "US") detectedCurrency = "USD";
      else if (country === "GB") detectedCurrency = "GBP";
      else if (["AU", "NZ"].includes(country)) detectedCurrency = "AUD";
      else if (country === "CA") detectedCurrency = "CAD";
      else if (["FR", "DE", "IT", "ES", "NL", "BE", "IE", "AT", "GR", "PT", "FI"].includes(country)) detectedCurrency = "EUR";
      
      if (detectedCurrency !== "INR" && currencySelector) {
        currencySelector.value = detectedCurrency;
        updatePrices(detectedCurrency);
      }
    })
    .catch(err => console.error("Currency detection failed", err));
});
</script>
"""

if "updatePrices(" not in html:
    html = html.replace('</body>', js_logic + '\n</body>')

with open("pricing/index.html", "w") as f:
    f.write(html)

print("Dynamic pricing script completed!")
