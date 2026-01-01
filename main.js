
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

  // 3. Smooth Page Transition (Fade-out on Link Click)
  const anchors = document.querySelectorAll('a');

  anchors.forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const href = this.getAttribute('href');
      const target = this.getAttribute('target');

      // Check if it's an internal link that we should animate
      // Exclude: anchors (#), mailto, tel, and new tab targets (_blank)
      if (href &&
        !href.startsWith('#') &&
        !href.startsWith('mailto:') &&
        !href.startsWith('tel:') &&
        target !== '_blank') {

        e.preventDefault(); // Stop immediate navigation

        // Add fade-out class to body
        document.body.classList.add('fade-out');

        // Wait for animation to finish (600ms matches CSS transition)
        setTimeout(() => {
          window.location.href = href;
        }, 600);
      }
    });
  });

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
});

console.log('Security Thought Platform initialized.');
