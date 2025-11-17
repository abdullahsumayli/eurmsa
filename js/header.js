// Header hide/show on scroll for mobile devices
let lastScrollTop = 0;
let scrollTimer = null;
const header = document.querySelector('header');
let isScrolling = false;

window.addEventListener('scroll', function() {
    // Only apply on mobile/tablet screens (768px and below)
    if (window.innerWidth > 768) {
        header.style.transform = 'translateY(0)';
        return;
    }

    // Clear previous timer
    if (scrollTimer !== null) {
        clearTimeout(scrollTimer);
    }

    const currentScroll = window.pageYOffset || document.documentElement.scrollTop;

    // Determine scroll direction
    if (currentScroll > lastScrollTop && currentScroll > 100) {
        // Scrolling down - hide header
        header.style.transform = 'translateY(-100%)';
        isScrolling = true;
    } else {
        // Scrolling up - show header
        header.style.transform = 'translateY(0)';
        isScrolling = false;
    }

    lastScrollTop = currentScroll <= 0 ? 0 : currentScroll;

    // Set a timeout to show header after scrolling stops
    scrollTimer = setTimeout(function() {
        if (isScrolling) {
            header.style.transform = 'translateY(0)';
            isScrolling = false;
        }
    }, 1500); // Show header 1.5 seconds after scrolling stops
}, false);

// Show header on resize if window becomes larger
window.addEventListener('resize', function() {
    if (window.innerWidth > 768) {
        header.style.transform = 'translateY(0)';
    }
});
