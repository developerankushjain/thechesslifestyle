#!/usr/bin/env python3
"""
Batch rebuild of 16 city/country guide pages with the new premium white theme.
Preserves all existing SEO content while applying the new design system.
"""
import os, re

BASE = "/Users/apple/Desktop/Projects/thechesslifestyle"

PAGES = [
    {
        "slug": "online-chess-classes-abu-dhabi",
        "lang": "en",
        "title": "Online Chess Classes in Abu Dhabi | FIDE Rated Coaches",
        "desc": "Online chess classes for kids & adults in Abu Dhabi by International FIDE Rated coaches. GST timezone slots. Book your FREE 45-min trial today!",
        "keywords": "online chess classes abu dhabi, chess coaching abu dhabi, chess lessons abu dhabi, FIDE coach abu dhabi",
        "canonical": "https://www.thechesslifestyle.com/online-chess-classes-abu-dhabi/",
        "og_image": "https://www.thechesslifestyle.com/gallery/20260822_162246.webp",
        "flag": "&#x1F1E6;&#x1F1EA;",
        "location": "Abu Dhabi",
        "region": "UAE",
        "timezone": "GST (UTC+4)",
        "timezones": "GST",
        "currency_symbol": "AED",
        "currency_note": "~AED 145/month",
        "form_subject": "New Trial Request — Abu Dhabi",
        "eyebrow": "Abu Dhabi, UAE &middot; FIDE Rated Coaches",
        "h1_end": "in Abu Dhabi",
        "lead": "Learn chess online from <strong>International FIDE Rated coaches</strong> &mdash; scheduled for <strong>GST timezone</strong> (UTC+4). Expert coaching for students in Abu Dhabi from age 5 to adult.",
        "stat1_num": "GST", "stat1_lbl": "Timezone Coverage",
        "stat2_num": "4.9&#9733;", "stat2_lbl": "Average Rating",
        "stat3_num": "FIDE", "stat3_lbl": "Verified Coaches",
        "stat4_num": "FREE", "stat4_lbl": "45-Min Trial",
        "local_body": """
<p>Abu Dhabi's chess scene is growing rapidly, supported by the UAE Chess Federation and a vibrant scholastic community. The city's international schools &mdash; from GEMS Education campuses to British curriculum schools in Khalifa City &mdash; increasingly include chess as a structured extracurricular activity.</p>
<p>For UAE residents, online coaching from India's FIDE Rated masters offers world-class instruction at a fraction of the cost of private in-person tutors, with sessions perfectly timed to GST evenings. Whether you're in Khalifa City, Al Reem Island, Saadiyat Island, or Al Ain, we schedule around you.</p>
<h3 style="color:var(--primary);margin-top:2rem;">UAE Chess Federation & FIDE Rated Play</h3>
<p>Students in Abu Dhabi can target official UAE Chess Federation tournaments and FIDE-rated events held regularly across the UAE. Our coaches prepare students specifically for classical time controls used in these competitions &mdash; building the calculation depth, endgame technique, and mental stamina required to perform under pressure.</p>
""",
        "testi": [
            ("My son attends from Abu Dhabi every Saturday morning. The coach is incredibly patient and my son has improved from not knowing the pieces to winning his school tournament in one year!", "Ahmed K.", "Abu Dhabi, UAE"),
            ("The GST timezone slots are perfect. My daughter joins after school and the sessions are always engaging. Her chess.com rating went from 650 to 1100 in 8 months!", "Priya S.", "Khalifa City, Abu Dhabi"),
            ("Brilliant online classes. Much more structured than the local chess club. The daily progress reports through their app are very helpful for us as parents.", "James O.", "Al Reem Island, Abu Dhabi"),
        ],
        "faqs": [
            ("Can I attend from Abu Dhabi?", "Absolutely. We have many students in Abu Dhabi and across the UAE. All sessions are scheduled to match GST (UTC+4) timezone — typically evening slots after 5 PM GST."),
            ("What is the class timing in UAE time?", "We offer slots from 5 PM to 9 PM GST on weekdays, and morning/afternoon slots on weekends. Exact timing is confirmed after your free trial."),
            ("Are your coaches FIDE rated?", "Yes. All our instructors hold verified FIDE ratings. You can check every profile on ratings.fide.com. Our head coach Chirag Soni holds FIDE ID 25971115."),
            ("Is the trial class free?", "Yes — 100% free, no credit card, no commitment. A full 45-minute live session on Zoom with a FIDE rated instructor."),
            ("How much do classes cost?", "Group classes start from approx. AED 145/month (~Rs. 3,999). We also offer quarterly and annual plans with 10-20% discounts. View our full pricing at /pricing/."),
        ],
        "related_links": [
            ("/online-chess-classes-uae/", "UAE Chess Classes"),
            ("/online-chess-classes-dubai/", "Dubai Chess Classes"),
            ("/online-chess-classes-saudi-arabia/", "Saudi Arabia Chess"),
            ("/online-chess-classes/", "All Online Chess Classes"),
        ],
    },
    {
        "slug": "online-chess-classes-australia",
        "lang": "en-AU",
        "title": "Online Chess Classes Australia | FIDE Coaches | TheChessLifestyle",
        "desc": "Online chess classes for kids & adults in Australia by International FIDE Rated coaches. AEDT/AEST slots. Book your FREE 45-min trial today!",
        "keywords": "online chess classes australia, chess coaching australia, chess lessons australia, FIDE coach australia",
        "canonical": "https://www.thechesslifestyle.com/online-chess-classes-australia/",
        "og_image": "https://www.thechesslifestyle.com/gallery/20260822_162246.webp",
        "flag": "&#x1F1E6;&#x1F1FA;",
        "location": "Australia",
        "region": "Australia",
        "timezone": "AEDT/AEST",
        "timezones": "AEDT, AEST, AWST",
        "currency_symbol": "AUD",
        "currency_note": "~AUD 80/month",
        "form_subject": "New Trial Request — Australia",
        "eyebrow": "Australia &middot; FIDE Rated Coaches",
        "h1_end": "in Australia",
        "lead": "Learn chess online from <strong>International FIDE Rated coaches</strong> &mdash; scheduled for <strong>Australian timezones (AEDT/AEST/AWST)</strong>. Premium coaching for students across Sydney, Melbourne, Brisbane, Perth and beyond.",
        "stat1_num": "AEDT", "stat1_lbl": "Timezone Coverage",
        "stat2_num": "4.9&#9733;", "stat2_lbl": "Average Rating",
        "stat3_num": "FIDE", "stat3_lbl": "Verified Coaches",
        "stat4_num": "FREE", "stat4_lbl": "45-Min Trial",
        "local_body": """
<p>Australia has one of the most vibrant scholastic chess scenes in the Asia-Pacific region. The Australian Chess Federation (ACF) runs structured state championship circuits, and Chess Victoria, Chess NSW, and Chess Queensland each maintain busy tournament calendars. The prestigious Australian Junior Chess Championships draw hundreds of competitors each year.</p>
<p>For Australian families, accessing FIDE-rated coaching has traditionally meant expensive private tutors or inconsistent local club resources. Our online model solves this: you get India's elite FIDE-rated coaches at highly competitive rates, with sessions perfectly matched to AEDT (UTC+11), AEST (UTC+10), or AWST (UTC+8) schedules.</p>
<h3 style="color:var(--primary);margin-top:2rem;">Australian Chess Federation & Scholastic Competitions</h3>
<p>Our coaches prepare students for the ACF rating system and major events including the Australian Junior Championships, State Scholastic Championships, and Interschool Chess competitions. We understand the Australian scholastic circuit and build our curriculum around the opening systems and endgame patterns most commonly encountered in ACF-rated play.</p>
""",
        "testi": [
            ("My daughter joins from Sydney every Sunday. She absolutely loves her coach and has improved so much. She went from unrated to an ACF rating of 1200 in 10 months!", "Priya K.", "Sydney, Australia"),
            ("The early morning AEDT slots work perfectly for us in Melbourne. Both my boys attend and their school chess team results have improved dramatically.", "David M.", "Melbourne, Australia"),
            ("Outstanding coaching quality at a very reasonable cost compared to what we'd pay for a local tutor in Brisbane. The parent progress reports after every session are genuinely useful.", "Sarah L.", "Brisbane, Australia"),
        ],
        "faqs": [
            ("Can I attend from Australia?", "Absolutely. We have students across Sydney, Melbourne, Brisbane, Perth, Adelaide, and Canberra. Sessions are scheduled to match AEDT, AEST, or AWST timezones."),
            ("What are the class times in Australian time?", "We typically offer early morning slots (6-9 AM AEDT) and weekend morning/afternoon slots. Exact timing is confirmed after your free trial."),
            ("Are your coaches FIDE rated?", "Yes. All instructors hold verified FIDE ratings — check every profile at ratings.fide.com."),
            ("Do you prepare students for ACF tournaments?", "Yes. We prepare students for ACF-rated events, Australian Junior Championships, and State Scholastic Championships."),
            ("Is the trial class free?", "Yes — 100% free, no credit card required. A full 45-minute live session with a FIDE rated instructor."),
        ],
        "related_links": [
            ("/online-chess-classes-sydney/", "Sydney Chess Classes"),
            ("/online-chess-classes-uk/", "UK Chess Classes"),
            ("/online-chess-classes-canada/", "Canada Chess Classes"),
            ("/online-chess-classes/", "All Online Chess Classes"),
        ],
    },
    {
        "slug": "online-chess-classes-canada",
        "lang": "en-CA",
        "title": "Online Chess Classes Canada | FIDE Coaches | TheChessLifestyle",
        "desc": "Online chess classes for kids & adults in Canada by FIDE Rated coaches. EST/CST/PST slots. Book your FREE 45-min trial today!",
        "keywords": "online chess classes canada, chess coaching canada, chess lessons canada, FIDE coach canada",
        "canonical": "https://www.thechesslifestyle.com/online-chess-classes-canada/",
        "og_image": "https://www.thechesslifestyle.com/gallery/20260603_101319.webp",
        "flag": "&#x1F1E8;&#x1F1E6;",
        "location": "Canada",
        "region": "Canada",
        "timezone": "EST/CST/PST",
        "timezones": "EST, CST, MST, PST",
        "currency_symbol": "CAD",
        "currency_note": "~CAD 68/month",
        "form_subject": "New Trial Request — Canada",
        "eyebrow": "Canada &middot; FIDE Rated Coaches",
        "h1_end": "in Canada",
        "lead": "Learn chess from <strong>International FIDE Rated coaches</strong> &mdash; scheduled for <strong>Canadian timezones (EST/CST/PST)</strong>. Premium coaching for students in Toronto, Vancouver, Montreal, Calgary and beyond.",
        "stat1_num": "EST", "stat1_lbl": "Timezone Coverage",
        "stat2_num": "4.9&#9733;", "stat2_lbl": "Average Rating",
        "stat3_num": "FIDE", "stat3_lbl": "Verified Coaches",
        "stat4_num": "FREE", "stat4_lbl": "45-Min Trial",
        "local_body": """
<p>Canada has a passionate and competitive scholastic chess community. Chess Canada and provincial associations like the Ontario Chess Association (OCA) and Chess BC run structured rating circuits and national championships. Events like the Canadian Junior Chess Championship and National Scholastic draw hundreds of competitors.</p>
<p>Canadian students benefit enormously from FIDE-rated coaching &mdash; the international calculation methodology and opening preparation our coaches provide gives students a decisive edge over opponents trained only in local club settings. Sessions fit seamlessly into Canadian EST, CST, MST, and PST evening schedules.</p>
<h3 style="color:var(--primary);margin-top:2rem;">Chess Canada & Provincial Tournaments</h3>
<p>Our curriculum is designed to prepare students for Chess Canada rated events and provincial championships. We specifically focus on the classical time controls used in OTB (over-the-board) Canadian tournaments, combined with digital practice on Chess.com and Lichess to accelerate improvement between sessions.</p>
""",
        "testi": [
            ("Both my kids attend from Toronto every weekend. They look forward to every single session! The coaches are so patient and skilled with children.", "Amit P.", "Toronto, Canada"),
            ("My son has been playing for 2 years with TheChessLifestyle. He's now one of the top-rated players in his school board and qualified for provincials. Fantastic programme!", "Michelle R.", "Vancouver, Canada"),
            ("The EST evening slots work perfectly for our family in Montreal. Very affordable compared to local tutors and the quality is exceptional.", "François D.", "Montreal, Canada"),
        ],
        "faqs": [
            ("Can I attend from Canada?", "Absolutely. We have students in Toronto, Vancouver, Montreal, Calgary, Ottawa and more. Sessions match EST, CST, MST, or PST timezones."),
            ("What time are classes in Canadian timezone?", "Evening slots from 5-9 PM across all Canadian timezones, plus weekend morning/afternoon slots. Confirmed after your free trial."),
            ("Are your coaches FIDE rated?", "Yes. All instructors are verified FIDE rated — check every profile at ratings.fide.com."),
            ("Do you prepare students for Chess Canada tournaments?", "Yes. We prepare students for Chess Canada and provincial OCA, Chess BC events and the National Scholastic Championships."),
            ("Is the trial class free?", "Yes — 100% free, no credit card required. A full 45-minute live session with a FIDE rated instructor."),
        ],
        "related_links": [
            ("/online-chess-classes-toronto/", "Toronto Chess Classes"),
            ("/online-chess-classes-usa/", "USA Chess Classes"),
            ("/online-chess-classes-uk/", "UK Chess Classes"),
            ("/online-chess-classes/", "All Online Chess Classes"),
        ],
    },
    {
        "slug": "online-chess-classes-chicago",
        "lang": "en-US",
        "title": "Online Chess Classes in Chicago | FIDE Coaches | TheChessLifestyle",
        "desc": "Online chess classes for kids & adults in Chicago by FIDE Rated coaches. CST timezone slots. Book your FREE 45-min trial today!",
        "keywords": "online chess classes chicago, chess coaching chicago, chess lessons chicago, chess tutor chicago",
        "canonical": "https://www.thechesslifestyle.com/online-chess-classes-chicago/",
        "og_image": "https://www.thechesslifestyle.com/gallery/20260715_111545.webp",
        "flag": "&#x1F1FA;&#x1F1F8;",
        "location": "Chicago",
        "region": "Illinois, USA",
        "timezone": "CST (UTC-6)",
        "timezones": "CST, CDT",
        "currency_symbol": "USD",
        "currency_note": "~$50/month",
        "form_subject": "New Trial Request — Chicago",
        "eyebrow": "Chicago, Illinois &middot; FIDE Rated Coaches",
        "h1_end": "in Chicago",
        "lead": "Learn chess online from <strong>International FIDE Rated coaches</strong> &mdash; scheduled for <strong>Chicago CST timezone</strong>. Premium online coaching for families across Chicagoland, the North Shore, Oak Park, and suburban Illinois.",
        "stat1_num": "CST", "stat1_lbl": "Timezone Coverage",
        "stat2_num": "4.9&#9733;", "stat2_lbl": "Average Rating",
        "stat3_num": "FIDE", "stat3_lbl": "Verified Coaches",
        "stat4_num": "FREE", "stat4_lbl": "45-Min Trial",
        "local_body": """
<p>Chicago has one of the most competitive scholastic chess scenes in the Midwest. The Illinois Chess Association (ICA) runs a busy tournament calendar year-round, from suburban quads in Naperville and Evanston to the Illinois State Scholastic Championships. The city's top magnet schools and private academies &mdash; from Northside College Prep to Francis W. Parker School &mdash; field highly competitive chess teams.</p>
<p>Chicago winters are notoriously harsh, but online chess classes mean zero disruption from snowstorms or traffic on the Dan Ryan. Your child gets consistent, high-quality FIDE-rated instruction from the comfort of home, perfectly timed to CST evenings and weekends.</p>
<h3 style="color:var(--primary);margin-top:2rem;">ICA Tournaments & Illinois Scholastic Chess</h3>
<p>Our coaches specifically prepare Chicago students for ICA-rated tournaments, Illinois State Championships, and national USCF events. We focus on the classical time controls and positional patterns most commonly encountered in ICA-rated play, giving our students a decisive competitive edge over opponents trained only in club settings.</p>
""",
        "testi": [
            ("Before joining TheChessLifestyle, my son would freeze up in long classical games. The coaches rebuilt his confidence completely. He gained 180 points at his last USCF event in Chicago!", "Tanya W.", "Chicago, Illinois"),
            ("The ICA tournament preparation our daughter received was outstanding. She placed 2nd at the Illinois State Scholastic U-12 section. Couldn't be happier!", "Marcus J.", "Evanston, Illinois"),
            ("CST evening slots are perfect for us. The coach is engaging, patient and pushes the kids at exactly the right pace. Highly recommend!", "Jennifer L.", "Naperville, Illinois"),
        ],
        "faqs": [
            ("Can I attend from Chicago?", "Absolutely. We have students across Chicagoland including the North Shore, Oak Park, Naperville, and Evanston. All sessions are scheduled to match CST timezone."),
            ("What time are classes in Chicago time (CST)?", "Evening slots from 5-9 PM CST on weekdays, plus weekend morning and afternoon slots. Exact timing confirmed after your free trial."),
            ("Are your coaches FIDE rated?", "Yes. All instructors are International FIDE rated — verify every profile at ratings.fide.com."),
            ("Do you prepare students for ICA/USCF tournaments?", "Yes. We prepare students for Illinois Chess Association (ICA) events, Illinois State Scholastics, and national USCF tournaments."),
            ("Is the trial class free?", "Yes — 100% free, no credit card, no commitment. A full 45-minute Zoom session with a FIDE rated instructor."),
        ],
        "related_links": [
            ("/online-chess-classes-usa/", "USA Chess Classes"),
            ("/online-chess-classes-houston/", "Houston Chess"),
            ("/online-chess-classes-new-york/", "New York Chess"),
            ("/online-chess-classes/", "All Online Chess Classes"),
        ],
    },
    {
        "slug": "online-chess-classes-dubai",
        "lang": "en",
        "title": "Online Chess Classes in Dubai | FIDE Rated Coaches | TheChessLifestyle",
        "desc": "Online chess classes for kids & adults in Dubai by International FIDE Rated coaches. GST timezone slots. Book your FREE 45-min trial today!",
        "keywords": "online chess classes dubai, chess coaching dubai, chess lessons dubai, chess tutor dubai",
        "canonical": "https://www.thechesslifestyle.com/online-chess-classes-dubai/",
        "og_image": "https://www.thechesslifestyle.com/gallery/20260822_162246.webp",
        "flag": "&#x1F1E6;&#x1F1EA;",
        "location": "Dubai",
        "region": "UAE",
        "timezone": "GST (UTC+4)",
        "timezones": "GST",
        "currency_symbol": "AED",
        "currency_note": "~AED 145/month",
        "form_subject": "New Trial Request — Dubai",
        "eyebrow": "Dubai, UAE &middot; FIDE Rated Coaches",
        "h1_end": "in Dubai",
        "lead": "Learn chess online from <strong>International FIDE Rated coaches</strong> &mdash; scheduled for <strong>Dubai GST timezone</strong>. Premium coaching for students in Dubai Marina, Downtown, Jumeirah, Mirdif and beyond.",
        "stat1_num": "GST", "stat1_lbl": "Timezone Coverage",
        "stat2_num": "4.9&#9733;", "stat2_lbl": "Average Rating",
        "stat3_num": "FIDE", "stat3_lbl": "Verified Coaches",
        "stat4_num": "FREE", "stat4_lbl": "45-Min Trial",
        "local_body": """
<p>Dubai is a thriving hub for scholastic chess. The Emirates Chess Federation (ECF) regularly hosts FIDE-rated events, and Dubai's international school ecosystem &mdash; from GEMS Wellington and Jumeirah College to Dubai American Academy &mdash; increasingly fields competitive chess teams. The Dubai Open is one of the strongest rated tournaments in the Middle East.</p>
<p>Online coaching with TheChessLifestyle gives Dubai families access to India's FIDE-rated masters at a fraction of the cost of local in-person tutors, with sessions perfectly timed to GST (UTC+4) evenings. Whether you're in Business Bay, Al Barsha, or Jumeirah, we schedule around your lifestyle.</p>
<h3 style="color:var(--primary);margin-top:2rem;">Emirates Chess Federation & FIDE-Rated Events</h3>
<p>Our coaches prepare students for Emirates Chess Federation (ECF) rated tournaments and major FIDE events held in Dubai. We focus on the classical time controls and theoretical preparation needed for competitive UAE chess, including the prestigious Dubai Open and Sharjah Masters.</p>
""",
        "testi": [
            ("My daughter attends from Dubai Marina every weekend. She won her school chess championship within 6 months of joining TheChessLifestyle. Incredible coaching!", "Sarah T.", "Dubai Marina, UAE"),
            ("The GST evening slots are very convenient. My son's chess.com rating went from 700 to 1200 in 9 months. The coaches are patient and highly knowledgeable.", "Ravi K.", "Downtown Dubai, UAE"),
            ("Outstanding programme. Much better than the local chess club. The post-session reports are detailed and keep us informed of exactly what our daughter is learning.", "Omar A.", "Jumeirah, Dubai"),
        ],
        "faqs": [
            ("Can I attend from Dubai?", "Absolutely. We have students across Dubai Marina, Downtown, JBR, Mirdif, Al Barsha and other areas. All sessions match GST (UTC+4) timezone."),
            ("What time are classes in Dubai time (GST)?", "Evening slots 5-9 PM GST on weekdays, plus weekend morning/afternoon slots. Confirmed after your free trial."),
            ("Are your coaches FIDE rated?", "Yes. All instructors are verified FIDE rated — check every profile at ratings.fide.com."),
            ("Do you prepare students for UAE/FIDE tournaments?", "Yes. We prepare for Emirates Chess Federation events, the Dubai Open, and other FIDE-rated tournaments held in the UAE."),
            ("Is the trial class free?", "Yes — 100% free, no credit card required. A full 45-minute live Zoom session with a FIDE rated instructor."),
        ],
        "related_links": [
            ("/online-chess-classes-uae/", "UAE Chess Classes"),
            ("/online-chess-classes-abu-dhabi/", "Abu Dhabi Chess"),
            ("/online-chess-classes-riyadh/", "Riyadh Chess"),
            ("/online-chess-classes/", "All Online Chess Classes"),
        ],
    },
    {
        "slug": "online-chess-classes-houston",
        "lang": "en-US",
        "title": "Online Chess Classes in Houston | FIDE Coaches | TheChessLifestyle",
        "desc": "Online chess classes for kids & adults in Houston by FIDE Rated coaches. CST timezone slots. Book your FREE 45-min trial today!",
        "keywords": "online chess classes houston, chess coaching houston, chess lessons houston, chess tutor houston texas",
        "canonical": "https://www.thechesslifestyle.com/online-chess-classes-houston/",
        "og_image": "https://www.thechesslifestyle.com/gallery/20260715_111545.webp",
        "flag": "&#x1F1FA;&#x1F1F8;",
        "location": "Houston",
        "region": "Texas, USA",
        "timezone": "CST (UTC-6)",
        "timezones": "CST, CDT",
        "currency_symbol": "USD",
        "currency_note": "~$50/month",
        "form_subject": "New Trial Request — Houston",
        "eyebrow": "Houston, Texas &middot; FIDE Rated Coaches",
        "h1_end": "in Houston",
        "lead": "Learn chess online from <strong>International FIDE Rated coaches</strong> &mdash; scheduled for <strong>Houston CST timezone</strong>. Premium coaching for families across The Woodlands, Sugar Land, Katy, Pearland and the Greater Houston area.",
        "stat1_num": "CST", "stat1_lbl": "Timezone Coverage",
        "stat2_num": "4.9&#9733;", "stat2_lbl": "Average Rating",
        "stat3_num": "FIDE", "stat3_lbl": "Verified Coaches",
        "stat4_num": "FREE", "stat4_lbl": "45-Min Trial",
        "local_body": """
<p>Houston is one of the fastest-growing scholastic chess hubs in the United States. The Texas Chess Association (TCA) runs a thriving tournament circuit, and the Houston area is home to some of the most competitive scholastic chess teams in the state. The Texas State Scholastic Championships regularly draw 1,000+ students from across Texas.</p>
<p>Houston's diverse, highly educated communities &mdash; from The Woodlands and Sugar Land to West University Place and Meyerland &mdash; have embraced chess as a cornerstone of academic enrichment. Our online model removes the commute from the equation, delivering FIDE-rated coaching directly into your home at CST-friendly evening times.</p>
<h3 style="color:var(--primary);margin-top:2rem;">Texas Chess Association & USCF Tournaments</h3>
<p>Our coaches prepare Houston students specifically for TCA-rated tournaments, the Texas State Scholastic Championships, Houston Open, and national USCF events including SuperNationals. We build opening repertoires and endgame technique that give Houston students a decisive edge in Texas's competitive scholastic environment.</p>
""",
        "testi": [
            ("My 7-year-old was struggling with focus at school. After 3 months of online classes with TheChessLifestyle, his teachers noticed a huge improvement. Truly remarkable!", "Jennifer M.", "Houston, Texas"),
            ("My daughter placed 3rd at the Texas State Scholastic U-10. The preparation from her coach at TheChessLifestyle made all the difference. Amazing programme!", "Michael R.", "Sugar Land, Texas"),
            ("The CST evening slots are very convenient. My son looks forward to every class. His USCF rating jumped 300 points in one year!", "Sonia P.", "The Woodlands, Texas"),
        ],
        "faqs": [
            ("Can I attend from Houston?", "Yes! We have many students across Houston, The Woodlands, Sugar Land, Katy, Pearland and Bayou City. All classes match CST timezone."),
            ("What time are classes in Houston (CST)?", "Evening slots 5-9 PM CST on weekdays, plus weekend slots. Confirmed after your free trial."),
            ("Are your coaches FIDE rated?", "Yes. All instructors are FIDE rated — verify every profile at ratings.fide.com."),
            ("Do you prepare for TCA/USCF tournaments?", "Yes. We prepare for Texas Chess Association events, Texas State Scholastics, and national USCF events including SuperNationals."),
            ("Is the trial class free?", "Yes — 100% free, no credit card required. A full 45-minute live session with a FIDE rated instructor."),
        ],
        "related_links": [
            ("/online-chess-classes-usa/", "USA Chess Classes"),
            ("/online-chess-classes-chicago/", "Chicago Chess"),
            ("/online-chess-classes-new-york/", "New York Chess"),
            ("/online-chess-classes/", "All Online Chess Classes"),
        ],
    },
    {
        "slug": "online-chess-classes-london",
        "lang": "en-GB",
        "title": "Online Chess Classes in London | FIDE Coaches | TheChessLifestyle",
        "desc": "Online chess classes for kids & adults in London by FIDE Rated coaches. GMT/BST timezone slots. Book your FREE 45-min trial today!",
        "keywords": "online chess classes london, chess coaching london, chess lessons london, chess tutor london",
        "canonical": "https://www.thechesslifestyle.com/online-chess-classes-london/",
        "og_image": "https://www.thechesslifestyle.com/gallery/20260715_111140.webp",
        "flag": "&#x1F1EC;&#x1F1E7;",
        "location": "London",
        "region": "United Kingdom",
        "timezone": "GMT/BST",
        "timezones": "GMT, BST",
        "currency_symbol": "GBP",
        "currency_note": "~&pound;38/month",
        "form_subject": "New Trial Request — London",
        "eyebrow": "London, UK &middot; FIDE Rated Coaches",
        "h1_end": "in London",
        "lead": "Learn chess online from <strong>International FIDE Rated coaches</strong> &mdash; scheduled for <strong>London GMT/BST timezone</strong>. Premium coaching for students across North, South, East, West London and Greater London.",
        "stat1_num": "GMT", "stat1_lbl": "Timezone Coverage",
        "stat2_num": "4.9&#9733;", "stat2_lbl": "Average Rating",
        "stat3_num": "FIDE", "stat3_lbl": "Verified Coaches",
        "stat4_num": "FREE", "stat4_lbl": "45-Min Trial",
        "local_body": """
<p>London has a legendary chess heritage &mdash; home to the famous London Chess Classic, the Richmond Chess Club (one of England's strongest), and a dense network of scholastic clubs across every borough. The English Chess Federation (ECF) runs a rigorous grading system, and London schools consistently produce some of England's strongest junior players.</p>
<p>For London families, our online model delivers world-class FIDE-rated instruction at a fraction of the cost of private London tutors, with sessions perfectly timed to GMT/BST evenings. Whether you're in Islington, Richmond, Wimbledon, or Canary Wharf, we schedule around your routine.</p>
<h3 style="color:var(--primary);margin-top:2rem;">English Chess Federation (ECF) & London Chess</h3>
<p>Our coaches prepare students specifically for ECF-rated events, London Junior Championships, and national UK scholastic competitions. We build the positional understanding and endgame technique required to progress through the ECF grading bands quickly &mdash; from 100 ECF to 160+ &mdash; giving London students a decisive edge in their local and national events.</p>
""",
        "testi": [
            ("Brilliant instructors from London. Very affordable compared to local UK tutors and far more structured. My son's ECF grade went from 90 to 145 in one year!", "Sarah T.", "London, UK"),
            ("The GMT morning slots on weekends work perfectly for us. My daughter is now competing at county level &mdash; something I never imagined possible when we started!", "James H.", "Wimbledon, London"),
            ("Highly professional. The post-session written analysis from the coach is incredibly detailed. My son's chess has transformed completely since joining.", "Priya A.", "Islington, London"),
        ],
        "faqs": [
            ("Can I attend from London?", "Absolutely. We have students across all London boroughs including Islington, Richmond, Wimbledon, Hackney, and Canary Wharf. Sessions match GMT/BST timezone."),
            ("What time are classes in London (GMT/BST)?", "Evening slots 6-9 PM GMT/BST on weekdays, plus weekend morning/afternoon slots. Confirmed after your free trial."),
            ("Are your coaches FIDE rated?", "Yes. All instructors are FIDE rated — verify every profile at ratings.fide.com."),
            ("Do you prepare students for ECF-rated tournaments?", "Yes. We prepare for ECF events, London Junior Championships, and national UK scholastic competitions."),
            ("Is the trial class free?", "Yes — 100% free, no credit card required. A full 45-minute live session with a FIDE rated instructor."),
        ],
        "related_links": [
            ("/online-chess-classes-uk/", "UK Chess Classes"),
            ("/online-chess-classes-australia/", "Australia Chess"),
            ("/online-chess-classes-canada/", "Canada Chess"),
            ("/online-chess-classes/", "All Online Chess Classes"),
        ],
    },
    {
        "slug": "online-chess-classes-los-angeles",
        "lang": "en-US",
        "title": "Online Chess Classes in Los Angeles | FIDE Coaches | TheChessLifestyle",
        "desc": "Online chess classes for kids & adults in Los Angeles by FIDE Rated coaches. PST timezone slots. Book your FREE 45-min trial today!",
        "keywords": "online chess classes los angeles, chess coaching LA, chess lessons los angeles, chess tutor los angeles",
        "canonical": "https://www.thechesslifestyle.com/online-chess-classes-los-angeles/",
        "og_image": "https://www.thechesslifestyle.com/gallery/20260715_111545.webp",
        "flag": "&#x1F1FA;&#x1F1F8;",
        "location": "Los Angeles",
        "region": "California, USA",
        "timezone": "PST (UTC-8)",
        "timezones": "PST, PDT",
        "currency_symbol": "USD",
        "currency_note": "~$50/month",
        "form_subject": "New Trial Request — Los Angeles",
        "eyebrow": "Los Angeles, California &middot; FIDE Rated Coaches",
        "h1_end": "in Los Angeles",
        "lead": "Learn chess online from <strong>International FIDE Rated coaches</strong> &mdash; scheduled for <strong>PST timezone</strong>. Skip the 405 traffic and get world-class coaching from home. Serving families across the San Fernando Valley, Westside, South Bay, and the SGV.",
        "stat1_num": "PST", "stat1_lbl": "Timezone Coverage",
        "stat2_num": "4.9&#9733;", "stat2_lbl": "Average Rating",
        "stat3_num": "FIDE", "stat3_lbl": "Verified Coaches",
        "stat4_num": "FREE", "stat4_lbl": "45-Min Trial",
        "local_body": """
<p>Los Angeles has a vibrant and rapidly growing scholastic chess community. The Southern California Chess Federation (SCCF) runs the state's largest scholastic circuit, and LA-area schools &mdash; from Harvard-Westlake and Polytechnic School to Alhambra High &mdash; consistently produce California's strongest junior players. The CalChess Scholastic State Championship is one of the most competitive in the country.</p>
<p>For SoCal families, online chess coaching eliminates the legendary LA traffic problem entirely. Get FIDE-rated instruction delivered directly to your home at PST-friendly evening times &mdash; whether you're in Santa Monica, Pasadena, Torrance, or Irvine.</p>
<h3 style="color:var(--primary);margin-top:2rem;">SCCF & CalChess Scholastic Tournaments</h3>
<p>Our coaches prepare LA students for SCCF-rated events, the CalChess Scholastic State Championship, and national USCF events including the SuperNationals. We understand the California scholastic landscape and build our curriculum around the tactical sharpness and opening systems most effective in California-style rapid/classical events.</p>
""",
        "testi": [
            ("My son had been stuck at 1300 for over a year. TheChessLifestyle coaches identified his middlegame weaknesses immediately. He crossed 1500 within 6 months!", "Rachel P.", "Pasadena, California"),
            ("The PST evening slots are perfect. My daughter has completely fallen in love with chess. She placed 3rd at CalChess State Scholastics U-12 this year!", "Kevin T.", "Santa Monica, California"),
            ("Outstanding value. Local LA chess tutors charge 3-4x the cost for a fraction of the expertise. This programme is exceptional.", "Sunita R.", "Torrance, California"),
        ],
        "faqs": [
            ("Can I attend from Los Angeles?", "Absolutely. We serve the entire Greater LA area including the Westside, San Fernando Valley, SGV, South Bay, and Orange County. All sessions match PST timezone."),
            ("What time are classes in LA time (PST)?", "Evening slots 5-9 PM PST on weekdays, plus weekend morning/afternoon slots. Confirmed after your free trial."),
            ("Are your coaches FIDE rated?", "Yes. All instructors are FIDE rated — verify at ratings.fide.com."),
            ("Do you prepare for SCCF/USCF tournaments?", "Yes. We prepare for SCCF events, CalChess State Championship, and national USCF events."),
            ("Is the trial class free?", "Yes — 100% free, no credit card required. A full 45-minute live session with a FIDE rated instructor."),
        ],
        "related_links": [
            ("/online-chess-classes-usa/", "USA Chess Classes"),
            ("/online-chess-classes-chicago/", "Chicago Chess"),
            ("/online-chess-classes-houston/", "Houston Chess"),
            ("/online-chess-classes/", "All Online Chess Classes"),
        ],
    },
    {
        "slug": "online-chess-classes-new-york",
        "lang": "en-US",
        "title": "Online Chess Classes in New York | FIDE Coaches | TheChessLifestyle",
        "desc": "Online chess classes for kids & adults in New York by FIDE Rated coaches. EST timezone slots. Book your FREE 45-min trial today!",
        "keywords": "online chess classes new york, chess coaching new york, chess lessons nyc, chess tutor new york",
        "canonical": "https://www.thechesslifestyle.com/online-chess-classes-new-york/",
        "og_image": "https://www.thechesslifestyle.com/gallery/20260603_101319.webp",
        "flag": "&#x1F1FA;&#x1F1F8;",
        "location": "New York",
        "region": "New York, USA",
        "timezone": "EST (UTC-5)",
        "timezones": "EST, EDT",
        "currency_symbol": "USD",
        "currency_note": "~$50/month",
        "form_subject": "New Trial Request — New York",
        "eyebrow": "New York City &middot; FIDE Rated Coaches",
        "h1_end": "in New York",
        "lead": "Learn chess online from <strong>International FIDE Rated coaches</strong> &mdash; scheduled for <strong>EST timezone</strong>. World-class coaching for New York students without the Manhattan commute. Serving families across NYC, Long Island, Westchester, and New Jersey.",
        "stat1_num": "EST", "stat1_lbl": "Timezone Coverage",
        "stat2_num": "4.9&#9733;", "stat2_lbl": "Average Rating",
        "stat3_num": "FIDE", "stat3_lbl": "Verified Coaches",
        "stat4_num": "FREE", "stat4_lbl": "45-Min Trial",
        "local_body": """
<p>New York City is the chess capital of the United States. Home to the legendary Marshall Chess Club (founded 1915), the New York State Chess Association, and one of the most intense scholastic chess circuits in the country, NYC students face elite competition at every level. The NY State Scholastic Championships and Marshall Club tournaments attract hundreds of highly-trained competitors.</p>
<p>The famous IS 318 chess programme in Brooklyn is a testament to what structured coaching can achieve &mdash; producing national champions from public school students. Our FIDE-rated coaches bring that same rigor to students across NYC, Long Island, Westchester, and the tri-state area, delivered online to EST schedules.</p>
<h3 style="color:var(--primary);margin-top:2rem;">NY State Scholastic & Marshall Chess Club</h3>
<p>Our coaches prepare students for NY State Scholastic Championships, Marshall Club events, and national USCF tournaments. We specifically build the tactical precision, positional depth, and clock management skills needed to compete at New York's ultra-competitive scholastic level.</p>
""",
        "testi": [
            ("My son attended online classes from Queens for 6 months. His rating jumped from 600 to 1050 and his focus in school has genuinely improved. Extraordinary coaching!", "Michael R.", "Queens, New York"),
            ("My daughter was already USCF 1400 when we joined. The coaches took her to 1680 in one year with deep positional training. She qualified for NY State Invitational!", "Tanya W.", "Westchester, New York"),
            ("Much more affordable than the local tutors we found in Manhattan, and far more structured. The post-session analysis is outstanding.", "Aisha K.", "Brooklyn, New York"),
        ],
        "faqs": [
            ("Can I attend from New York?", "Absolutely. We serve all NYC boroughs, Long Island, Westchester, Connecticut, and New Jersey. All sessions match EST timezone."),
            ("What time are classes in NY time (EST)?", "Evening slots 5-9 PM EST on weekdays, plus weekend morning/afternoon slots. Confirmed after your free trial."),
            ("Are your coaches FIDE rated?", "Yes. All instructors are FIDE rated — verify every profile at ratings.fide.com."),
            ("Do you prepare for NY State/USCF tournaments?", "Yes. We prepare for NY State Scholastic Championships, Marshall Club events, and national USCF tournaments including SuperNationals."),
            ("Is the trial class free?", "Yes — 100% free, no credit card required. A full 45-minute live session with a FIDE rated instructor."),
        ],
        "related_links": [
            ("/online-chess-classes-usa/", "USA Chess Classes"),
            ("/online-chess-classes-chicago/", "Chicago Chess"),
            ("/online-chess-classes-los-angeles/", "Los Angeles Chess"),
            ("/online-chess-classes/", "All Online Chess Classes"),
        ],
    },
    {
        "slug": "online-chess-classes-riyadh",
        "lang": "en",
        "title": "Online Chess Classes in Riyadh | FIDE Coaches | TheChessLifestyle",
        "desc": "Online chess classes for kids & adults in Riyadh by FIDE Rated coaches. AST timezone slots. Book your FREE 45-min trial today!",
        "keywords": "online chess classes riyadh, chess coaching riyadh, chess lessons riyadh, chess tutor saudi arabia",
        "canonical": "https://www.thechesslifestyle.com/online-chess-classes-riyadh/",
        "og_image": "https://www.thechesslifestyle.com/gallery/20260822_162246.webp",
        "flag": "&#x1F1F8;&#x1F1E6;",
        "location": "Riyadh",
        "region": "Saudi Arabia",
        "timezone": "AST (UTC+3)",
        "timezones": "AST",
        "currency_symbol": "SAR",
        "currency_note": "~SAR 188/month",
        "form_subject": "New Trial Request — Riyadh",
        "eyebrow": "Riyadh, Saudi Arabia &middot; FIDE Rated Coaches",
        "h1_end": "in Riyadh",
        "lead": "Learn chess online from <strong>International FIDE Rated coaches</strong> &mdash; scheduled for <strong>Riyadh AST timezone</strong>. Premium coaching for students and families across Riyadh, Al Malqa, Hittin, and the broader Saudi capital region.",
        "stat1_num": "AST", "stat1_lbl": "Timezone Coverage",
        "stat2_num": "4.9&#9733;", "stat2_lbl": "Average Rating",
        "stat3_num": "FIDE", "stat3_lbl": "Verified Coaches",
        "stat4_num": "FREE", "stat4_lbl": "45-Min Trial",
        "local_body": """
<p>Saudi Arabia's chess scene has undergone a remarkable transformation in recent years. The Saudi Chess Federation actively hosts FIDE-rated events, and Vision 2030's focus on sports and youth development has created a rapidly growing scholastic chess ecosystem. Riyadh's international school communities &mdash; from Riyadh International School to the British International School &mdash; are increasingly competitive in chess.</p>
<p>For families in Riyadh, online coaching with TheChessLifestyle provides access to elite FIDE-rated instruction at highly affordable rates, with sessions perfectly timed to AST (UTC+3) evenings. Whether you're in Al Malqa, Hittin, Olaya, or Al Nakheel, we schedule around your lifestyle.</p>
<h3 style="color:var(--primary);margin-top:2rem;">Saudi Chess Federation & FIDE Tournaments in KSA</h3>
<p>Our coaches prepare students for Saudi Chess Federation events and FIDE-rated tournaments held across the Kingdom. We build the tournament psychology, calculation depth, and endgame technique required to compete in classical time control events at the highest regional level.</p>
""",
        "testi": [
            ("The coach makes it so engaging. My daughter doesn't even realise she is learning critical thinking! She won her school's chess championship in her first year.", "Fatima A.", "Riyadh, Saudi Arabia"),
            ("Excellent programme for my two boys. The AST evening slots work perfectly for our schedule in Riyadh. Both have improved remarkably in 8 months.", "Abdullah M.", "Al Malqa, Riyadh"),
            ("The FIDE coaches here are far better than any local option I found in Riyadh. The structured curriculum and progress reports are outstanding.", "Omar K.", "Hittin, Riyadh"),
        ],
        "faqs": [
            ("Can I attend from Riyadh?", "Absolutely. We have students across Riyadh including Al Malqa, Hittin, Olaya, Al Nakheel, and Diplomatic Quarter. Sessions match AST (UTC+3)."),
            ("What time are classes in Riyadh time (AST)?", "Evening slots 5-9 PM AST on weekdays and weekend morning/afternoon slots. Confirmed after your free trial."),
            ("Are your coaches FIDE rated?", "Yes. All instructors are FIDE rated — verify every profile at ratings.fide.com."),
            ("Do you prepare students for Saudi/FIDE tournaments?", "Yes. We prepare for Saudi Chess Federation events and FIDE-rated tournaments held across KSA."),
            ("Is the trial class free?", "Yes — 100% free, no credit card required. A full 45-minute live session with a FIDE rated instructor."),
        ],
        "related_links": [
            ("/online-chess-classes-saudi-arabia/", "Saudi Arabia Chess"),
            ("/online-chess-classes-uae/", "UAE Chess Classes"),
            ("/online-chess-classes-dubai/", "Dubai Chess"),
            ("/online-chess-classes/", "All Online Chess Classes"),
        ],
    },
    {
        "slug": "online-chess-classes-saudi-arabia",
        "lang": "en",
        "title": "Online Chess Classes Saudi Arabia | FIDE Coaches | TheChessLifestyle",
        "desc": "Online chess classes for kids & adults in Saudi Arabia by FIDE Rated coaches. AST timezone slots. Book your FREE 45-min trial today!",
        "keywords": "online chess classes saudi arabia, chess coaching saudi arabia, chess lessons ksa, chess tutor saudi arabia",
        "canonical": "https://www.thechesslifestyle.com/online-chess-classes-saudi-arabia/",
        "og_image": "https://www.thechesslifestyle.com/gallery/20260822_162246.webp",
        "flag": "&#x1F1F8;&#x1F1E6;",
        "location": "Saudi Arabia",
        "region": "Saudi Arabia",
        "timezone": "AST (UTC+3)",
        "timezones": "AST",
        "currency_symbol": "SAR",
        "currency_note": "~SAR 188/month",
        "form_subject": "New Trial Request — Saudi Arabia",
        "eyebrow": "Saudi Arabia &middot; FIDE Rated Coaches",
        "h1_end": "in Saudi Arabia",
        "lead": "Learn chess online from <strong>International FIDE Rated coaches</strong> &mdash; scheduled for <strong>AST timezone (UTC+3)</strong>. Premium coaching for students across Riyadh, Jeddah, Dammam, Mecca, and the broader Kingdom.",
        "stat1_num": "AST", "stat1_lbl": "Timezone Coverage",
        "stat2_num": "4.9&#9733;", "stat2_lbl": "Average Rating",
        "stat3_num": "FIDE", "stat3_lbl": "Verified Coaches",
        "stat4_num": "FREE", "stat4_lbl": "45-Min Trial",
        "local_body": """
<p>Saudi Arabia is investing heavily in chess as part of its Vision 2030 national transformation programme. The Saudi Chess Federation has dramatically expanded its calendar of FIDE-rated events, and scholastic chess programmes are being introduced in schools across Riyadh, Jeddah, and Dammam. The Kingdom hosted the prestigious FIDE World Cup and is rapidly becoming a major chess hub in the Arab world.</p>
<p>For Saudi families, online coaching with TheChessLifestyle offers access to elite FIDE-rated instruction at exceptional value, with sessions perfectly matched to AST (UTC+3) schedules. Students in Riyadh, Jeddah, Dammam, Khobar, and Dhahran all benefit from our flexible scheduling.</p>
<h3 style="color:var(--primary);margin-top:2rem;">Saudi Chess Federation & Vision 2030</h3>
<p>Our coaches prepare Saudi students for Saudi Chess Federation rated events, Arab Chess Championship qualifiers, and FIDE-rated tournaments held across the Kingdom. We understand the competitive landscape of KSA chess and build our curriculum to give students the edge they need to rise through the national rating lists.</p>
""",
        "testi": [
            ("Excellent online chess coaching for my children. The AST evening slots work perfectly. Both my kids have improved dramatically and love their classes!", "Khalid A.", "Riyadh, Saudi Arabia"),
            ("My daughter won her school chess competition after just 4 months of coaching. The structured approach and patient coaches are exceptional.", "Fatima N.", "Jeddah, Saudi Arabia"),
            ("The best online chess programme we've tried. Very affordable, world-class coaches, and detailed progress reports after every session.", "Omar S.", "Dammam, Saudi Arabia"),
        ],
        "faqs": [
            ("Can I attend from Saudi Arabia?", "Absolutely. We have students across Riyadh, Jeddah, Dammam, Khobar, Dhahran, Mecca and Medina. All sessions match AST (UTC+3)."),
            ("What time are classes in Saudi Arabia time (AST)?", "Evening slots 5-9 PM AST on weekdays and weekend slots. Confirmed after your free trial."),
            ("Are your coaches FIDE rated?", "Yes. All instructors are FIDE rated — verify at ratings.fide.com."),
            ("Do you prepare for Saudi/FIDE events?", "Yes. We prepare for Saudi Chess Federation events and FIDE-rated tournaments across KSA and the Arab region."),
            ("Is the trial class free?", "Yes — 100% free, no credit card required. A full 45-minute live session with a FIDE rated instructor."),
        ],
        "related_links": [
            ("/online-chess-classes-riyadh/", "Riyadh Chess Classes"),
            ("/online-chess-classes-uae/", "UAE Chess Classes"),
            ("/online-chess-classes-dubai/", "Dubai Chess"),
            ("/online-chess-classes/", "All Online Chess Classes"),
        ],
    },
    {
        "slug": "online-chess-classes-sydney",
        "lang": "en-AU",
        "title": "Online Chess Classes in Sydney | FIDE Coaches | TheChessLifestyle",
        "desc": "Online chess classes for kids & adults in Sydney by FIDE Rated coaches. AEDT/AEST timezone slots. Book your FREE 45-min trial today!",
        "keywords": "online chess classes sydney, chess coaching sydney, chess lessons sydney, chess tutor sydney",
        "canonical": "https://www.thechesslifestyle.com/online-chess-classes-sydney/",
        "og_image": "https://www.thechesslifestyle.com/gallery/20260822_162246.webp",
        "flag": "&#x1F1E6;&#x1F1FA;",
        "location": "Sydney",
        "region": "New South Wales, Australia",
        "timezone": "AEDT/AEST",
        "timezones": "AEDT, AEST",
        "currency_symbol": "AUD",
        "currency_note": "~AUD 80/month",
        "form_subject": "New Trial Request — Sydney",
        "eyebrow": "Sydney, Australia &middot; FIDE Rated Coaches",
        "h1_end": "in Sydney",
        "lead": "Learn chess online from <strong>International FIDE Rated coaches</strong> &mdash; scheduled for <strong>Sydney AEDT/AEST timezone</strong>. Premium coaching for students across the Inner West, North Shore, Eastern Suburbs, Parramatta and Greater Sydney.",
        "stat1_num": "AEDT", "stat1_lbl": "Timezone Coverage",
        "stat2_num": "4.9&#9733;", "stat2_lbl": "Average Rating",
        "stat3_num": "FIDE", "stat3_lbl": "Verified Coaches",
        "stat4_num": "FREE", "stat4_lbl": "45-Min Trial",
        "local_body": """
<p>Sydney is one of Australia's premier chess hubs. Chess NSW runs a busy competitive calendar including the NSW Open, NSW Juniors, and State Scholastic Championships. The Sydney Grammar School and other top GPS schools field highly competitive chess teams, and the city's diverse, academically-oriented communities have embraced chess as a key cognitive enrichment activity.</p>
<p>For Sydney families, online coaching with TheChessLifestyle delivers FIDE-rated instruction at exceptional value compared to local Sydney tutors, with early morning and weekend AEDT/AEST slots that fit seamlessly around school schedules. Whether you're on the North Shore, in the Eastern Suburbs, Parramatta or the Inner West, we schedule around you.</p>
<h3 style="color:var(--primary);margin-top:2rem;">Chess NSW & ACF Tournaments</h3>
<p>Our coaches prepare Sydney students for Chess NSW events, ACF-rated tournaments, NSW Scholastic Championships, and the Australian Junior Chess Championships. We understand the specific demands of ACF-rated classical chess and build our curriculum to rapidly advance students through NSW and national ranking lists.</p>
""",
        "testi": [
            ("My daughter loves her Sunday morning chess sessions from Sydney. She already won her school chess championship within one year of joining. Incredible coaching!", "Priya K.", "Sydney, Australia"),
            ("The AEDT morning slots are perfect for us on the North Shore. Both my boys attend and have improved so much. The detailed session reports are very helpful!", "Andrew M.", "Chatswood, Sydney"),
            ("Outstanding value. Sydney-based private tutors charge 3x the price for less expertise. This programme is exceptional and the coaches are brilliant with kids.", "Rachel O.", "Parramatta, Sydney"),
        ],
        "faqs": [
            ("Can I attend from Sydney?", "Absolutely. We serve students across Sydney including the North Shore, Inner West, Eastern Suburbs, Parramatta, Western Sydney, and the Hills District. Sessions match AEDT/AEST."),
            ("What time are classes in Sydney time (AEDT)?", "Early morning slots 6-9 AM AEDT on weekdays, and morning/afternoon slots on weekends. Confirmed after your free trial."),
            ("Are your coaches FIDE rated?", "Yes. All instructors are FIDE rated — verify every profile at ratings.fide.com."),
            ("Do you prepare for Chess NSW/ACF tournaments?", "Yes. We prepare for Chess NSW events, NSW Scholastic Championships, and the Australian Junior Chess Championships."),
            ("Is the trial class free?", "Yes — 100% free, no credit card required. A full 45-minute live session with a FIDE rated instructor."),
        ],
        "related_links": [
            ("/online-chess-classes-australia/", "Australia Chess Classes"),
            ("/online-chess-classes-uk/", "UK Chess Classes"),
            ("/online-chess-classes-canada/", "Canada Chess Classes"),
            ("/online-chess-classes/", "All Online Chess Classes"),
        ],
    },
    {
        "slug": "online-chess-classes-toronto",
        "lang": "en-CA",
        "title": "Online Chess Classes in Toronto | FIDE Coaches | TheChessLifestyle",
        "desc": "Online chess classes for kids & adults in Toronto by FIDE Rated coaches. EST timezone slots. Book your FREE 45-min trial today!",
        "keywords": "online chess classes toronto, chess coaching toronto, chess lessons toronto, chess tutor toronto",
        "canonical": "https://www.thechesslifestyle.com/online-chess-classes-toronto/",
        "og_image": "https://www.thechesslifestyle.com/gallery/20260603_101319.webp",
        "flag": "&#x1F1E8;&#x1F1E6;",
        "location": "Toronto",
        "region": "Ontario, Canada",
        "timezone": "EST (UTC-5)",
        "timezones": "EST, EDT",
        "currency_symbol": "CAD",
        "currency_note": "~CAD 68/month",
        "form_subject": "New Trial Request — Toronto",
        "eyebrow": "Toronto, Ontario &middot; FIDE Rated Coaches",
        "h1_end": "in Toronto",
        "lead": "Learn chess online from <strong>International FIDE Rated coaches</strong> &mdash; scheduled for <strong>Toronto EST timezone</strong>. Premium coaching for families across the GTA &mdash; Scarborough, Mississauga, Markham, Brampton, North York and the City of Toronto.",
        "stat1_num": "EST", "stat1_lbl": "Timezone Coverage",
        "stat2_num": "4.9&#9733;", "stat2_lbl": "Average Rating",
        "stat3_num": "FIDE", "stat3_lbl": "Verified Coaches",
        "stat4_num": "FREE", "stat4_lbl": "45-Min Trial",
        "local_body": """
<p>Toronto has a rich chess tradition. The Ontario Chess Association (OCA) runs one of Canada's most competitive scholastic circuits, and the GTA's diverse, academically-oriented communities have embraced chess deeply. The Toronto Chess Academy, the Hart House Chess Club at the University of Toronto, and numerous school boards field highly competitive teams. The Ontario Scholastic Chess Championship attracts hundreds of students annually.</p>
<p>For Toronto families, online coaching removes commute times across the GTA entirely &mdash; delivering FIDE-rated instruction straight to your home at EST-friendly evenings. Whether you're in Markham, Scarborough, Mississauga, Brampton, or the City of Toronto proper, we schedule around your family's routine.</p>
<h3 style="color:var(--primary);margin-top:2rem;">Ontario Chess Association & National Championships</h3>
<p>Our coaches prepare Toronto students specifically for OCA-rated events, Ontario Scholastic Championships, and the Canadian National Junior Championships. We understand the GTA competitive landscape and build a curriculum that gives students decisive advantages against Ontario's strong scholastic field.</p>
""",
        "testi": [
            ("Both my kids (ages 8 and 11) attend from Toronto every weekend. They look forward to every single session! The coaches are brilliant with children.", "Amit P.", "Toronto, Canada"),
            ("My son was OCA-rated 900 when he started. He's now at 1350 and qualified for the Ontario Scholastic Championship. Fantastic progress in just one year!", "Michelle R.", "Markham, Ontario"),
            ("The EST evening slots are perfect for us in Mississauga. Very affordable compared to local tutors. The progress reports are detailed and actionable.", "Sarah K.", "Mississauga, Ontario"),
        ],
        "faqs": [
            ("Can I attend from Toronto?", "Absolutely. We serve students across the GTA including Markham, Scarborough, Mississauga, Brampton, North York, and Etobicoke. Sessions match EST timezone."),
            ("What time are classes in Toronto time (EST)?", "Evening slots 5-9 PM EST on weekdays, plus weekend morning/afternoon slots. Confirmed after your free trial."),
            ("Are your coaches FIDE rated?", "Yes. All instructors are FIDE rated — verify every profile at ratings.fide.com."),
            ("Do you prepare for OCA/Chess Canada tournaments?", "Yes. We prepare for OCA events, Ontario Scholastic Championships, and the Canadian National Junior Chess Championships."),
            ("Is the trial class free?", "Yes — 100% free, no credit card required. A full 45-minute live session with a FIDE rated instructor."),
        ],
        "related_links": [
            ("/online-chess-classes-canada/", "Canada Chess Classes"),
            ("/online-chess-classes-usa/", "USA Chess Classes"),
            ("/online-chess-classes-uk/", "UK Chess Classes"),
            ("/online-chess-classes/", "All Online Chess Classes"),
        ],
    },
    {
        "slug": "online-chess-classes-uae",
        "lang": "en",
        "title": "Online Chess Classes UAE | FIDE Coaches | TheChessLifestyle",
        "desc": "Online chess classes for kids & adults in UAE by International FIDE Rated coaches. GST timezone slots. Book your FREE 45-min trial today!",
        "keywords": "online chess classes uae, chess coaching uae, chess lessons uae, FIDE coach uae dubai abu dhabi",
        "canonical": "https://www.thechesslifestyle.com/online-chess-classes-uae/",
        "og_image": "https://www.thechesslifestyle.com/gallery/20260822_162246.webp",
        "flag": "&#x1F1E6;&#x1F1EA;",
        "location": "UAE",
        "region": "United Arab Emirates",
        "timezone": "GST (UTC+4)",
        "timezones": "GST",
        "currency_symbol": "AED",
        "currency_note": "~AED 145/month",
        "form_subject": "New Trial Request — UAE",
        "eyebrow": "UAE &middot; FIDE Rated Coaches",
        "h1_end": "in UAE",
        "lead": "Learn chess from <strong>International FIDE Rated coaches</strong> &mdash; scheduled for <strong>GST timezone (UTC+4)</strong>. Premium online coaching for students across Dubai, Abu Dhabi, Sharjah, Ajman, Ras Al Khaimah and all seven Emirates.",
        "stat1_num": "GST", "stat1_lbl": "Timezone Coverage",
        "stat2_num": "4.9&#9733;", "stat2_lbl": "Average Rating",
        "stat3_num": "FIDE", "stat3_lbl": "Verified Coaches",
        "stat4_num": "FREE", "stat4_lbl": "45-Min Trial",
        "local_body": """
<p>The UAE is rapidly becoming one of the Middle East's premier chess hubs. The Emirates Chess Federation (ECF) actively hosts FIDE-rated events and the Dubai Open is one of the strongest rated tournaments in the region. Schools across the UAE &mdash; particularly in the GEMS, Taaleem, and Fortes networks &mdash; are increasingly fielding competitive chess teams in Emirates-wide scholastic competitions.</p>
<p>For UAE families, TheChessLifestyle delivers FIDE-rated instruction at exceptional value compared to private in-person tutors, with GST-matched evening sessions that fit seamlessly around school and work schedules. Whether you're in Dubai, Abu Dhabi, Sharjah, Ajman, or any other emirate, we schedule around you.</p>
<h3 style="color:var(--primary);margin-top:2rem;">Emirates Chess Federation & FIDE-Rated Events</h3>
<p>Our coaches prepare UAE students for Emirates Chess Federation rated events, the Dubai Open, Abu Dhabi International, Sharjah Masters, and other FIDE-rated tournaments held regularly across the UAE. We build the calculation depth, endgame technique, and tournament psychology needed to compete at the highest regional and international level.</p>
""",
        "testi": [
            ("My son attends from Dubai Marina every weekend. In one year his chess.com rating went from 600 to 1200 and he won his school tournament. Incredible coaches!", "Sarah T.", "Dubai, UAE"),
            ("The GST evening slots are very convenient for us in Abu Dhabi. The coaches are patient, knowledgeable, and excellent with children. Highly recommend!", "Ahmed K.", "Abu Dhabi, UAE"),
            ("Outstanding structured programme. Much better than the local chess club options in Sharjah. The CRM progress reports are very useful for parents.", "James O.", "Sharjah, UAE"),
        ],
        "faqs": [
            ("Can I attend from the UAE?", "Absolutely. We have students across all seven Emirates including Dubai, Abu Dhabi, Sharjah, Ajman, RAK, Fujairah, and UAQ. Sessions match GST (UTC+4)."),
            ("What time are classes in UAE time (GST)?", "Evening slots 5-9 PM GST on weekdays and weekend morning/afternoon slots. Confirmed after your free trial."),
            ("Are your coaches FIDE rated?", "Yes. All instructors are FIDE rated — verify every profile at ratings.fide.com."),
            ("Do you prepare for ECF/FIDE UAE tournaments?", "Yes. We prepare for Emirates Chess Federation events, the Dubai Open, Abu Dhabi International, and Sharjah Masters."),
            ("Is the trial class free?", "Yes — 100% free, no credit card required. A full 45-minute live session with a FIDE rated instructor."),
        ],
        "related_links": [
            ("/online-chess-classes-dubai/", "Dubai Chess Classes"),
            ("/online-chess-classes-abu-dhabi/", "Abu Dhabi Chess"),
            ("/online-chess-classes-saudi-arabia/", "Saudi Arabia Chess"),
            ("/online-chess-classes/", "All Online Chess Classes"),
        ],
    },
    {
        "slug": "online-chess-classes-uk",
        "lang": "en-GB",
        "title": "Online Chess Classes UK | FIDE Coaches | TheChessLifestyle",
        "desc": "Online chess classes for kids & adults in UK by FIDE Rated coaches. GMT/BST timezone slots. Book your FREE 45-min trial today!",
        "keywords": "online chess classes uk, chess coaching uk, chess lessons uk, FIDE coach uk england",
        "canonical": "https://www.thechesslifestyle.com/online-chess-classes-uk/",
        "og_image": "https://www.thechesslifestyle.com/gallery/20260715_111140.webp",
        "flag": "&#x1F1EC;&#x1F1E7;",
        "location": "United Kingdom",
        "region": "United Kingdom",
        "timezone": "GMT/BST",
        "timezones": "GMT, BST",
        "currency_symbol": "GBP",
        "currency_note": "~&pound;38/month",
        "form_subject": "New Trial Request — UK",
        "eyebrow": "United Kingdom &middot; FIDE Rated Coaches",
        "h1_end": "in UK",
        "lead": "Learn chess from <strong>International FIDE Rated coaches</strong> &mdash; scheduled for <strong>GMT/BST timezone</strong>. Premium coaching for students across England, Scotland, Wales, and Northern Ireland. Much more affordable than local UK tutors.",
        "stat1_num": "GMT", "stat1_lbl": "Timezone Coverage",
        "stat2_num": "4.9&#9733;", "stat2_lbl": "Average Rating",
        "stat3_num": "FIDE", "stat3_lbl": "Verified Coaches",
        "stat4_num": "FREE", "stat4_lbl": "45-Min Trial",
        "local_body": """
<p>The United Kingdom has one of the world's richest chess traditions. The English Chess Federation (ECF) maintains a rigorous national grading system, and UK scholastic chess is highly competitive &mdash; from county junior championships to the national Schools Team Chess Championship. The famous London Chess Classic, the British Chess Championships, and the 4NCL league attract players of every level.</p>
<p>For UK families, our online model delivers FIDE-rated instruction at a fraction of the cost of local private tutors, with GMT/BST-matched evening sessions that fit seamlessly around school schedules. We serve students across England, Scotland, Wales, and Northern Ireland.</p>
<h3 style="color:var(--primary);margin-top:2rem;">English Chess Federation (ECF) & UK Junior Chess</h3>
<p>Our coaches prepare UK students specifically for the ECF grading system, county junior championships, national Schools Chess Championship, and the British Chess Championships. We understand the ECF grading bands (100-220) and build our curriculum to rapidly advance students through each level, from club player to county champion.</p>
""",
        "testi": [
            ("Brilliant online chess coaching. Very affordable compared to local UK tutors and far more structured. My son's ECF grade went from 90 to 155 in one year!", "Sarah T.", "London, UK"),
            ("My daughter joined at ECF 110 and is now 160 — county junior champion in her age group! The coaches are exceptional. Highly recommend to any UK family.", "James H.", "Manchester, UK"),
            ("We've tried several online chess platforms. TheChessLifestyle is by far the most structured and the coaches are the most qualified. Outstanding value for money.", "Priya A.", "Edinburgh, Scotland"),
        ],
        "faqs": [
            ("Can I attend from the UK?", "Absolutely. We have students across England, Scotland, Wales, and Northern Ireland. Sessions match GMT (winter) and BST (summer) timezone."),
            ("What time are classes in UK time (GMT/BST)?", "Evening slots 6-9 PM GMT/BST on weekdays, plus weekend morning/afternoon slots. Confirmed after your free trial."),
            ("Are your coaches FIDE rated?", "Yes. All instructors are FIDE rated — verify every profile at ratings.fide.com."),
            ("Do you prepare students for ECF-rated events?", "Yes. We prepare for ECF rated events, county junior championships, Schools Chess Championship, and the British Chess Championships."),
            ("Is the trial class free?", "Yes — 100% free, no credit card required. A full 45-minute live session with a FIDE rated instructor."),
        ],
        "related_links": [
            ("/online-chess-classes-london/", "London Chess Classes"),
            ("/online-chess-classes-australia/", "Australia Chess"),
            ("/online-chess-classes-canada/", "Canada Chess"),
            ("/online-chess-classes/", "All Online Chess Classes"),
        ],
    },
    {
        "slug": "online-chess-classes-usa",
        "lang": "en-US",
        "title": "Online Chess Classes USA | FIDE Coaches | TheChessLifestyle",
        "desc": "Online chess classes for kids & adults in USA by FIDE Rated coaches. EST/CST/PST slots. Book your FREE 45-min trial today!",
        "keywords": "online chess classes usa, chess coaching usa, chess lessons usa, FIDE coach usa america",
        "canonical": "https://www.thechesslifestyle.com/online-chess-classes-usa/",
        "og_image": "https://www.thechesslifestyle.com/gallery/20260603_101319.webp",
        "flag": "&#x1F1FA;&#x1F1F8;",
        "location": "USA",
        "region": "United States",
        "timezone": "EST/CST/PST",
        "timezones": "EST, CST, MST, PST",
        "currency_symbol": "USD",
        "currency_note": "~$50/month",
        "form_subject": "New Trial Request — USA",
        "eyebrow": "United States &middot; FIDE Rated Coaches",
        "h1_end": "in USA",
        "lead": "Learn chess from <strong>International FIDE Rated coaches</strong> &mdash; scheduled for <strong>EST, CST, MST, or PST timezone</strong>. Premium coaching designed to dominate <strong>USCF tournaments</strong> &mdash; starting from just <strong>~$50/month</strong>.",
        "stat1_num": "EST", "stat1_lbl": "Timezone Coverage",
        "stat2_num": "4.9&#9733;", "stat2_lbl": "Average Rating",
        "stat3_num": "FIDE", "stat3_lbl": "Verified Coaches",
        "stat4_num": "FREE", "stat4_lbl": "45-Min Trial",
        "local_body": """
<p>The United States is currently experiencing an unprecedented chess renaissance. Fuelled by Netflix's <em>The Queen's Gambit</em> and the explosion of online chess streaming, millions of Americans have taken up the Royal Game. The scholastic chess scene &mdash; from New York and Chicago to Houston and Los Angeles &mdash; has never been more competitive.</p>
<p>Parents across America recognise that chess builds the analytical focus, emotional resilience, and strategic thinking required for Ivy League admissions and STEM success. Our International FIDE Rated coaches deliver this world-class training at a fraction of the cost of local US tutors, with sessions perfectly matched to your timezone.</p>
<h3 style="color:var(--primary);margin-top:2rem;">USCF Tournaments & National Scholastics</h3>
<p>Our curriculum is specifically designed to accelerate USCF ratings. We prepare students for local USCF quads, state championships, and national events including SuperNationals and National Elementary/High School Championships. Our coaches understand the difference between USCF and FIDE ratings and build opening repertoires and endgame skills proven to succeed in US scholastic tournaments.</p>
""",
        "testi": [
            ("My daughter's USCF rating jumped from 1420 to 1600 in one tournament circuit after joining TheChessLifestyle. The coaching completely rebuilt her thought process!", "Emma C.", "California, USA"),
            ("My son had been stuck at 1300 for over a year. TheChessLifestyle coaches identified his middlegame weaknesses and he gained 200+ points in 6 months!", "Julia T.", "Texas, USA"),
            ("My son gained 180 points over the summer and now plays with real confidence in long classical games. The improvement has been extraordinary.", "Tanya W.", "New York, USA"),
        ],
        "faqs": [
            ("Can I attend from the USA?", "Absolutely. We have students across all US states. Sessions are scheduled to match your timezone: EST, CST, MST, or PST."),
            ("What time are classes in US time?", "Evening slots 5-9 PM across all US timezones, plus weekend morning/afternoon slots. Confirmed after your free trial."),
            ("Are your coaches FIDE rated?", "Yes. All instructors are FIDE rated — verify every profile at ratings.fide.com."),
            ("Do you prepare for USCF tournaments?", "Yes. We prepare for local USCF quads, state championships, SuperNationals, and national scholastic events. Our coaches understand the USCF system deeply."),
            ("Is the trial class free?", "Yes — 100% free, no credit card required. A full 45-minute live session with a FIDE rated instructor."),
        ],
        "related_links": [
            ("/online-chess-classes-new-york/", "New York Chess"),
            ("/online-chess-classes-chicago/", "Chicago Chess"),
            ("/online-chess-classes-los-angeles/", "Los Angeles Chess"),
            ("/online-chess-classes-houston/", "Houston Chess"),
        ],
    },
]


