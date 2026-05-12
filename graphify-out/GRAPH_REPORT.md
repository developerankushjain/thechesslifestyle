# Graph Report - thechesslifestyle  (2026-05-12)

## Corpus Check
- 7 files · ~140,464 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 68 nodes · 56 edges · 20 communities (10 shown, 10 thin omitted)
- Extraction: 80% EXTRACTED · 20% INFERRED · 0% AMBIGUOUS · INFERRED: 11 edges (avg confidence: 0.81)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `cfdf2de4`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- [[_COMMUNITY_Homepage JS & Animations|Homepage JS & Animations]]
- [[_COMMUNITY_SEO Landing Pages & FIDE USP|SEO Landing Pages & FIDE USP]]
- [[_COMMUNITY_Landing Page JS Internals|Landing Page JS Internals]]
- [[_COMMUNITY_Landing Page Shared Scripts|Landing Page Shared Scripts]]
- [[_COMMUNITY_Vite Dev Scaffold|Vite Dev Scaffold]]
- [[_COMMUNITY_Tournaments & Events|Tournaments & Events]]
- [[_COMMUNITY_Trial Class Enrollment Flow|Trial Class Enrollment Flow]]
- [[_COMMUNITY_Cognitive Benefits Visual Section|Cognitive Benefits Visual Section]]
- [[_COMMUNITY_Hero Section & King Image|Hero Section & King Image]]
- [[_COMMUNITY_Why Choose Us Section|Why Choose Us Section]]
- [[_COMMUNITY_Refund Policy|Refund Policy]]
- [[_COMMUNITY_Privacy Policy|Privacy Policy]]
- [[_COMMUNITY_Google Search Console Verification|Google Search Console Verification]]
- [[_COMMUNITY_Favicon Brand Icon|Favicon Brand Icon]]
- [[_COMMUNITY_UI Icons Sprite|UI Icons Sprite]]
- [[_COMMUNITY_SVG Favicon|SVG Favicon]]
- [[_COMMUNITY_Scaffold Hero Asset|Scaffold Hero Asset]]
- [[_COMMUNITY_Community 19|Community 19]]

## God Nodes (most connected - your core abstractions)
1. `Homepage` - 6 edges
2. `Vite Build Config` - 5 edges
3. `Indian FIDE Rated Coach — Core USP` - 4 edges
4. `Main JS Entry Point` - 3 edges
5. `Landing Page Shared JS` - 3 edges
6. `Trial Class Enrollment Form` - 3 edges
7. `Chess Classes Noida SEO Landing Page` - 3 edges
8. `Online Chess Classes — Primary SEO Target` - 3 edges
9. `Noida Local SEO Strategy` - 3 edges
10. `Elite 18 Showcase Tournament Page` - 3 edges

## Surprising Connections (you probably didn't know these)
- `Vite Logo Asset (Dev scaffold)` --conceptually_related_to--> `Vite Build Config`  [INFERRED]
  src/assets/vite.svg → vite.config.js
- `Vite Build Config` --references--> `Pricing Packages Page`  [EXTRACTED]
  vite.config.js → packages/index.html
- `Vite Build Config` --references--> `Chess Home Tutor Noida Landing Page`  [EXTRACTED]
  vite.config.js → chess-home-tutor-noida/index.html
- `Main JS Entry Point` --implements--> `Homepage`  [EXTRACTED]
  main.js → index.html
- `Glowing Gold King — Hero Section Image` --references--> `Homepage Hero Section`  [INFERRED]
  public/glowing_king_hero_1775631608464.png → index.html

## Hyperedges (group relationships)
- **Noida Local SEO Pages Cluster** — chess_classes_noida_page, chess_home_tutor_noida_page, noida_local_seo_concept [INFERRED 0.85]
- **Trial Class Registration Flow** — homepage_enrol_form, homepage_class_preference_field, formsubmit_integration [EXTRACTED 1.00]
- **Chess Visual Assets Cluster** — img_glowing_king, img_abstract_mind, img_pawns_ascent, img_strategic_knight, img_academy_glow [INFERRED 0.85]

## Communities (20 total, 10 thin omitted)

### Community 0 - "Homepage JS & Animations"
Cohesion: 0.23
Nodes (12): Vite Logo Asset (Dev scaffold), Chess Classes Noida SEO Landing Page, Chess Home Tutor Noida Landing Page, Indian FIDE Rated Coach — Core USP, Homepage, FIDE Trust Bar, Homepage Hero Section, Glowing Gold King — Hero Section Image (+4 more)

### Community 1 - "SEO Landing Pages & FIDE USP"
Cohesion: 0.18
Nodes (10): floaters, glowTracker, navLinks, rect, revealObserver, revealOptions, scrollElements, speed (+2 more)

### Community 2 - "Landing Page JS Internals"
Cohesion: 0.29
Nodes (5): dir, fs, geoPages, pages, path

### Community 3 - "Landing Page Shared Scripts"
Cohesion: 0.29
Nodes (6): glow, isOpen, item, navLinks, observer, toggle

### Community 4 - "Vite Dev Scaffold"
Cohesion: 0.5
Nodes (5): FAQ Accordion Interaction, Landing Page Shared JS, Mouse Glow Cursor Tracker, Scroll Reveal Animation, Main JS Entry Point

### Community 6 - "Trial Class Enrollment Flow"
Cohesion: 0.5
Nodes (4): Elite 18 Chess Showcase Event, Academy Glow — Ambiance Visual (Antique Clock & Board), Tournament Registration Form, Elite 18 Showcase Tournament Page

### Community 7 - "Cognitive Benefits Visual Section"
Cohesion: 0.67
Nodes (3): Chess Cognitive Benefits Section, Abstract Mind — Geometric Chess Cognition Graphic, Pawns Ascending to Queen — Benefits Section Graphic

### Community 8 - "Hero Section & King Image"
Cohesion: 0.67
Nodes (3): FormSubmit Email Integration, Online vs Offline Class Preference Field, Trial Class Enrollment Form

## Knowledge Gaps
- **44 isolated node(s):** `fs`, `path`, `pages`, `geoPages`, `dir` (+39 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **10 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Homepage` connect `Homepage JS & Animations` to `Hero Section & King Image`, `Vite Dev Scaffold`?**
  _High betweenness centrality (0.055) - this node is a cross-community bridge._
- **Why does `Main JS Entry Point` connect `Vite Dev Scaffold` to `Homepage JS & Animations`?**
  _High betweenness centrality (0.027) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Indian FIDE Rated Coach — Core USP` (e.g. with `Online Chess Classes — Primary SEO Target` and `Glowing Gold King — Hero Section Image`) actually correct?**
  _`Indian FIDE Rated Coach — Core USP` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `fs`, `path`, `pages` to the rest of the system?**
  _44 weakly-connected nodes found - possible documentation gaps or missing edges._