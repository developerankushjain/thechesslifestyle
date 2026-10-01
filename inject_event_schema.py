import json

file_path = 'tournament/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the meta description (remove the trial CTA which doesn't make sense for a tournament page)
bad_desc = "Join the 1st TCL Noida Chess Premier League at Raghav Global School on 31st October 2026. Two categories: Under 12 and Open. Cash prizes, trophies, chess sets and more!. Book your 100% free 45-minute trial today!"
good_desc = "Join the 1st TCL Noida Chess Premier League at Raghav Global School on 31st October 2026. Two categories: Under 12 and Open. Cash prizes, trophies, chess sets and more! Register now."
html = html.replace(bad_desc, good_desc)

# Event Schema
event_schema = {
  "@context": "https://schema.org",
  "@type": "Event",
  "name": "1st TCL Noida Chess Premier League",
  "startDate": "2026-10-31T09:00:00+05:30",
  "endDate": "2026-10-31T18:00:00+05:30",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
  "eventStatus": "https://schema.org/EventScheduled",
  "location": {
    "@type": "Place",
    "name": "Raghav Global School",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "Sector 122",
      "addressLocality": "Noida",
      "addressRegion": "UP",
      "postalCode": "201301",
      "addressCountry": "IN"
    }
  },
  "image": [
    "https://www.thechesslifestyle.com/gallery/20260715_111545.webp"
  ],
  "description": "Join the 1st TCL Noida Chess Premier League at Raghav Global School on 31st October 2026. Two categories: Under 12 and Open.",
  "offers": {
    "@type": "AggregateOffer",
    "lowPrice": "300",
    "highPrice": "500",
    "priceCurrency": "INR",
    "availability": "https://schema.org/InStock",
    "validFrom": "2026-09-01T00:00:00+05:30",
    "url": "https://www.thechesslifestyle.com/tournament/"
  },
  "organizer": {
    "@type": "Organization",
    "name": "TheChessLifestyle",
    "url": "https://www.thechesslifestyle.com"
  }
}

schema_script = f'\n  <script type="application/ld+json">\n  {json.dumps(event_schema, indent=2)}\n  </script>\n'

# Inject Schema before closing head
if '"@type": "Event"' not in html:
    html = html.replace('</head>', schema_script + '</head>')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
