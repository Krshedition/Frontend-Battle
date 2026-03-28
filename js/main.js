/* ==========================================
   MITS GWALIOR - MAIN JS FILE
   Vanilla JS only. Zero dependencies.
   ========================================== */

document.addEventListener('DOMContentLoaded', function () {
  initHamburgerMenu();
  initNavbarScroll();
  initSmoothScroll();
  initParticleCanvas();
  initScrollReveal();
  initAcademicTabs();
  initAnnouncementFilter();
});

/* ============================================
   1. HAMBURGER MOBILE MENU
   ============================================ */
function initHamburgerMenu() {
  const hamburger = document.getElementById('hamburger');
  const navbarLinks = document.getElementById('navbar-links');
  if (!hamburger || !navbarLinks) return;

  if (!document.querySelector('.navbar__mobile-menu')) {
    const mobileMenu = document.createElement('div');
    mobileMenu.classList.add('navbar__mobile-menu');

    navbarLinks.querySelectorAll('a').forEach(function (link, index) {
      const clone = link.cloneNode(true);
      clone.style.transitionDelay = (index * 80) + 'ms';
      mobileMenu.appendChild(clone);
    });

    const cta = document.querySelector('.navbar__cta');
    if (cta) {
      const ctaClone = cta.cloneNode(true);
      ctaClone.style.display = 'inline-flex';
      mobileMenu.appendChild(ctaClone);
    }

    document.body.appendChild(mobileMenu);

    hamburger.addEventListener('click', function () {
      hamburger.classList.toggle('active');
      mobileMenu.classList.toggle('active');
      document.body.style.overflow = mobileMenu.classList.contains('active') ? 'hidden' : '';
    });

    mobileMenu.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        hamburger.classList.remove('active');
        mobileMenu.classList.remove('active');
        document.body.style.overflow = '';
      });
    });
  }
}

/* ============================================
   2. STICKY NAVBAR ON SCROLL
   ============================================ */
function initNavbarScroll() {
  const navbar = document.getElementById('navbar');
  if (!navbar) return;
  let ticking = false;

  window.addEventListener('scroll', function () {
    if (!ticking) {
      window.requestAnimationFrame(function () {
        if (window.scrollY > 80) {
          navbar.classList.add('navbar--scrolled');
        } else {
          navbar.classList.remove('navbar--scrolled');
        }
        ticking = false;
      });
      ticking = true;
    }
  });
}

/* ============================================
   3. SMOOTH SCROLL
   ============================================ */
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') {
        e.preventDefault();
        alert('This feature is coming soon!');
        return;
      }
      const targetEl = document.querySelector(targetId);
      if (targetEl) {
        e.preventDefault();
        const headerOffset = 80;
        const offsetPosition = targetEl.getBoundingClientRect().top + window.pageYOffset - headerOffset;
        window.scrollTo({ top: offsetPosition, behavior: 'smooth' });
      }
    });
  });
}

/* ============================================
   4. PARTICLE CONSTELLATION CANVAS
   ============================================ */
function initParticleCanvas() {
  const canvas = document.getElementById('hero-canvas');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  let width, height;
  let particles = [];
  const mouse = { x: null, y: null, radius: 200 };

  function Particle() {
    this.x = Math.random() * width;
    this.y = Math.random() * height;
    this.size = Math.random() * 2 + 1;
    this.baseX = this.x;
    this.baseY = this.y;
    this.density = (Math.random() * 20) + 1;
    this.vx = (Math.random() - 0.5) * 0.5;
    this.vy = (Math.random() - 0.5) * 0.5;
    this.opacity = Math.random() * 0.5 + 0.2;
  }

  Particle.prototype.draw = function () {
    ctx.fillStyle = 'rgba(255, 193, 7, ' + this.opacity + ')';
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
    ctx.closePath();
    ctx.fill();
  };

  Particle.prototype.update = function () {
    this.x += this.vx;
    this.y += this.vy;
    if (this.x < 0 || this.x > width) this.vx *= -1;
    if (this.y < 0 || this.y > height) this.vy *= -1;

    if (mouse.x != null) {
      const dx = mouse.x - this.x;
      const dy = mouse.y - this.y;
      const distance = Math.sqrt(dx * dx + dy * dy);
      if (distance < mouse.radius) {
        const force = (mouse.radius - distance) / mouse.radius;
        this.x -= (dx / distance) * force * this.density;
        this.y -= (dy / distance) * force * this.density;
      }
    }
    this.draw();
  };

  function resizeCanvas() {
    width = canvas.width = window.innerWidth;
    height = canvas.height = canvas.parentElement.offsetHeight;
    createParticles();
  }

  function createParticles() {
    particles = [];
    const count = window.innerWidth < 768 ? 40 : 120;
    for (let i = 0; i < count; i++) {
      particles.push(new Particle());
    }
  }

  function connectParticles() {
    for (let a = 0; a < particles.length; a++) {
      for (let b = a; b < particles.length; b++) {
        const dx = particles[a].x - particles[b].x;
        const dy = particles[a].y - particles[b].y;
        const dist = dx * dx + dy * dy;
        if (dist < 22500) {
          const opacity = (1 - dist / 22500) * 0.4;
          ctx.strokeStyle = 'rgba(211, 47, 47, ' + opacity + ')';
          ctx.lineWidth = 0.5;
          ctx.beginPath();
          ctx.moveTo(particles[a].x, particles[a].y);
          ctx.lineTo(particles[b].x, particles[b].y);
          ctx.stroke();
        }
      }
    }
  }

  function animate() {
    ctx.clearRect(0, 0, width, height);
    for (let i = 0; i < particles.length; i++) {
      particles[i].update();
    }
    connectParticles();
    requestAnimationFrame(animate);
  }

  window.addEventListener('resize', resizeCanvas);

  const heroSection = document.getElementById('hero');
  if (heroSection) {
    heroSection.addEventListener('mousemove', function (e) {
      const rect = canvas.getBoundingClientRect();
      mouse.x = e.clientX - rect.left;
      mouse.y = e.clientY - rect.top;
    });
    heroSection.addEventListener('mouseleave', function () {
      mouse.x = null;
      mouse.y = null;
    });
  }

  resizeCanvas();
  animate();
}

