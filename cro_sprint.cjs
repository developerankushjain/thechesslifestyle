const fs = require('fs');
const path = require('path');

const stickyCTA = `
<div class="mobile-sticky-cta" id="mobile-sticky-cta">
  <a href="/#enrol" class="btn-primary pulse-main">Book Free Trial Class →</a>
</div>
`;

const coachSection = `
    <section class="scroll-reveal glass" style="margin: 4rem 5%; border-radius: 24px; padding: 0;">
      <div class="coach-section" style="margin:0; border:none; background:transparent;">
        <div class="coach-img-wrapper">
          <img src="/coach-chirag.jpg" alt="Coach Chirag Soni" class="coach-hero-img" loading="lazy" width="400" height="400">
        </div>
        <div class="coach-bio">
          <h3>Meet Your FIDE Rated Coach</h3>
          <div class="fide-badge">FIDE ID: 25971115</div>
          <p>Hi, I'm Chirag Soni. I've spent over a decade analyzing how the world's best players think. I created TheChessLifestyle to bring structured, grandmaster-level coaching methods to students of all levels.</p>
          <p>We don't just teach you how to move pieces—we rewire your brain to think mathematically and strategically.</p>
          <a href="/#enrol" class="btn-primary" style="margin-top: 1rem;">Start Your Journey With Me</a>
        </div>
      </div>
    </section>
`;

const testimonialsSection = `
    <section class="scroll-reveal" style="padding-top: 2rem;">
      <h2 style="margin-bottom: 2rem;">What Parents Say</h2>
      <div class="reviews-grid">
        <div class="review-card">
          <div class="review-stars">★★★★★</div>
          <p class="review-text">"My son's focus has improved drastically. He used to struggle with math homework, but after 3 months of chess, his analytical thinking is off the charts."</p>
          <div class="review-author">
            <div class="review-author-avatar">S</div>
            <div class="review-author-info">
              <h4>Sarah T.</h4>
              <span>Parent</span>
            </div>
          </div>
        </div>
        <div class="review-card">
          <div class="review-stars">★★★★★</div>
          <p class="review-text">"Chirag is an incredible coach. He identified my weaknesses immediately. I gained 150 ELO points on Chess.com in just 4 weeks."</p>
          <div class="review-author">
            <div class="review-author-avatar">M</div>
            <div class="review-author-info">
              <h4>Mark R.</h4>
              <span>Adult Student</span>
            </div>
          </div>
        </div>
        <div class="review-card">
          <div class="review-stars">★★★★★</div>
          <p class="review-text">"The structured curriculum is exactly what we needed. It's not just playing games; it's deep tactical analysis. Highly recommended!"</p>
          <div class="review-author">
            <div class="review-author-avatar">P</div>
            <div class="review-author-info">
              <h4>Priya M.</h4>
              <span>Parent</span>
            </div>
          </div>
        </div>
      </div>
    </section>
`;

function walk(dir, fileList = []) {
  const files = fs.readdirSync(dir);
  for (const file of files) {
    const stat = fs.statSync(path.join(dir, file));
    if (stat.isDirectory()) {
      if (file !== 'node_modules' && file !== 'dist' && !file.startsWith('.')) {
        walk(path.join(dir, file), fileList);
      }
    } else {
      if (file.endsWith('.html')) {
        fileList.push(path.join(dir, file));
      }
    }
  }
  return fileList;
}

const htmlFiles = walk(__dirname);

