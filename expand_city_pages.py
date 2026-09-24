import re, os

# Data for each thin city page
city_data = {
    'online-chess-classes-london': {
        'city': 'London', 'country': 'UK', 'timezone': 'GMT', 'currency': '£',
        'price': '35', 'org': 'ECF (English Chess Federation)',
        'context': 'London is one of the world\'s top chess cities, home to some of England\'s strongest clubs like the London Chess Classic venue. From Battersea to Hackney, families across the boroughs are discovering the cognitive benefits of structured chess training.',
        'benefit': 'ECF rating improvement and FIDE tournament preparation',
        'link1': '/online-chess-classes-uk/', 'link1_text': 'online chess classes in UK',
    },
    'online-chess-classes-dubai': {
        'city': 'Dubai', 'country': 'UAE', 'timezone': 'GST (UTC+4)', 'currency': 'AED',
        'price': '250', 'org': 'UAE Chess Federation',
        'context': 'Dubai\'s chess scene is booming under Vision 2030-inspired initiatives across the Gulf. Expat families and Emirati students alike are seeking structured coaching that goes far beyond what school clubs can offer.',
        'benefit': 'FIDE rating development and structured tournament preparation',
        'link1': '/online-chess-classes-uae/', 'link1_text': 'online chess classes in UAE',
    },
    'online-chess-classes-toronto': {
        'city': 'Toronto', 'country': 'Canada', 'timezone': 'EST', 'currency': 'CAD',
        'price': '85', 'org': 'Chess Federation of Canada',
        'context': 'Toronto is Canada\'s most diverse city and has a thriving chess community across its neighbourhoods. CFC-rated students from Scarborough to Mississauga are turning to structured online coaching as an alternative to expensive local programs.',
        'benefit': 'CFC rating growth and FIDE tournament pathway',
        'link1': '/online-chess-classes-canada/', 'link1_text': 'online chess classes in Canada',
    },
    'online-chess-classes-sydney': {
        'city': 'Sydney', 'country': 'Australia', 'timezone': 'AEDT', 'currency': 'AUD',
        'price': '80', 'org': 'Australian Chess Federation',
        'context': 'Sydney\'s families are increasingly turning to online chess coaching as a premium after-school enrichment activity. With ACF scholastic tournaments growing every year, structured FIDE-quality coaching is the fastest way to competitive improvement.',
        'benefit': 'ACF rating improvement and national tournament preparation',
        'link1': '/online-chess-classes-australia/', 'link1_text': 'online chess classes in Australia',
    },
    'online-chess-classes-riyadh': {
        'city': 'Riyadh', 'country': 'Saudi Arabia', 'timezone': 'AST (UTC+3)', 'currency': 'SAR',
        'price': '230', 'org': 'Saudi Chess Federation',
        'context': 'Under Vision 2030, chess has become one of Saudi Arabia\'s fastest growing mental sports. Riyadh families are investing in structured chess education as part of cognitive development programs for their children.',
        'benefit': 'FIDE rating development in the rapidly growing Saudi chess ecosystem',
        'link1': '/online-chess-classes-saudi-arabia/', 'link1_text': 'online chess classes in Saudi Arabia',
    },
    'online-chess-classes-abu-dhabi': {
        'city': 'Abu Dhabi', 'country': 'UAE', 'timezone': 'GST (UTC+4)', 'currency': 'AED',
        'price': '250', 'org': 'UAE Chess Federation',
        'context': 'Abu Dhabi is home to some of the Gulf\'s most active chess federations and tournaments. Emirati and expat families are increasingly seeking FIDE-quality online coaching that fits around school schedules.',
        'benefit': 'FIDE tournament readiness and rating progression',
        'link1': '/online-chess-classes-uae/', 'link1_text': 'online chess classes in UAE',
    },
}

