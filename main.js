
// Main JavaScript File

document.addEventListener('DOMContentLoaded', () => {
  // 1. Smooth Fade-in on Load (Handled by CSS animation on body)

  // 2. Active Link Highlighter
  const currentPath = window.location.pathname;
  const links = document.querySelectorAll('.nav-link');

  links.forEach(link => {
    // Reset active class first if needed, though mostly reliable server-side or static
    // Here we just add it if it matches
    if (link.getAttribute('href') === currentPath ||
      (currentPath === '/' && link.getAttribute('href') === 'index.html') ||
      (currentPath.endsWith('/') && link.getAttribute('href') === 'index.html')) {
      link.classList.add('active');
    }
  });

  // 3. Smooth Page Transition (Removed explicit fade-out delay for natural navigation)
  // Navigation is now handled natively by the browser, with CSS fade-in on the new page.

  // 4. Reveal Text on Scroll (Optional visual enhancement)
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
      }
    });
  });

  document.querySelectorAll('h1, h2, p').forEach((el) => {
    el.classList.add('reveal-text'); // Ensure CSS has this class if used, otherwise it does nothing harmlessly
    observer.observe(el);
  });
  // 5. Mobile Menu Toggle
  const menuToggle = document.getElementById('mobile-menu');
  const navLinks = document.querySelector('.nav-links');

  if (menuToggle && navLinks) {
    menuToggle.addEventListener('click', (e) => {
      e.stopPropagation(); // Prevent document click from immediately closing it
      menuToggle.classList.toggle('active');
      navLinks.classList.toggle('active');
    });

    // Close menu when clicking a link
    navLinks.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        menuToggle.classList.remove('active');
        navLinks.classList.remove('active');
      });
    });

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
      if (!navLinks.contains(e.target) && !menuToggle.contains(e.target)) {
        menuToggle.classList.remove('active');
        navLinks.classList.remove('active');
      }
    });
  }

  // 6. Smart Navbar (Hide on Scroll)
  let lastScrollY = window.scrollY;
  const navbar = document.querySelector('.navbar');

  window.addEventListener('scroll', () => {
    if (window.scrollY > lastScrollY && window.scrollY > 100) {
      // Scrolling Down
      navbar.classList.add('hidden');
    } else {
      // Scrolling Up
      navbar.classList.remove('hidden');
    }
    lastScrollY = window.scrollY;
  });
  // 7. Social Share Logic & Toast Notification
  function showToast(message, duration = 4000) {
    // Remove existing toast if present to prevent stacking
    const existingToast = document.querySelector('.toast-notification');
    if (existingToast) {
      existingToast.remove();
    }

    const toast = document.createElement('div');
    toast.className = 'toast-notification';
    toast.innerHTML = `
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="20 6 9 17 4 12"></polyline>
            </svg>
            <span>${message}</span>
        `;

    document.body.appendChild(toast);

    // Trigger animation
    setTimeout(() => toast.classList.add('show'), 10);

    // Remove after duration
    setTimeout(() => {
      toast.classList.remove('show');
      setTimeout(() => toast.remove(), 400); // Wait for fade out
    }, duration);
  }

  window.shareContent = function (platform) {
    const url = window.location.href;
    const lang = document.documentElement.lang || 'tr'; // Default to TR if not set, though it should be.

    // Get clean title by removing site name suffix if present (supports | and I separators)
    let rawTitle = document.title;
    let cleanTitle = rawTitle.replace(/\s*[|I]\s*Taktik Eğitim Akademisi.*/i, '').trim();

    // Construct localized text
    let prefix = (lang === 'tr') ? 'Analiz' : 'Analysis';
    let text = `${prefix}: ${cleanTitle} | Taktik Eğitim Akademisi`;

    if (platform === 'whatsapp') {
      // WhatsApp Share
      const whatsappUrl = `https://api.whatsapp.com/send?text=${encodeURIComponent(text + ' ' + url)}`;
      window.open(whatsappUrl, '_blank');
    } else if (platform === 'instagram') {
      // Instagram Strategy: Copy Link + Guide User
      navigator.clipboard.writeText(url).then(() => {
        showToast("Bağlantı kopyalandı! Hikayenize 'Bağlantı' etiketiyle ekleyebilirsiniz.");
      }).catch(err => {
        console.error('Copy failed', err);
        prompt("Bağlantıyı kopyalayın:", url);
      });
    } else {
      // Generic / Other
      if (navigator.share) {
        navigator.share({
          title: title,
          text: text,
          url: url
        }).catch((error) => console.log('Error sharing', error));
      } else {
        navigator.clipboard.writeText(url).then(() => {
          showToast("Bağlantı kopyalandı!");
        });
      }
    }
  };
});

console.log('Security Thought Platform initialized.');
