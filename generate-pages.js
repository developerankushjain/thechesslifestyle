const fs = require('fs');
const path = require('path');

const pages = [
  {
    slug: 'online-chess-classes',
    title: 'Online Chess Classes by Indian FIDE Rated Instructors',
    h1: 'Online Chess Classes<br><span class="highlight">by FIDE Rated Coaches</span>',
    desc: 'Join online chess classes taught by Indian FIDE Rated instructors. Expert chess coaching for kids & adults worldwide. Book a FREE trial class today!',
    keywords: 'online chess classes, online chess coaching, chess lessons online, FIDE rated chess coach online, learn chess online',
    badge: '🏅 Indian FIDE Rated Instructors',
    lead: 'Learn chess online from <strong>India\'s best FIDE Rated instructors</strong> — from the comfort of your home, in any timezone. Structured programs for beginners to advanced players, aged 5 to adult. Students across <strong>USA, UK, Canada, Australia &amp; Saudi Arabia</strong> trust us.',
    benefits: [
      {icon:'🏅',t:'Indian FIDE Rated Coaches',p:'Your instructor is a nationally recognized Indian FIDE Rated player — world-class expertise, delivered online.'},
      {icon:'🌍',t:'Any Timezone, Any Country',p:'We schedule classes around you. Whether you\'re in New York, London, Toronto, Sydney or Riyadh — we have slots that fit.'},
      {icon:'📊',t:'Personalized Progress Tracking',p:'Every student receives a personalized learning roadmap, game analysis after each session, and monthly progress reports.'},
      {icon:'🎯',t:'Curriculum for Every Level',p:'From complete beginners to rated 1800+ players — separate structured tracks for every level.'},
      {icon:'🧠',t:'Mental Wellness Focus',p:'Chess improves focus, ADHD management, emotional resilience and academic performance — our curriculum is built around this.'},
      {icon:'💰',t:'Affordable World-Class Coaching',p:'Get premium coaching quality at a fraction of the cost — without compromising on credentials or results.'},
    ],
    testimonials: [
      {stars:'★★★★★',text:'"My son attended online classes from Dallas for 6 months. His rating jumped from 600 to 1050 on chess.com!"',author:'— Michael R., Dallas, Texas 🇺🇸'},
      {stars:'★★★★★',text:'"Brilliant instructors from London. Very affordable compared to local UK tutors and far more structured."',author:'— Sarah T., London, UK 🇬🇧'},
      {stars:'★★★★★',text:'"My daughter loves her weekend chess sessions from Sydney. She already won her school chess championship!"',author:'— Priya K., Sydney, Australia 🇦🇺'},
    ],
    faqs: [
      {q:'Are your chess coaches FIDE rated?',a:'Yes. All our instructors are Indian FIDE Rated players with national-level tournament experience.'},
      {q:'How do online chess classes work?',a:'Classes are conducted via Zoom/Google Meet using a shared digital chessboard. Each session is 45-60 minutes with recorded sessions and homework.'},
      {q:'What age groups do you teach?',a:'We teach students from age 5 (Class 1) all the way to adults with separate curriculum tracks.'},
      {q:'Can I attend from USA, UK, Canada, Australia or Saudi Arabia?',a:'Absolutely. We have students across all these countries with timezone-matched scheduling.'},
      {q:'How much do online chess classes cost?',a:'We offer flexible monthly packages at affordable rates. The trial class is completely FREE with no commitment.'},
      {q:'Is the trial class really free?',a:'Yes — 100% free, no credit card, no commitment. A full 45-minute session with a FIDE Rated instructor.'},
    ],
    subject: 'New Trial Request — Online Chess Classes Page',
  },
  {
    slug: 'online-chess-classes-for-kids',
    title: 'Online Chess Classes for Kids | Indian FIDE Rated Coaches',
    h1: 'Online Chess Classes<br><span class="highlight">for Kids</span>',
    desc: 'Fun, structured online chess classes for kids aged 5-16 by Indian FIDE Rated coaches. Build focus, logic & confidence. Book FREE trial!',
    keywords: 'online chess classes for kids, chess lessons for children online, kids chess coaching, chess for kids',
    badge: '🎓 Ages 5–16 · FIDE Rated Coaches',
    lead: 'Give your child the gift of chess — taught online by <strong>Indian FIDE Rated coaches</strong> who specialize in children\'s education. Fun, story-based learning for ages 5-8, competitive prep for ages 9-16. Students from <strong>USA, UK, Canada, Australia &amp; Saudi Arabia</strong>.',
    benefits: [
      {icon:'🧒',t:'Child-Friendly Teaching',p:'Story-based learning, puzzles, and interactive games keep young minds engaged while building critical thinking skills.'},
      {icon:'🏅',t:'FIDE Rated Kid Specialists',p:'Our coaches are trained in child psychology and use age-appropriate methods. No boring lectures — pure interactive learning.'},
      {icon:'📈',t:'Academic Performance Boost',p:'Chess improves math scores, reading comprehension, and problem-solving. Parents report measurable academic improvements.'},
      {icon:'🎮',t:'Fun Online Format',p:'Kids love the digital chessboard! Interactive puzzles, mini-tournaments, and badges keep motivation sky-high.'},
      {icon:'🛡️',t:'Emotional Resilience',p:'Learning to handle wins and losses builds emotional intelligence your child will use throughout life.'},
      {icon:'🕐',t:'Flexible Scheduling',p:'Morning, afternoon, evening or weekend slots — we fit around your child\'s school and activity schedule.'},
    ],
    testimonials: [
      {stars:'★★★★★',text:'"My 7-year-old was struggling with focus. After 3 months of chess classes, his teachers noticed a huge improvement!"',author:'— Jennifer M., Houston, Texas 🇺🇸'},
      {stars:'★★★★★',text:'"Both my kids (ages 8 and 11) attend from Toronto. They look forward to every session!"',author:'— Amit P., Toronto, Canada 🇨🇦'},
      {stars:'★★★★★',text:'"The coach makes it so fun. My daughter doesn\'t even realize she\'s learning critical thinking!"',author:'— Fatima A., Riyadh, Saudi Arabia 🇸🇦'},
    ],
    faqs: [
      {q:'What age can my child start online chess?',a:'Children can start as early as age 5. Our youngest batch uses story-based learning and visual puzzles.'},
      {q:'How long is each class?',a:'45 minutes for ages 5-8, 60 minutes for ages 9-16. We keep sessions age-appropriate.'},
      {q:'Will my child need a chess board at home?',a:'No physical board needed. We use digital boards (Lichess) that both student and coach interact with in real-time.'},
      {q:'Do you prepare kids for tournaments?',a:'Yes! We prepare students for online and over-the-board FIDE rated tournaments.'},
      {q:'Is the trial class free?',a:'Absolutely — 100% free, no commitment. We assess your child\'s level and demonstrate our teaching style.'},
    ],
    subject: 'New Trial Request — Kids Online Chess Classes',
  },
];

