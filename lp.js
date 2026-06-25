// Shared landing page utilities
// FAQ accordion
document.querySelectorAll(".faq-question").forEach((btn) => {
  btn.addEventListener("click", () => {
    const item = btn.closest(".faq-item");
    const isOpen = item.classList.contains("open");
    document
      .querySelectorAll(".faq-item")
      .forEach((i) => i.classList.remove("open"));
    if (!isOpen) item.classList.add("open");
  });
});

// Scroll reveal
const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) e.target.classList.add("visible");
    });
  },
  { threshold: 0.1, rootMargin: "0px 0px -60px 0px" },
);
document
  .querySelectorAll(".scroll-reveal")
  .forEach((el) => observer.observe(el));

// Mouse glow tracker
const glow = document.getElementById("cursor-glow");
if (glow) {
  document.addEventListener("mousemove", (e) => {
    glow.style.left = e.clientX + "px";
    glow.style.top = e.clientY + "px";
  });
}

// Mobile nav
const toggle = document.querySelector(".mobile-menu-toggle");
const navLinks = document.querySelector(".nav-links");
if (toggle && navLinks) {
  toggle.addEventListener("click", () => navLinks.classList.toggle("active"));
}

// Ensure GA4 form_submit event fires on form submission
document.addEventListener("DOMContentLoaded", function () {
  const forms = document.querySelectorAll("form");
  forms.forEach((form) => {
    form.addEventListener("submit", function () {
      if (typeof gtag === "function") {
        gtag("event", "form_submit", {
          event_category: "Lead Generation",
          event_label: window.location.pathname,
        });
      }
    });
  });
});

// ----------------------------------------------------
// UX Psychology Implementations
// ----------------------------------------------------

