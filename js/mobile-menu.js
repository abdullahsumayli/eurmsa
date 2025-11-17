// Mobile Sidebar Menu Functionality
document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuToggle = document.getElementById('mobile-menu-toggle');
    const mobileSidebar = document.getElementById('mobile-sidebar');
    const sidebarClose = document.getElementById('sidebar-close');
    const body = document.body;

    // Check if elements exist
    if (!mobileSidebar) {
        console.error('Mobile sidebar not found!');
        return;
    }

    // Create overlay element
    const overlay = document.createElement('div');
    overlay.className = 'sidebar-overlay';
    body.appendChild(overlay);

    // Function to open sidebar
    function openSidebar() {
        mobileSidebar.classList.add('active');
        overlay.classList.add('active');
        body.style.overflow = 'hidden'; // Prevent body scroll when sidebar is open
    }

    // Function to close sidebar
    function closeSidebar() {
        mobileSidebar.classList.remove('active');
        overlay.classList.remove('active');
        body.style.overflow = ''; // Restore body scroll
    }

    // Open sidebar when hamburger button is clicked
    if (mobileMenuToggle) {
        mobileMenuToggle.addEventListener('click', openSidebar);
    }

    // Close sidebar when close button is clicked
    if (sidebarClose) {
        sidebarClose.addEventListener('click', closeSidebar);
    }

    // Close sidebar when overlay is clicked
    overlay.addEventListener('click', closeSidebar);

    // Close sidebar when a navigation link is clicked (allow navigation to happen)
    const sidebarLinks = mobileSidebar.querySelectorAll('.sidebar-nav a');
    sidebarLinks.forEach(link => {
        link.addEventListener('click', function() {
            // Just close the sidebar, don't prevent the link from working
            setTimeout(closeSidebar, 100);
        });
    });

    // Close sidebar on window resize if screen becomes larger
    window.addEventListener('resize', function() {
        if (window.innerWidth > 768) {
            closeSidebar();
        }
    });

    // Handle theme toggle in sidebar
    const themeToggleMobile = document.getElementById('theme-toggle-mobile');
    if (themeToggleMobile) {
        themeToggleMobile.addEventListener('click', function() {
            const html = document.documentElement;
            const theme = html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
            html.setAttribute('data-theme', theme);
            localStorage.setItem('theme', theme);
        });
    }
});