deep_content_template = """
    <!-- Deep Content Section -->
    <section class="section-alt scroll-reveal" style="padding: 5rem 5%;">
      <div style="max-width: 900px; margin: 0 auto;">

        <h2>Why {city} Families Are Choosing <span class="highlight">Online FIDE Coaching</span></h2>
        <p style="font-size: 1.05rem; color: var(--text-muted); margin-bottom: 2rem;">{context}</p>

        <h2>What Our Curriculum Covers for <span class="highlight">{city} Students</span></h2>
        <p>Our structured programme is built around your child's current chess.com or {org} rating and scales progressively. Unlike generic platforms, every student gets a personalised journey:</p>
        <ul style="padding-left: 1.5rem; color: var(--text-main); line-height: 2; margin: 1.5rem 0;">
          <li><strong>Foundational (0–800 rating):</strong> Piece movement mastery, basic tactics, checkmate patterns, and first opening principles.</li>
          <li><strong>Beginner (800–1200):</strong> Modern openings, fork/pin/skewer tactics, pawn structures, and endgame fundamentals.</li>
          <li><strong>Intermediate (1200–1500):</strong> Positional play, long-term planning, opening repertoire building, and psychological game management.</li>
          <li><strong>Advanced (1500–1800+):</strong> Deep game analysis, novelty creation, dynamic vs static advantages, and tournament preparation.</li>
        </ul>

        <h2>How Classes Work for <span class="highlight">{city} Timezone</span></h2>
        <p>All classes are conducted live via Zoom, fully optimised for students in <strong>{timezone}</strong>. Our scheduling system lets you pick from morning, after-school, or weekend slots — so your child never misses a session due to school commitments.</p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.5rem; margin: 2.5rem 0;">
          <div style="background: var(--bg-card); border: 1px solid var(--border-light); border-radius: 12px; padding: 1.5rem; text-align: center;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">🕐</div>
            <strong>45-Minute Sessions</strong>
            <p style="color: var(--text-muted); font-size: 0.9rem; margin: 0.5rem 0 0;">Optimal for deep focus — not too short, not tiring</p>
          </div>
          <div style="background: var(--bg-card); border: 1px solid var(--border-light); border-radius: 12px; padding: 1.5rem; text-align: center;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">📊</div>
            <strong>Monthly Progress Reports</strong>
            <p style="color: var(--text-muted); font-size: 0.9rem; margin: 0.5rem 0 0;">Detailed analysis sent directly to parents</p>
          </div>
          <div style="background: var(--bg-card); border: 1px solid var(--border-light); border-radius: 12px; padding: 1.5rem; text-align: center;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">🏆</div>
            <strong>In-House Tournaments</strong>
            <p style="color: var(--text-muted); font-size: 0.9rem; margin: 0.5rem 0 0;">Real competitive experience in a safe online environment</p>
          </div>
        </div>

        <h2>Pricing for <span class="highlight">{city} Students</span></h2>
        <p>Group classes start from approximately <strong>{currency}{price}/month</strong> for {city} students. We offer quarterly, half-yearly, and annual payment plans with discounts up to 20%. Every new student gets a <strong>FREE 45-minute trial class</strong> — no credit card required.</p>
        <p>👉 See full <a href="/pricing/" style="color: var(--primary); font-weight: 600;">pricing and plan details</a> including the referral programme and registration fee structure.</p>

        <h2>Frequently Asked Questions — <span class="highlight">Chess Classes in {city}</span></h2>
        <div style="margin-top: 1.5rem;">
          <details style="border: 1px solid var(--border-light); border-radius: 8px; padding: 1rem; margin-bottom: 1rem; background: var(--bg-card);">
            <summary style="font-weight: 600; cursor: pointer; color: var(--text-main);">Are the coaches really FIDE rated?</summary>
            <p style="margin-top: 0.8rem; color: var(--text-muted);">Yes. All TheChessLifestyle coaches are internationally rated by FIDE — you can verify each coach's profile directly on the official FIDE website. Our head coach Chirag Soni holds FIDE ID 25971115.</p>
          </details>
          <details style="border: 1px solid var(--border-light); border-radius: 8px; padding: 1rem; margin-bottom: 1rem; background: var(--bg-card);">
            <summary style="font-weight: 600; cursor: pointer; color: var(--text-main);">What age groups do you teach in {city}?</summary>
            <p style="margin-top: 0.8rem; color: var(--text-muted);">We teach students from age 5 upwards. We have a dedicated 0-Level programme for children under 7 who don't yet know how the pieces move, right through to advanced programmes for adult competitive players.</p>
          </details>
          <details style="border: 1px solid var(--border-light); border-radius: 8px; padding: 1rem; margin-bottom: 1rem; background: var(--bg-card);">
            <summary style="font-weight: 600; cursor: pointer; color: var(--text-main);">How is this better than a local {city} chess club?</summary>
            <p style="margin-top: 0.8rem; color: var(--text-muted);">Local clubs are great for practice games but rarely offer structured, syllabus-based coaching by FIDE-rated instructors. Our online model gives you access to international-quality coaching at a fraction of the local private tutor cost — without the commute.</p>
          </details>
          <details style="border: 1px solid var(--border-light); border-radius: 8px; padding: 1rem; background: var(--bg-card);">
            <summary style="font-weight: 600; cursor: pointer; color: var(--text-main);">What platform do you use for classes?</summary>
            <p style="margin-top: 0.8rem; color: var(--text-muted);">All live sessions are conducted on Zoom. We also use Lichess for game analysis and a custom CRM for tracking homework, progress, and parent communication — accessible from any device.</p>
          </details>
        </div>

        <p style="margin-top: 2rem; color: var(--text-muted); font-size: 0.9rem;">
          Also explore: <a href="{link1}" style="color: var(--primary); font-weight: 600;">{link1_text}</a> · <a href="/pricing/" style="color: var(--primary); font-weight: 600;">View full pricing</a> · <a href="/blog/" style="color: var(--primary); font-weight: 600;">Read our chess blog</a>
        </p>
      </div>
    </section>"""

