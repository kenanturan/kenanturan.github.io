

// Simple active link highlighter
document.addEventListener('DOMContentLoaded', () => {
  const currentPath = window.location.pathname;
  const links = document.querySelectorAll('.nav-link');

  links.forEach(link => {
    if (link.getAttribute('href') === currentPath || (currentPath === '/' && link.getAttribute('href') === '/index.html')) {
      link.classList.add('active');
    }
  });
});

console.log('Security Thought Platform initialized.');