document.addEventListener("DOMContentLoaded", () => {
  // 1. Social Proof Toasts
  const toast = document.getElementById("booking-toast");
  const toastText = document.getElementById("toast-text");

  if (toast && toastText) {
    const locations = [
      "Chicago",
      "San Jose",
      "London",
      "Toronto",
      "Sydney",
      "New York",
      "Dubai",
      "Houston",
      "Dallas",
      "Birmingham",
      "Melbourne",
    ];
    const actions = [
      "booked a free trial",
      "just enrolled",
      "started learning chess",
    ];

    // Show toast occasionally (random interval between 15-45 seconds)
    setTimeout(showRandomToast, 5000 + Math.random() * 10000);

    function showRandomToast() {
      const loc = locations[Math.floor(Math.random() * locations.length)];
      const act = actions[Math.floor(Math.random() * actions.length)];
      toastText.textContent = `A student from ${loc} ${act}.`;

      toast.classList.add("show");

      // Hide after 5 seconds
      setTimeout(() => {
        toast.classList.remove("show");
        // Schedule next one
        setTimeout(showRandomToast, 20000 + Math.random() * 30000);
      }, 5000);
    }
  }

  // 2. Exit Intent Popup
  const exitModal = document.getElementById("exit-modal");
  const closeModalBtn = document.querySelector(".close-modal");
  let exitIntentTriggered = false;

  if (exitModal) {
    // Desktop exit intent
    document.addEventListener("mouseleave", (e) => {
      if (e.clientY < 10 && !exitIntentTriggered) {
        // Check session storage so we don't annoy them if they dismissed it
        if (!sessionStorage.getItem("exitModalDismissed")) {
          exitModal.classList.add("show");
          exitIntentTriggered = true;
        }
      }
    });

    // Close logic
    if (closeModalBtn) {
      closeModalBtn.addEventListener("click", () => {
        exitModal.classList.remove("show");
        sessionStorage.setItem("exitModalDismissed", "true");
      });
    }

    // Close on outside click
    exitModal.addEventListener("click", (e) => {
      if (e.target === exitModal) {
        exitModal.classList.remove("show");
        sessionStorage.setItem("exitModalDismissed", "true");
      }
    });
  }

  // 3. Multi-step Quiz Form Conversion for main footer form
  const mainForms = document.querySelectorAll(".enrol-form:not(.mini-form)");

  mainForms.forEach((form) => {
    // Only convert if it has more than 3 form-groups
    const formGroups = Array.from(form.querySelectorAll(".form-group"));
    if (formGroups.length < 4) return;

    // Hide original submit button initially
    const submitBtn = form.querySelector('button[type="submit"], .submit-btn');
    if (submitBtn) submitBtn.style.display = "none";

    // Group them into 3 logical steps
    const step1Groups = formGroups.slice(0, Math.ceil(formGroups.length / 3));
    const step2Groups = formGroups.slice(
      Math.ceil(formGroups.length / 3),
      Math.ceil((formGroups.length * 2) / 3),
    );
    const step3Groups = formGroups.slice(
      Math.ceil((formGroups.length * 2) / 3),
    );

    const steps = [step1Groups, step2Groups, step3Groups];
    let currentStep = 0;

    // Create step indicator
    const indicatorDiv = document.createElement("div");
    indicatorDiv.className = "step-indicator";
    steps.forEach((_, i) => {
      const dot = document.createElement("div");
      dot.className = `step-dot ${i === 0 ? "active" : ""}`;
      indicatorDiv.appendChild(dot);
    });
    form.insertBefore(indicatorDiv, formGroups[0]);

    // Create navigation buttons container
    const navContainer = document.createElement("div");
    navContainer.className = "step-nav-btns";

    const prevBtn = document.createElement("button");
    prevBtn.type = "button";
    prevBtn.className = "btn-secondary";
    prevBtn.textContent = "Back";
    prevBtn.style.display = "none"; // Hidden on step 1

    const nextBtn = document.createElement("button");
    nextBtn.type = "button";
    nextBtn.className = "btn-primary btn-next pulse-main";
    nextBtn.textContent = "Next Step";

    navContainer.appendChild(prevBtn);
    navContainer.appendChild(nextBtn);
    form.appendChild(navContainer);

    // Wrapping groups
    steps.forEach((groupSet, index) => {
      const stepWrapper = document.createElement("div");
      stepWrapper.className = `form-step ${index === 0 ? "active" : ""}`;
      stepWrapper.dataset.step = index;

      // Insert wrapper before first group in this set
      form.insertBefore(stepWrapper, groupSet[0]);

      // Move groups into wrapper
      groupSet.forEach((g) => stepWrapper.appendChild(g));
    });

    // Navigation logic
    function updateSteps() {
      // Update DOM classes
      form.querySelectorAll(".form-step").forEach((s, i) => {
        s.classList.toggle("active", i === currentStep);
      });
      form.querySelectorAll(".step-dot").forEach((d, i) => {
        d.classList.toggle("active", i === currentStep);
      });

      // Update buttons
      prevBtn.style.display = currentStep > 0 ? "block" : "none";

      if (currentStep === steps.length - 1) {
        nextBtn.style.display = "none";
        if (submitBtn) {
          submitBtn.style.display = "block";
          submitBtn.style.width = "100%";
          // Move submit button to nav container
          navContainer.appendChild(submitBtn);
        }
      } else {
        nextBtn.style.display = "block";
        if (submitBtn) submitBtn.style.display = "none";
      }
    }

    nextBtn.addEventListener("click", () => {
      // Basic HTML5 validation for current step
      const currentStepEl = form.querySelector(
        `.form-step[data-step="${currentStep}"]`,
      );
      const inputs = currentStepEl.querySelectorAll(
        "input[required], select[required], textarea[required]",
      );
      let allValid = true;

      inputs.forEach((input) => {
        if (!input.checkValidity()) {
          input.reportValidity();
          allValid = false;
        }
      });

      if (allValid && currentStep < steps.length - 1) {
        currentStep++;
        updateSteps();
      }
    });

    prevBtn.addEventListener("click", () => {
      if (currentStep > 0) {
        currentStep--;
        updateSteps();
      }
    });
  });
});