# FAQ JSON-LD schema for each city page
faq_schema_template = """  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {{"@type": "Question", "name": "Are the coaches really FIDE rated?", "acceptedAnswer": {{"@type": "Answer", "text": "Yes. All TheChessLifestyle coaches hold official FIDE ratings verifiable at ratings.fide.com. Our head coach Chirag Soni holds FIDE ID 25971115."}}}},
      {{"@type": "Question", "name": "What age groups do you teach in {city}?", "acceptedAnswer": {{"@type": "Answer", "text": "We teach students from age 5 upwards, from complete beginners to competitive players above 1800 rating."}}}},
      {{"@type": "Question", "name": "How is this better than a local {city} chess club?", "acceptedAnswer": {{"@type": "Answer", "text": "Online FIDE-rated coaching offers structured, syllabus-based learning at a fraction of local private tutor costs, with no commute required."}}}},
      {{"@type": "Question", "name": "What platform do you use for classes?", "acceptedAnswer": {{"@type": "Answer", "text": "All live sessions are conducted on Zoom, with Lichess for game analysis and a custom CRM for progress tracking."}}}}
    ]
  }}
  </script>"""

for slug, data in city_data.items():
    path = f'{slug}/index.html'
    if not os.path.exists(path):
        continue
    with open(path, 'r') as f:
        html = f.read()

    # Inject deep content before the enrol section
    deep_html = deep_content_template.format(**data)
    html = html.replace('    <section id="enrol"', deep_html + '\n\n    <section id="enrol"')

    # Inject FAQ schema before </head>
    faq_schema = faq_schema_template.format(city=data['city'])
    html = html.replace('</head>', faq_schema + '\n</head>')

    with open(path, 'w') as f:
        f.write(html)

    words = len(re.sub('<[^>]+>', '', html).split())
    print(f"✅ {slug}: now ~{words} words")

print("\nCity page expansion complete!")
