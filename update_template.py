"""
Script to update all remaining HTML pages with mobile sidebar menu
"""
import os

# List of files to update (excluding index.html and about.html which are already done)
arabic_files = [
    'services.html',
    'contact.html',
    'expo-registration.html',
    'thanks.html'
]

english_files = [
    'index-en.html',
    'about-en.html',
    'services-en.html',
    'contact-en.html',
    'expo-registration-en.html',
    'thanks-en.html'
]

# Templates for Arabic and English pages
arabic_mobile_header = '''        <!-- Mobile Menu Toggle Button -->
        <button class="mobile-menu-toggle" id="mobile-menu-toggle" aria-label="فتح القائمة">
            <span></span>
            <span></span>
            <span></span>
        </button>

        <!-- Mobile Sidebar Menu -->
        <div class="mobile-sidebar" id="mobile-sidebar">
            <div class="sidebar-header">
                <img src="images/logo-eurm.png" alt="EURM Logo" class="sidebar-logo">
                <button class="sidebar-close" id="sidebar-close" aria-label="إغلاق القائمة">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <line x1="18" y1="6" x2="6" y2="18"></line>
                        <line x1="6" y1="6" x2="18" y2="18"></line>
                    </svg>
                </button>
            </div>
            <nav class="sidebar-nav">
                <ul>
                    <li><a href="index.html">الرئيسية</a></li>
                    <li><a href="about.html">من نحن</a></li>
                    <li><a href="services.html">الخدمات</a></li>
                    <li><a href="expo-registration.html" class="nav-cta">حجز مساحة المعرض</a></li>
                    <li><a href="contact.html">تواصل معنا</a></li>
                    <li><a href="{{LANG_LINK}}" class="lang-switch">English</a></li>
                    <li class="theme-toggle-item">
                        <button id="theme-toggle-mobile" class="theme-toggle" aria-label="تبديل الوضع">
                            <svg class="sun-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <circle cx="12" cy="12" r="5"></circle>
                                <line x1="12" y1="1" x2="12" y2="3"></line>
                                <line x1="12" y1="21" x2="12" y2="23"></line>
                                <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
                                <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
                                <line x1="1" y1="12" x2="3" y2="12"></line>
                                <line x1="21" y1="12" x2="23" y2="12"></line>
                                <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
                                <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
                            </svg>
                            <svg class="moon-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
                            </svg>
                            <span>تبديل الوضع</span>
                        </button>
                    </li>
                </ul>
            </nav>
        </div>

        <!-- Desktop Navigation (hidden on mobile) -->
        <nav class="desktop-nav">'''

english_mobile_header = '''        <!-- Mobile Menu Toggle Button -->
        <button class="mobile-menu-toggle" id="mobile-menu-toggle" aria-label="Open menu">
            <span></span>
            <span></span>
            <span></span>
        </button>

        <!-- Mobile Sidebar Menu -->
        <div class="mobile-sidebar" id="mobile-sidebar">
            <div class="sidebar-header">
                <img src="images/logo-eurm.png" alt="EURM Logo" class="sidebar-logo">
                <button class="sidebar-close" id="sidebar-close" aria-label="Close menu">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <line x1="18" y1="6" x2="6" y2="18"></line>
                        <line x1="6" y1="6" x2="18" y2="18"></line>
                    </svg>
                </button>
            </div>
            <nav class="sidebar-nav">
                <ul>
                    <li><a href="index-en.html">Home</a></li>
                    <li><a href="about-en.html">About</a></li>
                    <li><a href="services-en.html">Services</a></li>
                    <li><a href="expo-registration-en.html" class="nav-cta">Book Exhibition Space</a></li>
                    <li><a href="contact-en.html">Contact</a></li>
                    <li><a href="{{LANG_LINK}}" class="lang-switch">العربية</a></li>
                    <li class="theme-toggle-item">
                        <button id="theme-toggle-mobile" class="theme-toggle" aria-label="Toggle theme">
                            <svg class="sun-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <circle cx="12" cy="12" r="5"></circle>
                                <line x1="12" y1="1" x2="12" y2="3"></line>
                                <line x1="12" y1="21" x2="12" y2="23"></line>
                                <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
                                <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
                                <line x1="1" y1="12" x2="3" y2="12"></line>
                                <line x1="21" y1="12" x2="23" y2="12"></line>
                                <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
                                <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
                            </svg>
                            <svg class="moon-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
                            </svg>
                            <span>Toggle Theme</span>
                        </button>
                    </li>
                </ul>
            </nav>
        </div>

        <!-- Desktop Navigation (hidden on mobile) -->
        <nav class="desktop-nav">'''

print("This script shows the template structure for updating HTML files.")
print("Use VS Code's find/replace or manual editing to apply these templates.")
print("\nFiles to update:")
print("Arabic:", arabic_files)
print("English:", english_files)
