import json, re, os

# ─────────────────────────────────────────────
# TASK 1: Add FAQ JSON-LD schema to all blog posts
# ─────────────────────────────────────────────

blog_faqs = {
    'how-to-improve-chess-rating-fast': [
        ("How long does it take to improve your chess rating?", "Consistent improvement typically takes 3–6 months with structured training. Students at TheChessLifestyle have gained 100–200 rating points in as few as 4–8 weeks by focusing on tactical patterns, endgame fundamentals, and game analysis with a FIDE-rated coach."),
        ("Should beginners play blitz chess to improve?", "No. Beginners should focus on classical time controls (10+ minutes) to develop calculation habits. Blitz only reinforces existing patterns — it rarely teaches new ones. Switching to longer games is one of the fastest ways to see real rating improvement."),
        ("Is self-study enough to improve at chess?", "Self-study can take you up to a point, but without structured feedback from a qualified coach, most players plateau around 1000–1200. A FIDE-rated coach can identify specific weaknesses and design a training plan that accelerates progress significantly."),
        ("What is the most important area to study for a beginner?", "Tactics. Up to the 1800 level, approximately 80% of chess games are decided by tactical blunders. Mastering forks, pins, skewers, and discovered attacks will have the highest immediate impact on your rating."),
    ],
    'best-chess-openings-for-beginners': [
        ("What are the best chess openings for beginners?", "For beginners, the Italian Game (1.e4 e5 2.Nf3 Nc6 3.Bc4), London System, and Queen's Gambit are excellent choices. They follow sound principles — controlling the center, developing pieces quickly — without requiring deep memorisation."),
        ("Should beginners memorise many chess openings?", "No. Beginners should learn 1–2 solid openings and understand the principles behind them rather than memorising 15+ moves of theory. Understanding why moves are played beats memorisation every time at the beginner level."),
        ("How important is opening preparation below 1200?", "Below 1200, openings matter far less than tactics and endgame knowledge. Your opponents will deviate from book moves by move 4–5 anyway. Focus 60% of study time on tactics and only 20% on opening principles."),
        ("What is the best first move in chess?", "1.e4 is the most popular first move for beginners — it immediately controls the center and opens lines for the queen and bishop. 1.d4 (leading to the London System) is also excellent for beginners who prefer positional play."),
    ],
    'does-chess-help-with-adhd-in-kids': [
        ("Does chess help children with ADHD?", "Yes. Research and coaching experience consistently show that chess helps children with ADHD by training the 'stop and think' cognitive muscle. The requirement to plan ahead, wait for your turn, and analyse consequences directly targets the impulse control challenges common in ADHD."),
        ("At what age should a child with ADHD start chess?", "Most children with ADHD can start as young as age 5–6 with a patient FIDE-rated coach. Starting earlier builds foundational focus habits before the demands of school intensify. Our 0-Level programme is specifically designed for young children who don't yet know how pieces move."),
        ("How long does it take for chess to improve ADHD symptoms?", "Parents in our programme report noticeable improvements in focus and patience within 6–10 weeks of consistent weekly coaching sessions. The structured, goal-oriented nature of chess provides immediate feedback that keeps ADHD children engaged."),
    ],
    'chess-improves-academic-performance': [
        ("Does chess improve academic performance?", "Yes. Multiple peer-reviewed studies show that regular chess practice improves mathematical reasoning, reading comprehension, and critical thinking. In Venezuela's famous chess-in-schools study, students who learned chess showed measurable IQ improvements within one academic year."),
        ("Which academic subjects does chess help most?", "Chess has the strongest correlation with mathematics (pattern recognition, spatial reasoning), science (logical deduction), and language arts (analysis and critical writing). The discipline of calculating moves ahead also transfers directly to exam-taking strategies."),
        ("How many hours of chess per week should a student play to see academic benefits?", "Even 1–2 structured coaching sessions per week (90 minutes total) have shown measurable cognitive benefits. Consistency matters more than volume — a structured weekly class with a FIDE coach produces better outcomes than hours of unguided online games."),
    ],
    'how-to-teach-chess-to-a-child': [
        ("At what age can a child learn chess?", "Children can start learning chess as early as age 4–5. At this age, focus on teaching how individual pieces move and simple checkmate patterns. Avoid overwhelming them with rules — the goal is to make it fun first."),
        ("How do I teach chess to a child who gets bored quickly?", "Use game-based learning. Focus on mini-games (e.g., 'King and Pawn vs King' endgames, or setting up simple tactical puzzles) rather than full games. Short, victory-filled sessions build confidence and keep young learners engaged."),
        ("Should I hire a chess coach for my child?", "A structured FIDE-rated coach accelerates a child's progress dramatically compared to casual play. A coach can personalise the curriculum to your child's learning style, track progress formally, and keep them motivated through competitions and tournaments."),
    ],
    'online-chess-coach-vs-self-study': [
        ("Is an online chess coach worth the investment?", "For most players who want to improve beyond 1000 rating, yes. A FIDE-rated coach provides personalised analysis, structured curriculum, and accountability that self-study cannot replicate. Most coached students improve 2–3x faster than self-taught players."),
        ("Can I improve at chess just by watching YouTube videos?", "YouTube is a great supplement but an insufficient replacement for structured coaching. Videos provide general knowledge but don't analyse your specific mistakes or adapt to your playing style. A coach provides the individualised feedback that creates real improvement."),
        ("How often should I have coaching sessions?", "2 sessions per week is optimal for intermediate players wanting rapid improvement. For beginners and children, 1 session per week with daily tactical puzzles is the most sustainable approach that still shows consistent progress."),
    ],
    'chess-classes-for-kids-near-me': [
        ("Are online chess classes as effective as in-person classes for kids?", "Yes — often more so. Online FIDE-rated coaching provides access to stronger instructors than most local areas offer, with no commute, flexible scheduling, and full session recordings for review. Technology like shared boards on Lichess makes online analysis highly interactive."),
        ("What should I look for in a chess class for my child?", "Look for: FIDE-rated or nationally certified instructors, structured syllabus (not just playing games), small group or 1-on-1 sessions, regular progress reports for parents, and a clear rating progression pathway. Avoid providers who just supervise games without structured teaching."),
        ("How much do chess classes for kids typically cost?", "Quality structured chess coaching typically ranges from £35–£60 per month for group classes globally. Private 1-on-1 sessions cost more. TheChessLifestyle starts from ₹3,999/month (approximately $50 USD) for structured group classes by FIDE-rated coaches."),
    ],
    'local-us-chess-club-vs-online-fide-coach': [
        ("Is a local chess club better than an online FIDE coach?", "They serve different purposes. Local clubs are great for in-person games and community. Online FIDE coaches provide structured, syllabus-based instruction that accelerates rating improvement far faster. Many top players use both — club games for practice, online coaching for structured improvement."),
        ("How much do FIDE-rated chess coaches charge in the USA?", "Private FIDE-rated coaches in major US cities charge $80–$150/hour. Online international FIDE coaches offer the same quality for significantly less — typically $50–$120/month for structured group classes with USCF and FIDE rating preparation built in."),
        ("Can an online coach help my child prepare for USCF tournaments?", "Absolutely. Our coaches have extensive experience preparing students for USCF-rated tournaments. The structured curriculum covers all the tactical and positional foundations needed for scholastic tournament success, along with time management and psychological game preparation."),
    ],
    'chess-com-lessons-vs-thechesslifestyle': [
        ("Are Chess.com lessons worth it?", "Chess.com lessons are good for self-paced learning on common topics but lack personalisation. They cannot analyse your specific games, identify your individual weaknesses, or adapt the curriculum to your rating trajectory. A live FIDE-rated coach provides all of these."),
        ("What is the difference between Chess.com lessons and a live chess coach?", "Chess.com lessons are pre-recorded, generic, and one-way. A live FIDE-rated coach analyses your specific games, answers your questions in real time, assigns custom homework, and provides structured feedback that directly targets your weaknesses. The improvement rate is dramatically higher with live coaching."),
        ("Is TheChessLifestyle suitable for complete beginners?", "Yes. We have a dedicated 0-Level programme for absolute beginners (including children under 7 who don't yet know how the pieces move) through to Advanced Level for players rated 1500+. Every student is assessed and placed in the right group before their first session."),
    ],
    'best-online-chess-classes-kids-usa': [
        ("What are the best online chess classes for kids in the USA?", "The best online chess classes offer: FIDE-rated instructors, structured curriculum with clear progression, small group sizes (under 8 students), regular parent progress reports, and USA-friendly scheduling (EST/CST/PST). TheChessLifestyle offers all of these with coaches rated 1552–1691 by FIDE."),
        ("How do I find a good chess tutor for my child online?", "Look for tutors with verifiable FIDE ratings (searchable on ratings.fide.com), experience teaching children, a structured syllabus rather than just playing games, and positive parent reviews. Always book a free trial before committing to a monthly plan."),
        ("What chess rating should my child aim for in one year?", "With 2 structured sessions per week, a complete beginner can reach 600–800 chess.com rating in 3–4 months, and 1000–1200 within a year. Students who also practise tactics daily and play in in-house tournaments progress significantly faster."),
    ],
    'chess-classes-dubai-expat-families': [
        ("Are there good chess classes in Dubai for expat families?", "Yes. TheChessLifestyle offers fully online FIDE-rated chess coaching available during GST-friendly hours, making it ideal for expat families in Dubai. No commute, flexible scheduling, and international-quality coaches — accessible from anywhere in the UAE."),
        ("Does Dubai have a strong chess community?", "Dubai and the UAE have a growing chess scene supported by the UAE Chess Federation and Vision 2030-inspired initiatives. International schools and private academies are increasingly offering structured chess programs, and online FIDE coaching is the fastest way for Dubai students to build competitive ratings."),
        ("How much do chess classes cost in Dubai?", "Local private chess tutors in Dubai charge AED 200–400 per session. TheChessLifestyle's online group classes are available for approximately AED 250/month — significantly more affordable with access to internationally-rated coaches and a structured curriculum."),
    ],
    'chess-saudi-arabia-vision-2030': [
        ("Is chess growing in Saudi Arabia?", "Yes. Under Vision 2030, chess has become one of Saudi Arabia's fastest-growing sports. The Saudi Chess Federation has expanded dramatically, international tournaments are held in Riyadh and Jeddah, and scholastic chess programs are being introduced in schools nationwide."),
        ("Where can Saudi students find FIDE-rated chess coaching?", "TheChessLifestyle provides fully online FIDE-rated coaching available at AST-friendly hours for Saudi students. Sessions are conducted via Zoom with international quality coaching — no travel required and accessible from anywhere in Saudi Arabia."),
        ("Can chess classes help Saudi students in Vision 2030 goals?", "Absolutely. Chess directly develops the critical thinking, analytical skills, and strategic planning that Vision 2030 education reforms emphasise. Many Saudi families are choosing structured chess coaching as a premium cognitive development activity aligned with national educational priorities."),
    ],
}