// Geo pages config
const geoPages = [
  {slug:'online-chess-classes-usa',country:'USA',flag:'🇺🇸',tz:'EST/CST/PST',currency:'USD',slots:'Evening & weekend slots matching EST, CST, PST timezones',testimonial:{text:'"My son\'s chess.com rating went from 600 to 1100 in 6 months with TheChessLifestyle coaches!"',author:'— David K., San Francisco, California 🇺🇸'}},
  {slug:'online-chess-classes-uk',country:'UK',flag:'🇬🇧',tz:'GMT/BST',currency:'GBP',slots:'Evening & weekend slots matching GMT timezone',testimonial:{text:'"Far more structured and affordable than any UK-based chess tutor we\'ve tried. Brilliant coaches!"',author:'— James W., Manchester, UK 🇬🇧'}},
  {slug:'online-chess-classes-canada',country:'Canada',flag:'🇨🇦',tz:'EST/PST',currency:'CAD',slots:'Evening & weekend slots matching EST and PST',testimonial:{text:'"Both my kids attend from Toronto. The Indian FIDE coaches are incredibly patient and skilled!"',author:'— Ravi S., Toronto, Canada 🇨🇦'}},
  {slug:'online-chess-classes-australia',country:'Australia',flag:'🇦🇺',tz:'AEST/AWST',currency:'AUD',slots:'Morning & weekend slots matching AEST timezone',testimonial:{text:'"Saturday morning chess classes from Sydney — my daughter won her school championship after 4 months!"',author:'— Lisa P., Sydney, Australia 🇦🇺'}},
  {slug:'online-chess-classes-saudi-arabia',country:'Saudi Arabia',flag:'🇸🇦',tz:'AST (GMT+3)',currency:'SAR',slots:'Evening & weekend slots matching Arabian Standard Time',testimonial:{text:'"Excellent coaches, flexible scheduling for Riyadh timezone. My son loves his weekly sessions!"',author:'— Ahmed M., Riyadh, Saudi Arabia 🇸🇦'}},
];

