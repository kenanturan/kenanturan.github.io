
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
  // 7. Social Share Logic
  window.shareContent = function (platform) {
    const url = window.location.href;
    const title = document.title;
    const text = "Taktik Eğitim Akademisi Analysis: " + title;

    if (platform === 'whatsapp') {
      // WhatsApp Share
      const whatsappUrl = `https://api.whatsapp.com/send?text=${encodeURIComponent(text + ' ' + url)}`;
      window.open(whatsappUrl, '_blank');
    } else if (platform === 'instagram' || platform === 'share') {
      // Web Share API (Mobile Native Share)
      // This is the best way to share to Instagram Stories/DM on mobile
      if (navigator.share) {
        navigator.share({
          title: title,
          text: text,
          url: url
        }).catch((error) => console.log('Error sharing', error));
      } else {
        // Fallback: Copy to Clipboard (Desktop)
        navigator.clipboard.writeText(url).then(() => {
          alert('Bağlantı kopyalandı! (Link copied!)');
        }).catch(err => {
          console.error('Failed to copy: ', err);
          prompt("Copy this link:", url); // Ultimate fallback
        });
      }
    }
  };
});

console.log('Security Thought Platform initialized.');