/* ============================================
   5. SCROLL-REVEAL + COUNTER TRIGGER
   ============================================ */
function initScrollReveal() {
  const revealEls = document.querySelectorAll('.reveal');

  const observer = new IntersectionObserver(function (entries, obs) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('reveal--visible');
        // Trigger counters if inside this element
        const counters = entry.target.querySelectorAll('.stat-counter');
        if (counters.length) runCounters(entry.target);
        // Also if the element itself is a counter wrapper
        if (entry.target.querySelector && entry.target.querySelector('.stat-counter')) {
          runCounters(entry.target);
        }
        obs.unobserve(entry.target);
      }
    });
  }, { root: null, threshold: 0.12 });

  revealEls.forEach(function (el) { observer.observe(el); });
}

function runCounters(container) {
  const counters = container.querySelectorAll('.stat-counter');
  const duration = 2000;
  counters.forEach(function (counter) {
    if (counter.classList.contains('counted')) return;
    counter.classList.add('counted');
    const target = +counter.getAttribute('data-target');
    if (isNaN(target)) return;
    let startTime = null;
    function step(currentTime) {
      if (!startTime) startTime = currentTime;
      const elapsed = currentTime - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const ease = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);
      counter.innerText = Math.floor(target * ease);
      if (progress < 1) {
        requestAnimationFrame(step);
      } else {
        counter.innerText = target;
      }
    }
    requestAnimationFrame(step);
  });
}

/* ============================================
   6. ACADEMIC TABS
   ============================================ */
function initAcademicTabs() {
  const tabs = document.querySelectorAll('.academics__tab');
  const panels = document.querySelectorAll('.academics__panel');
  if (!tabs.length || !panels.length) return;

  tabs.forEach(function (tab) {
    tab.addEventListener('click', function () {
      const target = tab.getAttribute('data-tab');

      // Update tabs
      tabs.forEach(function (t) { t.classList.remove('academics__tab--active'); });
      tab.classList.add('academics__tab--active');

      // Update panels
      panels.forEach(function (panel) {
        if (panel.getAttribute('data-panel') === target) {
          panel.classList.add('academics__panel--active');
        } else {
          panel.classList.remove('academics__panel--active');
        }
      });
    });
  });
}

/* ============================================
   7. ANNOUNCEMENT FILTER
   ============================================ */
function initAnnouncementFilter() {
  const filters = document.querySelectorAll('.ann-filter');
  const cards = document.querySelectorAll('.ann-card');
  if (!filters.length) return;

  filters.forEach(function (filter) {
    filter.addEventListener('click', function () {
      const selected = filter.getAttribute('data-filter');

      filters.forEach(function (f) { f.classList.remove('ann-filter--active'); });
      filter.classList.add('ann-filter--active');

      cards.forEach(function (card) {
        const cat = card.getAttribute('data-category');
        if (selected === 'all' || cat === selected) {
          card.classList.remove('ann-card--hidden');
        } else {
          card.classList.add('ann-card--hidden');
        }
      });
    });
  });
}
