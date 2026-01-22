function toggleExpertise(e) {
    if (e) e.preventDefault();

    const hiddenItems = document.querySelectorAll('.hidden-item');
    const trigger = document.getElementById('view-all-trigger');

    hiddenItems.forEach(item => {
        item.style.display = 'flex'; // Restore display:flex (dashboard-card has flex)
        // Add a slight animation class if desired
        item.style.animation = 'fadeIn 0.5s ease';
    });

    if (trigger) {
        trigger.style.display = 'none';
    }
}