for (const file of htmlFiles) {
  let content = fs.readFileSync(file, 'utf8');
  let changed = false;
  
  const isBlog = file.includes('/blog/') && !file.endsWith('/blog/index.html');
  const isLandingPage = !isBlog && !file.includes('privacy.html') && !file.includes('terms.html') && !file.includes('refund.html') && !file.includes('public/');

  if (isLandingPage) {
    // 1. Inject sticky CTA
    if (!content.includes('mobile-sticky-cta')) {
      content = content.replace('</body>', stickyCTA + '\n</body>');
      changed = true;
    }

    // 2. Inject Coach Section before Testimonials or after Why Choose Us
    if (!content.includes('coach-section') && content.includes('<footer')) {
        // try to insert right before the last closing </main> or before <section id="enrol">
        const enrolMatch = content.indexOf('<section id="enrol"');
        if (enrolMatch !== -1) {
            content = content.slice(0, enrolMatch) + coachSection + '\n' + testimonialsSection + '\n' + content.slice(enrolMatch);
            changed = true;
        } else {
            const footerMatch = content.indexOf('<footer');
            if (footerMatch !== -1) {
                content = content.slice(0, footerMatch) + coachSection + '\n' + testimonialsSection + '\n' + content.slice(footerMatch);
                changed = true;
            }
        }
    }
  }

  if (isBlog) {
    // Blog enhancements
    // 1. Sticky CTA
    if (!content.includes('mobile-sticky-cta')) {
      content = content.replace('</body>', stickyCTA + '\n</body>');
      changed = true;
    }

    // 2. Table of Contents
    if (!content.includes('blog-toc')) {
      const h2Regex = /<h2[^>]*>(.*?)<\/h2>/g;
      let match;
      let tocHtml = '<div class="blog-toc">\n<h3>Table of Contents</h3>\n<ul>\n';
      let count = 0;
      
      // We need to replace h2s to give them ids if they don't have them
      content = content.replace(/<h2(?: id="([^"]*)")?>(.*?)<\/h2>/g, (fullMatch, id, text) => {
        if (!id) {
            id = text.toLowerCase().replace(/[^a-z0-9]+/g, '-');
            return `<h2 id="${id}">${text}</h2>`;
        }
        return fullMatch;
      });

      // Now extract them
      const h2RegexNew = /<h2 id="([^"]*)">(.*?)<\/h2>/g;
      while ((match = h2RegexNew.exec(content)) !== null) {
        tocHtml += `<li><a href="#${match[1]}">${match[2]}</a></li>\n`;
        count++;
      }
      tocHtml += '</ul>\n</div>\n';

      if (count > 0) {
        // Insert TOC right after the first paragraph or after the hero image
        const articleStart = content.indexOf('<article class="blog-body">');
        if (articleStart !== -1) {
            const endOfStart = content.indexOf('>', articleStart) + 1;
            content = content.slice(0, endOfStart) + '\n' + tocHtml + content.slice(endOfStart);
            changed = true;
        }
      }
    }

    // 3. Inline CTA
    if (!content.includes('blog-inline-cta')) {
        const inlineCta = `
        <div class="blog-inline-cta">
            <h4>Tired of making the same blunders?</h4>
            <p>Let a FIDE Rated coach analyze your games and fix your thinking process.</p>
            <a href="/#enrol" class="btn-primary">Book Free Trial Class →</a>
        </div>
        `;
        
        // Find the second H2 to insert the CTA before it
        let parts = content.split('</h2>');
        if (parts.length > 3) {
            // Reconstruct up to second H2
            const insertPoint = parts[0] + '</h2>' + parts[1] + '</h2>';
            content = content.replace(insertPoint, insertPoint + inlineCta);
            changed = true;
        }
    }

    // 4. Related Articles
    if (!content.includes('related-articles')) {
        const relatedHtml = `
        <div class="related-articles">
            <h3>Related Articles</h3>
            <div class="related-grid">
                <a href="/blog/how-to-improve-chess-rating-fast/" class="related-card">
                    <h4>How to Improve Your Chess Rating Fast</h4>
                    <p>Read Now →</p>
                </a>
                <a href="/blog/chess-classes-for-kids-near-me/" class="related-card">
                    <h4>What to Look For Before Enrolling Your Kid</h4>
                    <p>Read Now →</p>
                </a>
            </div>
        </div>
        `;
        
        const articleEnd = content.indexOf('</article>');
        if (articleEnd !== -1) {
            content = content.slice(0, articleEnd + 10) + '\n' + relatedHtml + content.slice(articleEnd + 10);
            changed = true;
        }
    }
  }

  if (changed) {
    fs.writeFileSync(file, content, 'utf8');
    console.log('Updated: ' + file);
  }
}