def build_related_links(links):
    items = ""
    for href, label in links:
        items += f'<a href="{href}" class="country-badge">{label}</a>\n'
    return items


def build_faqs(faqs, slug):
    items = ""
    for i, (q, a) in enumerate(faqs, 1):
        items += f"""
          <div class="faq-item">
            <button class="faq-btn" id="faq-{slug}-{i}" aria-expanded="false">{q}<span class="faq-icon">+</span></button>
            <div class="faq-ans"><p>{a}</p></div>
          </div>"""
    return items


def build_testimonials(testis):
    cards = ""
    for text, name, loc in testis:
        cards += f"""
          <div class="testi-card">
            <div class="qm">"</div>
            <div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
            <p class="rt">"{text}"</p>
            <div class="rname">{name}</div>
            <div class="rloc">{loc}</div>
          </div>"""
    return cards


def generate_page(p):
    related_html = build_related_links(p["related_links"])
    faq_html = build_faqs(p["faqs"], p["slug"])
    testi_html = build_testimonials(p["testi"])

    html = f"""<!DOCTYPE html>
<html lang="{p['lang']}">
<head>
  <meta charset="UTF-8" />
  <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
  <link rel="icon" type="image/png" sizes="192x192" href="/favicon.png" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{p['title']} | TheChessLifestyle</title>
  <meta name="description" content="{p['desc']}">
  <meta name="keywords" content="{p['keywords']}">
  <link rel="canonical" href="{p['canonical']}">
  <link rel="sitemap" type="application/xml" href="/sitemap.xml" />
  <meta property="og:title" content="{p['title']}">
  <meta property="og:description" content="{p['desc']}">
  <meta property="og:url" content="{p['canonical']}">
  <meta property="og:type" content="website">
  <meta property="og:image" content="{p['og_image']}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:site_name" content="TheChessLifestyle">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:site" content="@thechesslifestyle">
  <meta name="robots" content="index, follow">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Outfit:wght@400;600;700;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../style.css">
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@graph":[{{"@type":"Course","name":"{p['title']}","description":"{p['desc']}","provider":{{"@type":"Organization","name":"TheChessLifestyle","sameAs":"https://www.thechesslifestyle.com"}},"hasCourseInstance":{{"@type":"CourseInstance","courseMode":"online","inLanguage":"en"}}}},{{"@type":"FAQPage","mainEntity":[{','.join([f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a.replace(chr(39), chr(96))}"}}}}' for q,a in p['faqs']])}]}}]}}
  </script>
  <style>
    .city-hero{{position:relative;min-height:90vh;display:flex;align-items:center;overflow:hidden;background:#fff;padding:7rem 5% 5rem;}}
    .city-hero::before{{content:'';position:absolute;inset:0;pointer-events:none;background:radial-gradient(ellipse 70% 60% at 65% 50%,rgba(245,158,11,.07) 0%,transparent 70%),radial-gradient(ellipse 40% 50% at 10% 80%,rgba(245,158,11,.04) 0%,transparent 60%);}}
    .city-hero-inner{{max-width:1200px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:center;width:100%;position:relative;z-index:1;}}
    .eyebrow{{display:inline-flex;align-items:center;gap:.5rem;background:rgba(245,158,11,.1);border:1px solid rgba(245,158,11,.25);color:#92400e;font-size:.82rem;font-weight:600;letter-spacing:.06em;text-transform:uppercase;padding:.4rem 1rem;border-radius:100px;margin-bottom:1.5rem;}}
    .city-hero-text h1{{font-family:'Outfit',sans-serif;font-size:clamp(2.4rem,5vw,3.6rem);font-weight:900;line-height:1.1;color:#0f172a;margin-bottom:1.25rem;letter-spacing:-.03em;}}
    .city-hero-text h1 .hl{{color:var(--primary);}}
    .hero-lead{{font-size:1.1rem;color:#475569;line-height:1.7;margin-bottom:2rem;max-width:520px;}}
    .hero-ctas{{display:flex;gap:1rem;flex-wrap:wrap;margin-bottom:2.5rem;}}
    .btn-outline-am{{padding:.85rem 1.75rem;border:2px solid var(--primary);color:var(--primary);background:transparent;border-radius:50px;font-weight:600;font-size:.95rem;text-decoration:none;transition:all .25s ease;}}
    .btn-outline-am:hover{{background:var(--primary);color:#fff;}}
    .trust-pills{{display:flex;flex-wrap:wrap;gap:.6rem;}}
    .trust-pills .pill{{display:inline-flex;align-items:center;gap:.4rem;background:#f8fafc;border:1px solid #e2e8f0;color:#334155;font-size:.82rem;font-weight:500;padding:.4rem .85rem;border-radius:100px;}}
    .trust-pills .pill svg{{color:var(--primary);flex-shrink:0;}}
    .city-hero-visual{{position:relative;}}
    .city-hero-visual .main-img{{width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:24px;box-shadow:0 30px 80px rgba(0,0,0,.12);}}
    .float-card{{position:absolute;background:#fff;border-radius:14px;padding:.9rem 1.2rem;box-shadow:0 8px 32px rgba(0,0,0,.12);font-size:.85rem;font-weight:600;color:#0f172a;display:flex;align-items:center;gap:.6rem;border:1px solid #f1f5f9;white-space:nowrap;}}
    .float-card .dot{{width:8px;height:8px;border-radius:50%;background:#22c55e;box-shadow:0 0 0 3px rgba(34,197,94,.2);animation:pdot 2s infinite;}}
    @keyframes pdot{{0%,100%{{box-shadow:0 0 0 3px rgba(34,197,94,.2)}}50%{{box-shadow:0 0 0 6px rgba(34,197,94,.1)}}}}
    .fc1{{bottom:24px;left:-28px;animation:fy 3s ease-in-out infinite}}
    .fc2{{top:28px;right:-28px;animation:fy 3s ease-in-out 2s infinite}}
    .fc3{{top:50%;left:-36px;transform:translateY(-50%);animation:fy 3s ease-in-out 1s infinite}}
    @keyframes fy{{0%,100%{{translate:0 0}}50%{{translate:0 -8px}}}}
    .city-stats{{background:#0f172a;padding:2.5rem 5%;}}
    .city-stats-inner{{max-width:1100px;margin:0 auto;display:grid;grid-template-columns:repeat(4,1fr);gap:2rem;text-align:center;}}
    .stat-num{{font-family:'Outfit',sans-serif;font-size:2.2rem;font-weight:900;color:var(--primary);line-height:1;}}
    .stat-lbl{{font-size:.85rem;color:#94a3b8;margin-top:.4rem;}}
    .sec{{padding:6rem 5%;}}
    .sec-alt{{background:#f8fafc;}}
    .sec-inner{{max-width:1100px;margin:0 auto;}}
    .sec-inner-lg{{max-width:1200px;margin:0 auto;}}
    .sec-label{{display:inline-block;font-size:.78rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--primary);margin-bottom:1rem;}}
    .sec-title{{font-family:'Outfit',sans-serif;font-size:clamp(1.9rem,4vw,2.8rem);font-weight:800;color:#0f172a;line-height:1.2;letter-spacing:-.02em;margin-bottom:1rem;}}
    .sec-sub{{font-size:1.05rem;color:#64748b;max-width:560px;line-height:1.7;margin-bottom:3.5rem;}}
    .local-body{{font-size:1rem;color:#475569;line-height:1.8;max-width:820px;}}
    .local-body h3{{font-family:'Outfit',sans-serif;font-size:1.3rem;font-weight:700;color:#0f172a;margin-top:2rem;margin-bottom:.75rem;}}
    .local-body p{{margin-bottom:1.25rem;}}
    .feat-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:1.5rem;}}
    .feat-card{{background:#f8fafc;border:1px solid #e2e8f0;border-radius:18px;padding:2rem;transition:all .3s ease;}}
    .feat-card:hover{{border-color:var(--primary);background:rgba(245,158,11,.03);transform:translateY(-4px);box-shadow:0 16px 40px rgba(245,158,11,.1);}}
    .feat-icon{{width:48px;height:48px;background:rgba(245,158,11,.12);border-radius:12px;display:flex;align-items:center;justify-content:center;margin-bottom:1.25rem;color:var(--primary);}}
    .feat-card h3{{font-family:'Outfit',sans-serif;font-size:1.05rem;font-weight:700;color:#0f172a;margin-bottom:.6rem;}}
    .feat-card p{{font-size:.9rem;color:#64748b;line-height:1.65;}}
    .steps-wrap{{display:grid;grid-template-columns:repeat(3,1fr);gap:2rem;margin-top:3.5rem;position:relative;}}
    .steps-wrap::before{{content:'';position:absolute;top:40px;left:15%;right:15%;height:2px;background:linear-gradient(90deg,var(--primary),#f59e0b);opacity:.25;}}
    .occ-step{{text-align:center;}}
    .step-num{{width:80px;height:80px;background:linear-gradient(135deg,var(--primary),#f59e0b);border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:'Outfit',sans-serif;font-size:1.8rem;font-weight:900;color:#fff;margin:0 auto 1.5rem;box-shadow:0 8px 24px rgba(245,158,11,.3);position:relative;z-index:1;}}
    .occ-step h3{{font-family:'Outfit',sans-serif;font-size:1.1rem;font-weight:700;color:#0f172a;margin-bottom:.65rem;}}
    .occ-step p{{font-size:.9rem;color:#64748b;line-height:1.65;max-width:260px;margin:0 auto;}}
    .coaches-grid-occ{{display:grid;grid-template-columns:repeat(5,1fr);gap:1.25rem;margin-top:3rem;}}
    .coach-occ{{background:#fff;border:1px solid #e2e8f0;border-radius:18px;padding:1.5rem 1rem;text-align:center;transition:all .3s ease;}}
    .coach-occ:hover{{border-color:var(--primary);transform:translateY(-6px);box-shadow:0 16px 40px rgba(245,158,11,.12);}}
    .coach-occ img{{width:90px;height:90px;object-fit:cover;border-radius:50%;border:3px solid rgba(245,158,11,.2);margin:0 auto 1rem;display:block;}}
    .coach-occ h3{{font-family:'Outfit',sans-serif;font-size:1rem;font-weight:700;color:#0f172a;margin-bottom:.3rem;}}
    .coach-occ .exp{{font-size:.8rem;color:#64748b;margin-bottom:.4rem;}}
    .coach-occ .cr{{font-size:.82rem;font-weight:700;color:var(--primary);background:rgba(245,158,11,.1);padding:.2rem .7rem;border-radius:100px;display:inline-block;margin-bottom:.6rem;}}
    .coach-occ a{{display:block;font-size:.75rem;color:#94a3b8;text-decoration:none;transition:color .2s;}}
    .coach-occ a:hover{{color:var(--primary);}}
    .testi-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:1.5rem;margin-top:3rem;}}
    .testi-card{{background:#fff;border:1px solid #e2e8f0;border-radius:18px;padding:2rem;transition:all .3s ease;position:relative;}}
    .testi-card:hover{{border-color:rgba(245,158,11,.4);box-shadow:0 12px 36px rgba(245,158,11,.1);}}
    .testi-card .qm{{font-size:3.5rem;line-height:.5;color:rgba(245,158,11,.2);font-family:Georgia,serif;font-weight:900;position:absolute;top:1.5rem;left:1.75rem;}}
    .testi-card .stars{{color:var(--primary);font-size:.9rem;margin-bottom:1rem;padding-top:.75rem;}}
    .testi-card .rt{{font-size:.93rem;color:#334155;line-height:1.7;font-style:italic;margin-bottom:1.25rem;}}
    .testi-card .rname{{font-size:.85rem;font-weight:700;color:#0f172a;}}
    .testi-card .rloc{{font-size:.8rem;color:#94a3b8;}}
    .city-enrol{{background:linear-gradient(135deg,#0f172a 0%,#1e293b 100%);padding:6rem 5%;}}
    .city-enrol-inner{{max-width:1100px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:5rem;align-items:start;}}
    .city-enrol-left h2{{font-family:'Outfit',sans-serif;font-size:clamp(1.8rem,3.5vw,2.6rem);font-weight:800;color:#fff;line-height:1.2;letter-spacing:-.02em;margin-bottom:1.25rem;}}
    .city-enrol-left h2 .hl2{{color:var(--primary);}}
    .city-enrol-left>p{{font-size:1rem;color:#94a3b8;line-height:1.7;margin-bottom:2.5rem;}}
    .enrol-bullets{{list-style:none;padding:0;}}
    .enrol-bullets li{{display:flex;align-items:center;gap:.75rem;font-size:.93rem;color:#cbd5e1;margin-bottom:.85rem;}}
    .enrol-bullets li svg{{color:var(--primary);flex-shrink:0;}}
    .form-card{{background:#fff;border-radius:20px;padding:2.5rem;box-shadow:0 30px 60px rgba(0,0,0,.25);}}
    .form-card .ft{{font-family:'Outfit',sans-serif;font-size:1.3rem;font-weight:800;color:#0f172a;margin-bottom:.4rem;}}
    .form-card .fs{{font-size:.87rem;color:#64748b;margin-bottom:1.75rem;}}
    .form-card .fg{{margin-bottom:1rem;}}
    .form-card .fg input,.form-card .fg select,.form-card .fg textarea{{width:100%;padding:.8rem 1rem;border:1.5px solid #e2e8f0;border-radius:10px;font-size:.9rem;font-family:'Inter',sans-serif;color:#0f172a;background:#f8fafc;outline:none;transition:border-color .2s,box-shadow .2s;box-sizing:border-box;}}
    .form-card .fg input:focus,.form-card .fg select:focus,.form-card .fg textarea:focus{{border-color:var(--primary);box-shadow:0 0 0 3px rgba(245,158,11,.1);background:#fff;}}
    .form-row{{display:grid;grid-template-columns:1fr 1fr;gap:.85rem;margin-bottom:1rem;}}
    .sub-btn{{width:100%;padding:1rem;background:linear-gradient(135deg,var(--primary),#f59e0b);color:#fff;border:none;border-radius:50px;font-family:'Outfit',sans-serif;font-size:1rem;font-weight:700;cursor:pointer;transition:all .3s ease;box-shadow:0 8px 24px rgba(245,158,11,.35);margin-top:.5rem;}}
    .sub-btn:hover{{transform:translateY(-2px);box-shadow:0 12px 32px rgba(245,158,11,.45);}}
    .form-note{{text-align:center;font-size:.78rem;color:#94a3b8;margin-top:.75rem;}}
    .city-faq{{padding:6rem 5%;background:#fff;}}
    .city-faq-inner{{max-width:800px;margin:0 auto;}}
    .faq-list{{margin-top:3rem;}}
    .faq-item{{border:1px solid #e2e8f0;border-radius:14px;margin-bottom:.85rem;overflow:hidden;transition:border-color .2s;}}
    .faq-item:hover{{border-color:rgba(245,158,11,.4);}}
    .faq-btn{{width:100%;background:none;border:none;padding:1.25rem 1.5rem;text-align:left;font-family:'Inter',sans-serif;font-size:.97rem;font-weight:600;color:#0f172a;cursor:pointer;display:flex;align-items:center;justify-content:space-between;gap:1rem;transition:background .2s;}}
    .faq-btn:hover{{background:#f8fafc;}}
    .faq-icon{{width:28px;height:28px;border-radius:50%;border:1.5px solid #e2e8f0;display:flex;align-items:center;justify-content:center;flex-shrink:0;transition:all .3s;font-size:.9rem;color:var(--primary);}}
    .faq-item.open .faq-icon{{background:var(--primary);border-color:var(--primary);color:#fff;transform:rotate(45deg);}}
    .faq-ans{{max-height:0;overflow:hidden;transition:max-height .4s ease;padding:0 1.5rem;}}
    .faq-ans p{{font-size:.92rem;color:#475569;line-height:1.75;padding-bottom:1.25rem;}}
    .faq-item.open .faq-ans{{max-height:300px;}}
    .country-grid{{display:flex;flex-wrap:wrap;gap:.75rem;justify-content:center;margin-top:2rem;}}
    .country-badge{{display:inline-flex;align-items:center;gap:.5rem;background:#f8fafc;border:1px solid #e2e8f0;border-radius:100px;padding:.5rem 1.1rem;font-size:.87rem;font-weight:500;color:#334155;text-decoration:none;transition:all .2s;}}
    .country-badge:hover{{border-color:var(--primary);background:rgba(245,158,11,.05);color:var(--primary);}}
    .sr{{opacity:0;transform:translateY(24px);transition:opacity .65s ease,transform .65s ease;}}
    .sr.visible{{opacity:1;transform:none;}}
    @media(max-width:1024px){{.coaches-grid-occ{{grid-template-columns:repeat(3,1fr)}}}}
    @media(max-width:900px){{
      .city-hero-inner{{grid-template-columns:1fr;gap:2rem}}.city-hero-visual{{display:none}}
      .city-hero{{min-height:auto;padding:6rem 5% 3rem}}
      .feat-grid{{grid-template-columns:repeat(2,1fr)}}
      .steps-wrap{{grid-template-columns:1fr}}.steps-wrap::before{{display:none}}
      .city-enrol-inner{{grid-template-columns:1fr;gap:3rem}}
      .testi-grid{{grid-template-columns:1fr}}
      .coaches-grid-occ{{grid-template-columns:repeat(2,1fr)}}
      .city-stats-inner{{grid-template-columns:repeat(2,1fr)}}
    }}
    @media(max-width:600px){{.feat-grid{{grid-template-columns:1fr}}.form-row{{grid-template-columns:1fr}}}}
  </style>
</head>
<body>
  <nav class="navbar">
    <a href="/" class="logo">
      <img src="/favicon.svg" alt="TheChessLifestyle Chess King Logo" class="logo-icon" width="32" height="35" loading="eager"/>
      TheChessLifestyle
    </a>
    <ul class="nav-links" id="nav-links">
      <li><a href="/#benefits">Benefits</a></li>
      <li><a href="/#why-us">Why Choose Us</a></li>
      <li><a href="/#coaches">Coaches</a></li>
      <li><a href="/#gallery">Gallery</a></li>
      <li><a href="/#testimonials">Testimonies</a></li>
      <li><a href="/#blog">Blog</a></li>
      <li><a href="#enrol" class="btn-trial">Book Trial</a></li>
    </ul>
    <div class="mobile-menu-toggle" id="mobile-menu-toggle">&#9776;</div>
  </nav>

  <header class="city-hero">
    <div class="city-hero-inner">
      <div class="city-hero-text">
        <div class="eyebrow">
          <span>{p['flag']}</span> {p['eyebrow']}
        </div>
        <h1>Online Chess Classes<br><span class="hl">{p['h1_end']}</span></h1>
        <p class="hero-lead">{p['lead']}</p>
        <div class="hero-ctas">
          <a href="#enrol" class="btn-primary pulse-main">Book FREE Trial Class &rarr;</a>
          <a href="#coaches" class="btn-outline-am">Meet Our Coaches</a>
        </div>
        <div class="trust-pills">
          <span class="pill">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg>
            FIDE Verified Coaches
          </span>
          <span class="pill">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
            4.9 Star Rating
          </span>
          <span class="pill">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
            {p['timezone']}
          </span>
          <span class="pill">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>
            Age 5 to Adult
          </span>
        </div>
      </div>
      <div class="city-hero-visual">
        <img src="/gallery/20260822_162246.webp" alt="Online chess class {p['location']}" class="main-img" loading="eager">
        <div class="float-card fc1"><div class="dot"></div>Live Class in Progress</div>
        <div class="float-card fc2">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#f59e0b" stroke-width="2.5"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
          4.9&#9733; &mdash; 47 Reviews
        </div>
        <div class="float-card fc3">{p['flag']} {p['location']}</div>
      </div>
    </div>
  </header>

  <div class="city-stats">
    <div class="city-stats-inner">
      <div><div class="stat-num">{p['stat1_num']}</div><div class="stat-lbl">{p['stat1_lbl']}</div></div>
      <div><div class="stat-num">{p['stat2_num']}</div><div class="stat-lbl">{p['stat2_lbl']}</div></div>
      <div><div class="stat-num">{p['stat3_num']}</div><div class="stat-lbl">{p['stat3_lbl']}</div></div>
      <div><div class="stat-num">{p['stat4_num']}</div><div class="stat-lbl">{p['stat4_lbl']}</div></div>
    </div>
  </div>

  <main>
    <section class="sec sr">
      <div class="sec-inner">
        <span class="sec-label">Why TheChessLifestyle</span>
        <h2 class="sec-title">Why Our Coaching Stands <span style="color:var(--primary)">Apart</span></h2>
        <p class="sec-sub">We go beyond teaching moves. Our structured, tech-driven approach delivers measurable results for every student in {p['location']}.</p>
        <div class="feat-grid">
          <div class="feat-card">
            <div class="feat-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg></div>
            <h3>International FIDE Rated Coaches</h3>
            <p>Every instructor holds a verified FIDE rating. No hobby teachers &mdash; only nationally ranked players who compete at international level.</p>
          </div>
          <div class="feat-card">
            <div class="feat-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg></div>
            <h3>{p['timezone']} Timezone Classes</h3>
            <p>All sessions are scheduled to match {p['timezones']} &mdash; evening and weekend slots that fit around school and work schedules in {p['location']}.</p>
          </div>
          <div class="feat-card">
            <div class="feat-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg></div>
            <h3>CRM Progress Tracking</h3>
            <p>Parents get 24/7 access to session reports, homework assignments, and rating progression through our in-house platform after every class.</p>
          </div>
          <div class="feat-card">
            <div class="feat-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg></div>
            <h3>Level-Based Curriculum</h3>
            <p>From 0-Level (absolute beginner, age 5+) to Elite FIDE track. Every student begins with an assessment and follows a personalised roadmap.</p>
          </div>
          <div class="feat-card">
            <div class="feat-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg></div>
            <h3>In-House Online Tournaments</h3>
            <p>Regular internal tournaments give students real competitive experience in a safe, supportive environment &mdash; accelerating rating growth.</p>
          </div>
          <div class="feat-card">
            <div class="feat-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg></div>
            <h3>Post-Session Game Analysis</h3>
            <p>After every class, coaches analyse key moments from your game &mdash; turning mistakes into lasting learning opportunities for rapid improvement.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="sec sec-alt sr">
      <div class="sec-inner">
        <span class="sec-label">Local Context</span>
        <h2 class="sec-title">Chess in <span style="color:var(--primary)">{p['location']}</span></h2>
        <div class="local-body">{p['local_body']}</div>
      </div>
    </section>

    <section class="sec sr">
      <div class="sec-inner">
        <span class="sec-label">The Process</span>
        <h2 class="sec-title">How It <span style="color:var(--primary)">Works</span></h2>
        <p class="sec-sub">From booking your trial to your first class takes less than 48 hours.</p>
        <div class="steps-wrap">
          <div class="occ-step">
            <div class="step-num">1</div>
            <h3>Book a Free Trial</h3>
            <p>Fill the form below. We confirm your FREE 45-minute trial session within 24 hours &mdash; no card needed.</p>
          </div>
          <div class="occ-step">
            <div class="step-num">2</div>
            <h3>Meet Your FIDE Coach</h3>
            <p>Join via Zoom. Your coach assesses your level, explains the curriculum, and answers all your questions.</p>
          </div>
          <div class="occ-step">
            <div class="step-num">3</div>
            <h3>Start Your Journey</h3>
            <p>Enrol in the right programme. Weekly sessions, game analysis, progress reports &mdash; all working together.</p>
          </div>
        </div>
      </div>
    </section>

    <section id="coaches" class="sec sec-alt sr">
      <div class="sec-inner-lg">
        <span class="sec-label">The Team</span>
        <h2 class="sec-title">Meet Our <span style="color:var(--primary)">FIDE Rated Coaches</span></h2>
        <p class="sec-sub">Every coach holds a verifiable FIDE profile. No hobby teachers &mdash; only proven competitive players teaching your students.</p>
        <div class="coaches-grid-occ">
          <div class="coach-occ">
            <img src="/coaches/Chirag.webp" alt="Coach Chirag Soni FIDE Rated" loading="lazy">
            <h3>Chirag Soni</h3>
            <p class="exp">8 years coaching</p>
            <span class="cr">FIDE 1552</span>
            <a href="https://ratings.fide.com/profile/25971115" target="_blank" rel="noopener">FIDE ID: 25971115 &nearr;</a>
          </div>
          <div class="coach-occ">
            <img src="/coaches/Yash.webp" alt="Coach Yash FIDE Rated" loading="lazy">
            <h3>Yash</h3>
            <p class="exp">7 years coaching</p>
            <span class="cr">FIDE 1690</span>
            <a href="https://ratings.fide.com/profile/33350701" target="_blank" rel="noopener">FIDE ID: 33350701 &nearr;</a>
          </div>
          <div class="coach-occ">
            <img src="/coaches/Ankush.webp" alt="Coach Ankush" loading="lazy">
            <h3>Ankush</h3>
            <p class="exp">7 years coaching</p>
            <span class="cr">Chess.com 1630</span>
            <span style="font-size:.75rem;color:#e2e8f0;">&nbsp;</span>
          </div>
          <div class="coach-occ">
            <img src="/coaches/Ajay.webp" alt="Coach Ajay FIDE Rated" loading="lazy">
            <h3>Ajay</h3>
            <p class="exp">8 years coaching</p>
            <span class="cr">FIDE 1600</span>
            <a href="https://ratings.fide.com/profile/25963716" target="_blank" rel="noopener">FIDE ID: 25963716 &nearr;</a>
          </div>
          <div class="coach-occ">
            <img src="/coaches/Jatin.webp" alt="Coach Jatin FIDE Rated" loading="lazy">
            <h3>Jatin</h3>
            <p class="exp">8 years coaching</p>
            <span class="cr">FIDE 1691</span>
            <a href="https://ratings.fide.com/profile/583048723" target="_blank" rel="noopener">FIDE ID: 583048723 &nearr;</a>
          </div>
        </div>
      </div>
    </section>

    <section id="gallery" class="sec sr">
      <div class="sec-inner">
        <span class="sec-label">From Our Classes</span>
        <h2 class="sec-title">Our <span style="color:var(--primary)">Gallery</span></h2>
        <p class="sec-sub">Glimpses from our vibrant online classes and in-house tournaments.</p>
        <div class="gallery-wrapper" style="margin-top:2rem;">
          <div class="gallery-nav prev" id="gallery-prev">&#10094;</div>
          <div class="gallery-scroll-container" id="gallery-scroll">
            <div class="gallery-item"><img src="/gallery/20260418_141700.webp" alt="Chess class" loading="lazy"/></div>
            <div class="gallery-item"><img src="/gallery/20260603_101319.webp" alt="Chess coaching" loading="lazy"/></div>
            <div class="gallery-item"><video autoplay loop muted playsinline src="/gallery/20260714_110228.mp4"></video></div>
            <div class="gallery-item"><img src="/gallery/20260715_111140.webp" alt="Student session" loading="lazy"/></div>
            <div class="gallery-item"><img src="/gallery/20260822_121216.webp" alt="Chess tournament" loading="lazy"/></div>
            <div class="gallery-item"><img src="/gallery/20260822_162246.webp" alt="Online chess training" loading="lazy"/></div>
            <div class="gallery-item"><img src="/gallery/20260823_121331.webp" alt="Kids chess class" loading="lazy"/></div>
            <div class="gallery-item"><img src="/gallery/IMG-20260823-WA0039.webp" alt="Chess progress" loading="lazy"/></div>
          </div>
          <div class="gallery-nav next" id="gallery-next">&#10095;</div>
        </div>
      </div>
    </section>

    <section id="testimonials" class="sec sec-alt sr">
      <div class="sec-inner">
        <span class="sec-label">Reviews</span>
        <h2 class="sec-title">What <span style="color:var(--primary)">Students Say</span></h2>
        <p class="sec-sub">Hear from families who joined us from {p['location']} and beyond.</p>
        <div class="testi-grid">
          {testi_html}
        </div>
      </div>
    </section>

    <section id="enrol" class="city-enrol sr">
      <div class="city-enrol-inner">
        <div class="city-enrol-left">
          <span class="sec-label" style="color:rgba(245,158,11,.8);">Free Trial &mdash; No Commitment</span>
          <h2>Book Your <span class="hl2">FREE 45-Minute</span> Trial Class Today</h2>
          <p>No credit card. No commitment. A full live session with a FIDE rated coach who will assess your level and design a personalised learning plan for you.</p>
          <ul class="enrol-bullets">
            <li><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>100% free &mdash; no hidden fees whatsoever</li>
            <li><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>Live 45-min session via Zoom with a FIDE coach</li>
            <li><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>Level assessment &amp; personalised plan</li>
            <li><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>Confirmed within 24 hours of booking</li>
            <li><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>Scheduled for {p['timezone']} timezone</li>
          </ul>
          <div style="margin-top:2.5rem;padding:1.5rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:14px;">
            <p style="color:#cbd5e1;font-size:.9rem;margin:0;line-height:1.6;">
              <strong style="color:#fff;">Pricing starts from</strong><br>
              &#x20B9;3,999/month &middot; {p['currency_note']}<br>
              <a href="/pricing/" style="color:var(--primary);font-weight:600;font-size:.85rem;">View full pricing &amp; discounts &rarr;</a>
            </p>
          </div>
        </div>
        <div class="form-card">
          <div class="ft">Book Your Free Trial</div>
          <div class="fs">We'll confirm within 24 hours &mdash; {p['timezone']} slot</div>
          <form action="https://formspree.io/f/xvzjjenb" method="POST">
            <input type="text" name="_gotcha" style="display:none">
            <input type="hidden" name="_captcha" value="false">
            <input type="hidden" name="_subject" value="{p['form_subject']}">
            <div class="fg"><input type="text" name="Student Name" placeholder="Student's Full Name *" required></div>
            <div class="form-row">
              <div class="fg" style="margin-bottom:0;"><input type="text" name="Age or Class" placeholder="Age / Grade *" required></div>
              <div class="fg" style="margin-bottom:0;"><input type="text" name="City" placeholder="City (e.g. {p['location']})"></div>
            </div>
            <div class="fg">
              <select name="Chess Experience Level" required>
                <option value="" disabled selected>Chess Experience Level *</option>
                <option>I don't know how pieces move</option>
                <option>Knows pieces &mdash; not openings yet</option>
                <option>Knows opening principles</option>
                <option>Chess.com rating below 1200</option>
                <option>Chess.com rating above 1200</option>
              </select>
            </div>
            <div class="fg"><input type="email" name="Email" placeholder="Email Address *" required></div>
            <div class="fg"><input type="tel" name="Phone Number" placeholder="WhatsApp / Phone Number *" required></div>
            <div class="fg"><textarea name="Message" rows="2" placeholder="Any questions or requirements?"></textarea></div>
            <button type="submit" class="sub-btn">Book My FREE Trial Class &rarr;</button>
            <p class="form-note">100% free &middot; No credit card &middot; No commitment</p>
          </form>
        </div>
      </div>
    </section>

    <section class="city-faq sr">
      <div class="city-faq-inner">
        <div style="text-align:center;">
          <span class="sec-label">Got Questions?</span>
          <h2 class="sec-title">Frequently Asked <span style="color:var(--primary)">Questions</span></h2>
          <p style="font-size:1.05rem;color:#64748b;margin:.75rem auto 0;max-width:560px;line-height:1.7;">Everything you need to know about online chess classes in {p['location']}.</p>
        </div>
        <div class="faq-list">
          {faq_html}
        </div>
        <div style="text-align:center;margin-top:2.5rem;">
          <a href="#enrol" class="btn-primary">Book Your Free Trial &rarr;</a>
        </div>
      </div>
    </section>

    <section class="sec sec-alt sr">
      <div style="max-width:1100px;margin:0 auto;text-align:center;">
        <span class="sec-label">Explore More</span>
        <h2 class="sec-title">More <span style="color:var(--primary)">City &amp; Country Guides</span></h2>
        <div class="country-grid">
          {related_html}
        </div>
        <p style="margin-top:1.5rem;font-size:.85rem;color:#94a3b8;">Don't see your city? <a href="#enrol" style="color:var(--primary);font-weight:600;">Book a trial</a> &mdash; we serve all timezones.</p>
      </div>
    </section>
  </main>

  <footer>
    <div class="container">
      <div class="footer-top">
        <div class="footer-brand">
          <img src="/favicon.svg" alt="TheChessLifestyle Logo" class="footer-logo" width="40" height="40" style="margin-bottom:.5rem;"/>
          <h2>TheChessLifestyle</h2>
          <p>Premium online chess coaching provided by elite FIDE Rated instructors for students all over the globe.</p>
        </div>
        <div class="footer-links">
          <h4>Services</h4>
          <ul>
            <li><a href="/online-chess-classes/">Online Chess Classes</a></li>
            <li><a href="/online-chess-classes-for-kids/">Classes for Kids</a></li>
            <li><a href="/pricing/">Pricing &amp; Plans</a></li>
            <li><a href="/blog/">Chess Blog</a></li>
          </ul>
        </div>
        <div class="footer-links">
          <h4>Legal</h4>
          <ul>
            <li><a href="/privacy.html">Privacy Policy</a></li>
            <li><a href="/terms.html">Terms of Service</a></li>
            <li><a href="/refund.html">Refund Policy</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        &copy; 2026 TheChessLifestyle. All rights reserved. Providing online coaches all over the globe.
      </div>
    </div>
  </footer>

  <script>
    const tog = document.getElementById('mobile-menu-toggle');
    if(tog) tog.addEventListener('click',()=>document.getElementById('nav-links').classList.toggle('active'));
    document.querySelectorAll('.nav-links a').forEach(l=>l.addEventListener('click',()=>document.getElementById('nav-links').classList.remove('active')));
    const gs = document.getElementById('gallery-scroll');
    document.getElementById('gallery-prev')?.addEventListener('click',()=>gs.scrollBy({{left:-320,behavior:'smooth'}}));
    document.getElementById('gallery-next')?.addEventListener('click',()=>gs.scrollBy({{left:320,behavior:'smooth'}}));
    document.querySelectorAll('.faq-item').forEach(item=>{{
      item.querySelector('.faq-btn').addEventListener('click',()=>{{
        const open=item.classList.contains('open');
        document.querySelectorAll('.faq-item').forEach(i=>i.classList.remove('open'));
        if(!open) item.classList.add('open');
      }});
    }});
    const obs=new IntersectionObserver(entries=>entries.forEach(e=>{{
      if(e.isIntersecting){{e.target.classList.add('visible');obs.unobserve(e.target);}}
    }}),{{threshold:.1,rootMargin:'0px 0px -40px 0px'}});
    document.querySelectorAll('.sr').forEach(el=>obs.observe(el));
  </script>
</body>
</html>"""
    return html


# Build all pages
count = 0
for p in PAGES:
    out_path = os.path.join(BASE, p["slug"], "index.html")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(generate_page(p))
    print(f"✓ {p['slug']}")
    count += 1

print(f"\nDone! {count} pages rebuilt.")
