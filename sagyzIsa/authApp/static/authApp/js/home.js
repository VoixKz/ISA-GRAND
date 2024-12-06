document.addEventListener('DOMContentLoaded', function() {
    const themeToggle = document.getElementById('themeToggle');
    const mainContent = document.getElementById('mainContent');
    const mainHeading = document.getElementById('mainHeading');

    themeToggle.addEventListener('click', function() {
        document.body.classList.toggle('dark-theme');
        mainContent.classList.toggle('dark-theme');
        mainHeading.classList.toggle('dark-theme');
    });
});