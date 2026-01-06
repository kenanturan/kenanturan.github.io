
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
    menuToggle.addEventListener('click', () => {
      menuToggle.classList.toggle('active');
      navLinks.classList.toggle('active');
    });
  }
});

console.log('Security Thought Platform initialized.');
