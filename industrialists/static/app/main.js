// Sidebar
var toggleSidebar = document.getElementById('toggleSidebar');
var sidebar = document.querySelector('.sidebar');
var languageSwitcher = document.getElementById('language');

sidebar.addEventListener('click', function (event) {
    // Check if the clicked element is the language switcher or its dropdown
    if (
        event.target === languageSwitcher ||
        event.target.closest('.switcher-language')
    ) {
        // Stop event propagation
        event.stopPropagation();
    } else {
        // Toggle the checkbox state
        toggleSidebar.checked = !toggleSidebar.checked;
    }
});

// Close the sidebar when clicking outside of it
document.addEventListener('click', function (event) {
    if (!event.target.closest('.sidebar') && toggleSidebar.checked) {
        toggleSidebar.checked = false;
    }
});



const gallerySlider = new Swiper(".swiper.is-gallery", {
    loop: true,
    slidesPerView: 2,
    centeredSlides: true,
    speed: 300,
    grabCursor: true,
    parallax: true
});

document.addEventListener('DOMContentLoaded', function () {
    var swiper = new Swiper('.swiper-container', {
        direction: 'horizontal',
        slidesPerView: 'auto',
        spaceBetween: 10,
        freeMode: true,
        scrollbar: {
            el: '.swiper-scrollbar',
            hide: false,
        },
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
    });
});