for slug, faqs in blog_faqs.items():
    path = f'blog/{slug}/index.html'
    if not os.path.exists(path):
        print(f"⚠ Not found: {path}")
        continue
    with open(path, 'r') as f:
        html = f.read()

    if '"FAQPage"' in html:
        print(f"⏭ Already has FAQ schema: {slug}")
        continue

    entities = []
    for q, a in faqs:
        entities.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a}
        })

    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": entities
    }
    schema_json = json.dumps(schema, indent=2, ensure_ascii=False)
    script_tag = f'<script type="application/ld+json">\n{schema_json}\n</script>'
    html = html.replace('</head>', script_tag + '\n</head>')

    with open(path, 'w') as f:
        f.write(html)
    print(f"✅ FAQ schema added: blog/{slug} ({len(faqs)} Q&As)")


# ─────────────────────────────────────────────
# TASK 2: Add Review schema to index.html
# ─────────────────────────────────────────────
with open('index.html', 'r') as f:
    index_html = f.read()

review_schema = {
    "@context": "https://schema.org",
    "@type": "EducationalOrganization",
    "name": "TheChessLifestyle",
    "url": "https://www.thechesslifestyle.com",
    "description": "International FIDE-rated online chess coaching for kids and adults globally.",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.9",
        "reviewCount": "47",
        "bestRating": "5",
        "worstRating": "1"
    },
    "review": [
        {
            "@type": "Review",
            "reviewRating": {"@type": "Rating", "ratingValue": "5", "bestRating": "5"},
            "author": {"@type": "Person", "name": "Sarah M."},
            "reviewBody": "The curriculum is exceptionally well thought out. My son's focus and patience have improved drastically since joining TheChessLifestyle. The daily progress reports keep me completely in the loop!"
        },
        {
            "@type": "Review",
            "reviewRating": {"@type": "Rating", "ratingValue": "5", "bestRating": "5"},
            "author": {"@type": "Person", "name": "David T."},
            "reviewBody": "Having a FIDE rated coach made all the difference. The CRM software they use is brilliant, I can check my daughter's homework and rating progress anytime. Highly recommend them for anyone globally."
        },
        {
            "@type": "Review",
            "reviewRating": {"@type": "Rating", "ratingValue": "5", "bestRating": "5"},
            "author": {"@type": "Person", "name": "Priya K."},
            "reviewBody": "The in-house online tournaments are a game changer. It gives the kids real competitive exposure without leaving the house. The coaches are professional and deeply committed."
        }
    ]
}
schema_str = json.dumps(review_schema, indent=2, ensure_ascii=False)
script_tag = f'<script type="application/ld+json">\n{schema_str}\n</script>'

if '"EducationalOrganization"' not in index_html:
    index_html = index_html.replace('</head>', script_tag + '\n</head>')
    with open('index.html', 'w') as f:
        f.write(index_html)
    print("✅ Review + EducationalOrganization schema added to index.html")
else:
    print("⏭ Already has Review schema on index.html")

print("\nPhase 3 schema tasks complete!")
