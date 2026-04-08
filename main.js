document.addEventListener('DOMContentLoaded', () => {
  /* -------------------------------
     Mobile Menu Toggle
  ------------------------------- */
  const toggleBtn = document.querySelector('.mobile-menu-toggle');
  const navLinks = document.querySelector('.nav-links');

  toggleBtn.addEventListener('click', () => {
    navLinks.classList.toggle('active');
  });

  navLinks.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      navLinks.classList.remove('active');
    });
  });

  /* -------------------------------
     Scroll Reveal & Stagger
  ------------------------------- */
  const scrollElements = document.querySelectorAll('.scroll-reveal');
  const revealOptions = { root: null, rootMargin: '0px', threshold: 0.15 };

  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, revealOptions);

  scrollElements.forEach(el => revealObserver.observe(el));

  /* -------------------------------
     Cursor Glow Tracker
  ------------------------------- */
  const glowTracker = document.getElementById('cursor-glow');
  document.addEventListener('mousemove', (e) => {
    if (window.innerWidth > 768) {
      glowTracker.style.left = `${e.clientX}px`;
      glowTracker.style.top = `${e.clientY}px`;
    }
  });

  /* -------------------------------
     3D Interactive Card Tilt WOW Effect
  ------------------------------- */
  const tiltCards = document.querySelectorAll('.tilt-card');
  
  tiltCards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;

      // Calculate tilt degrees (max 10 degrees)
      const rotateX = ((y - centerY) / centerY) * -10;
      const rotateY = ((x - centerX) / centerX) * 10;

      card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
    });

    card.addEventListener('mouseleave', () => {
      card.style.transform = `perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)`;
      card.style.transition = 'transform 0.5s cubic-bezier(0.2, 0.8, 0.2, 1)';
    });

    card.addEventListener('mouseenter', () => {
      card.style.transition = 'none';
    });
  });

  /* -------------------------------
     Parallax Background SVGs
  ------------------------------- */
  const floaters = document.querySelectorAll('.svg-floater');
  window.addEventListener('scroll', () => {
    const scrollY = window.pageYOffset;
    floaters.forEach(floater => {
      const speed = parseFloat(floater.getAttribute('data-speed'));
      floater.style.transform = `translateY(${scrollY * speed * 0.15}px)`;
    });
  });
});
