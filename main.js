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

  /* -------------------------------
     Form Submission Handler
  ------------------------------- */
  const form = document.getElementById('trial-class-form');
  if (form) {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      
      const btn = document.getElementById('form-submit-btn');
      const originalText = btn.textContent;
      btn.innerHTML = '<span class="spinner"></span> Booking...';
      btn.disabled = true;
      btn.style.opacity = '0.7';
      
      const formData = new FormData(form);
      try {
        const response = await fetch("https://formsubmit.co/ajax/teacherankushjain@gmail.com", {
          method: "POST",
          headers: { 
            'Accept': 'application/json'
          },
          body: formData
        });
        
        if (response.ok) {
          // Success State
          form.innerHTML = `
            <div class="success-message float-anim">
              <svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="var(--primary)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom: 1rem;">
                <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                <polyline points="22 4 12 14.01 9 11.01"></polyline>
              </svg>
              <h3 style="color: var(--primary); font-size: 1.8rem; margin-bottom: 0.5rem;">Booking Confirmed!</h3>
              <p style="color: var(--text-muted); font-size: 1.1rem;">Thank you for your interest. We will contact you shortly with the trial class details.</p>
            </div>
          `;
        } else {
          throw new Error('Network response was not ok');
        }
      } catch (error) {
        // Error State
        btn.innerHTML = originalText;
        btn.disabled = false;
        btn.style.opacity = '1';
        
        const existingError = form.querySelector('.error-message');
        if (!existingError) {
          const errorDiv = document.createElement('div');
          errorDiv.className = 'error-message';
          errorDiv.style.color = '#ef4444';
          errorDiv.style.marginTop = '1rem';
          errorDiv.style.padding = '1rem';
          errorDiv.style.background = 'rgba(239, 68, 68, 0.1)';
          errorDiv.style.borderRadius = '8px';
          errorDiv.style.border = '1px solid rgba(239, 68, 68, 0.3)';
          errorDiv.innerHTML = 'There was an error submitting your request. Please try again or email us directly at hello@thechesslifestyle.com.';
          form.appendChild(errorDiv);
        }
      }
    });
  }
});

// Ensure GA4 form_submit event fires on form submission
document.addEventListener("DOMContentLoaded", function() {
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function() {
            if (typeof gtag === 'function') {
                gtag('event', 'form_submit', {
                    'event_category': 'Lead Generation',
                    'event_label': window.location.pathname
                });
            }
        });
    });
});