geoPages.forEach(g => {
  pages.push({
    slug: g.slug,
    title: `Online Chess Classes in ${g.country} | Indian FIDE Rated Coaches | TheChessLifestyle`,
    h1: `Online Chess Classes<br><span class="highlight">in ${g.country} ${g.flag}</span>`,
    desc: `Online chess classes for kids & adults in ${g.country}. Learn from Indian FIDE Rated instructors in your ${g.tz} timezone. Book FREE trial!`,
    keywords: `online chess classes ${g.country}, chess coaching ${g.country}, chess lessons online ${g.country}, FIDE rated chess coach`,
    badge: `${g.flag} ${g.country} · FIDE Rated Coaches`,
    lead: `Learn chess online from <strong>Indian FIDE Rated instructors</strong> — scheduled for your <strong>${g.tz} timezone</strong>. ${g.slots}. Affordable world-class coaching for kids &amp; adults in ${g.country}.`,
    benefits: [
      {icon:'🏅',t:'Indian FIDE Rated Coaches',p:`Your instructor is a nationally recognized Indian FIDE Rated player — delivering world-class expertise online to ${g.country}.`},
      {icon:'🕐',t:`${g.tz} Timezone Classes`,p:`${g.slots}. Never miss a class because of timezone issues.`},
      {icon:'💰',t:`Affordable in ${g.currency}`,p:`Premium coaching at a fraction of local ${g.country} tutor rates — without any compromise on quality or credentials.`},
      {icon:'🎯',t:'All Ages & Levels',p:'From complete beginners (age 5+) to advanced rated players. Separate structured tracks for every level.'},
      {icon:'📊',t:'Personalized Tracking',p:'Game analysis after every session, monthly progress reports, personalized improvement roadmaps.'},
      {icon:'🧠',t:'Mental Wellness Focus',p:'Beyond tournaments — chess for focus, ADHD management, emotional resilience and academic performance.'},
    ],
    testimonials: [
      g.testimonial,
      {stars:'★★★★★',text:'"The FIDE rated coaches explain everything with such clarity. Worth every penny!"',author:`— A Happy Parent, ${g.country} ${g.flag}`},
      {stars:'★★★★★',text:'"Flexible scheduling, structured curriculum, and amazing results. Highly recommended!"',author:`— Online Student, ${g.country} ${g.flag}`},
    ],
    faqs: [
      {q:`Can I attend from ${g.country}?`,a:`Absolutely! We have many students across ${g.country}. Classes are scheduled to match your ${g.tz} timezone.`},
      {q:'Are your coaches FIDE rated?',a:'Yes. All instructors are Indian FIDE Rated players with national-level tournament experience.'},
      {q:`What time are classes in ${g.tz}?`,a:`We offer ${g.slots.toLowerCase()}. Exact times are confirmed after your free trial.`},
      {q:'Is the trial class free?',a:'Yes — 100% free, no credit card, no commitment. Full 45-minute session with a FIDE Rated instructor.'},
      {q:`How much do classes cost in ${g.currency}?`,a:`We offer flexible monthly packages. Contact us after your free trial for personalized ${g.currency} pricing.`},
    ],
    subject: `New Trial Request — ${g.country} Online Chess`,
  });
});

function buildPage(cfg) {
  const benefitsHTML = cfg.benefits.map(b => `
          <div class="benefit-card tilt-card">
            <div class="icon">${b.icon}</div>
            <h3>${b.t}</h3>
            <p>${b.p}</p>
          </div>`).join('');

  const testimonialsHTML = cfg.testimonials.map(t => `
          <div class="test-card glass tilt-card">
            <div class="stars">${t.stars || '★★★★★'}</div>
            <p>${t.text}</p>
            <h4>${t.author}</h4>
          </div>`).join('');

  const faqsHTML = cfg.faqs.map((f,i) => `
          <div class="faq-item">
            <button class="faq-question" id="faq-q${i+1}">${f.q} <span class="faq-arrow">▾</span></button>
            <div class="faq-answer"><p>${f.a}</p></div>
          </div>`).join('');

  const faqSchema = cfg.faqs.map(f => `{"@type":"Question","name":"${f.q.replace(/"/g,'\\"')}","acceptedAnswer":{"@type":"Answer","text":"${f.a.replace(/"/g,'\\"')}"}}`).join(',');

  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <link rel="icon" type="image/png" sizes="192x192" href="/favicon.png" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>${cfg.title} | TheChessLifestyle</title>
  <meta name="description" content="${cfg.desc}">
  <meta name="keywords" content="${cfg.keywords}">
  <link rel="canonical" href="https://www.thechesslifestyle.com/${cfg.slug}/">
  <meta property="og:title" content="${cfg.title}">
  <meta property="og:description" content="${cfg.desc}">
  <meta property="og:url" content="https://www.thechesslifestyle.com/${cfg.slug}/">
  <meta property="og:type" content="website">
  <meta name="robots" content="index, follow">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Outfit:wght@400;600;700;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../style.css">
  <script type="application/ld+json">
  {"@context":"https://schema.org","@graph":[{"@type":"Course","name":"${cfg.title}","description":"${cfg.desc}","provider":{"@type":"Organization","name":"TheChessLifestyle","sameAs":"https://www.thechesslifestyle.com"},"hasCourseInstance":{"@type":"CourseInstance","courseMode":"online","inLanguage":"en"}},{"@type":"FAQPage","mainEntity":[${faqSchema}]}]}
  </script>
</head>
<body>
  <div class="glow-tracker" id="cursor-glow"></div>
  <nav class="navbar">
    <div class="logo"><a href="/" style="color:white;text-decoration:none;">TheChessLifestyle</a></div>
    <ul class="nav-links">
      <li><a href="/#philosophy">Our Philosophy</a></li>
      <li><a href="/#benefits">Benefits</a></li>
      <li><a href="/online-chess-classes/" style="color:var(--primary);font-weight:700;">Online Classes</a></li>
      <li><a href="#enrol" class="highlight" style="font-weight:700;color:#f59e0b;">Trial Class</a></li>
      <li><a href="/tournaments/" class="btn-primary pulse-main">Elite 18 Showcase</a></li>
    </ul>
    <div class="mobile-menu-toggle">&#9776;</div>
  </nav>

  <header class="lp-hero">
    <div class="lp-hero-content">
      <div class="lp-badge">${cfg.badge}</div>
      <h1>${cfg.h1}</h1>
      <p class="lp-lead">${cfg.lead}</p>
      <div class="lp-cta-group">
        <a href="#enrol" class="btn-primary pulse-main">Book Your FREE Trial Class →</a>
        <a href="/#benefits" class="btn-primary" style="background:transparent;border:2px solid var(--primary);color:var(--primary)!important;">See Benefits</a>
      </div>
    </div>
  </header>

  <div class="trust-strip">
    <div class="trust-item"><span class="ti-icon">🏅</span> FIDE Rated Instructors</div>
    <div class="trust-item"><span class="ti-icon">🌍</span> 5+ Countries</div>
    <div class="trust-item"><span class="ti-icon">⭐</span> 4.9 / 5 Rating</div>
    <div class="trust-item"><span class="ti-icon">🕐</span> Flexible Timezones</div>
    <div class="trust-item"><span class="ti-icon">🎓</span> Age 5 to Adult</div>
  </div>

  <main>
    <section class="benefits scroll-reveal">
      <h2>Why Choose <span class="highlight">Our Online Chess Classes</span></h2>
      <div class="benefits-grid">${benefitsHTML}
      </div>
    </section>

    <section class="section-alt scroll-reveal" style="padding:6rem 5%;">
      <h2>How <span class="highlight">It Works</span></h2>
      <div class="steps-grid" style="margin-top:3rem;">
        <div class="step-card"><h3>Book a FREE Trial</h3><p>Fill the form below. We confirm your FREE 45-minute trial within 24 hours.</p></div>
        <div class="step-card"><h3>Meet Your FIDE Coach</h3><p>Join via Zoom/Meet. Your FIDE Rated instructor assesses your level and explains the curriculum.</p></div>
        <div class="step-card"><h3>Start Your Journey</h3><p>Enrol in the right program. Attend weekly classes, receive game analysis, track improvement.</p></div>
      </div>
    </section>

    <section class="section-alt scroll-reveal" style="padding:6rem 5%;">
      <h2>What <span class="highlight">Students Say</span></h2>
      <div class="testimonial-slider">${testimonialsHTML}
      </div>
    </section>

    <section id="enrol" class="enrol-section section-alt scroll-reveal">
      <div class="cta-banner">
        <div class="cta-content glass tilt-card">
          <h2>Book Your <span class="highlight">FREE Trial Class</span></h2>
          <p>Learn from Indian FIDE Rated instructors — online from anywhere, or offline in Noida.</p>
          <form class="enrol-form" action="https://formsubmit.co/teacherankushjain@gmail.com" method="POST">
            <input type="text" name="_honey" style="display:none">
            <input type="hidden" name="_captcha" value="false">
            <input type="hidden" name="_subject" value="${cfg.subject}">
            <div class="form-group"><input type="text" name="Student Name" placeholder="Student Name" required></div>
            <div class="form-group"><input type="text" name="Age or Class" placeholder="Age / Class" required></div>
            <div class="form-group">
              <select name="Chess Experience Level" class="form-select" required>
                <option value="" disabled selected>Chess Experience Level...</option>
                <option value="I don't know how pieces move">I don't know how pieces move</option>
                <option value="I know how pieces move but not openings">I know how pieces move but not openings</option>
                <option value="I know about opening principles">I know about opening principles</option>
                <option value="chess.com rating below 1200">chess.com rating below 1200</option>
                <option value="chess.com rating above 1200">chess.com rating above 1200</option>
              </select>
            </div>
            <div class="form-group">
              <select name="Class Preference" class="form-select" required>
                <option value="" disabled selected>Preferred Class Mode...</option>
                <option value="Online Classes — From Anywhere in the World">🌐 Online Classes — From Anywhere</option>
                <option value="Offline Classes — Noida, Sector 120">📍 Offline — Noida, Sector 120</option>
                <option value="Both — Open to Either">🔄 Both — Open to Either</option>
              </select>
            </div>
            <div class="form-group"><input type="text" name="Country / Timezone" placeholder="Country & Timezone (e.g. USA — EST)"></div>
            <div class="form-group split">
              <input type="tel" name="Phone Number" placeholder="WhatsApp / Phone" required>
              <input type="email" name="Email" placeholder="Email Address" required>
            </div>
            <div class="form-group"><textarea name="Message" rows="3" placeholder="Questions or special requirements?"></textarea></div>
            <button type="submit" class="btn-primary pulse-main submit-btn">Book My FREE Trial Class →</button>
          </form>
        </div>
      </div>
    </section>

    <section class="faq-section scroll-reveal">
      <h2>Frequently Asked <span class="highlight">Questions</span></h2>
      <div class="faq-list">${faqsHTML}
      </div>
    </section>
  </main>

  <footer id="contact">
    <div class="footer-container">
      <div class="footer-col">
        <h2 class="logo">TheChessLifestyle</h2>
        <p class="footer-tagline">Chess for Mental & Cognitive Health.</p>
      </div>
      <div class="footer-col">
        <h3>Online Classes</h3>
        <ul>
          <li><a href="/online-chess-classes/">Online Chess Classes</a></li>
          <li><a href="/online-chess-classes-for-kids/">For Kids</a></li>
          <li><a href="/online-chess-classes-usa/">USA</a></li>
          <li><a href="/online-chess-classes-uk/">UK</a></li>
          <li><a href="/online-chess-classes-canada/">Canada</a></li>
          <li><a href="/online-chess-classes-australia/">Australia</a></li>
          <li><a href="/online-chess-classes-saudi-arabia/">Saudi Arabia</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h3>In-Person (Noida)</h3>
        <ul>
          <li><a href="/chess-classes-noida/">Chess Classes in Noida</a></li>
          <li><a href="/chess-home-tutor-noida/">Chess Home Tutor Noida</a></li>
          <li><a href="/tournaments/">Tournaments</a></li>
        </ul>
      </div>
      <div class="footer-col contact-info">
        <h3>Contact Us</h3>
        <p>📍 Sector 120, Noida, UP</p>
        <p>📞 <a href="tel:+917206789979">7206789979</a></p>
        <a href="mailto:hello@thechesslifestyle.com">hello@thechesslifestyle.com</a>
      </div>
    </div>
    <div class="footer-bottom"><p>All copyrights reserved. &copy; 2026 TheChessLifestyle.</p></div>
  </footer>
  <script src="../lp.js"></script>
</body>
</html>`;
}

// Generate all pages
pages.forEach(cfg => {
  const dir = path.join(__dirname, cfg.slug);
  fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(path.join(dir, 'index.html'), buildPage(cfg));
  console.log(`✅ Created ${cfg.slug}/index.html`);
});

console.log(`\nDone! Generated ${pages.length} landing pages.`);
