// Sidebar
var toggleSidebar = document.getElementById('toggleSidebar');
var sidebar = document.querySelector('.sidebar');

sidebar.addEventListener('click', function () {
    // Toggle the checkbox state
    toggleSidebar.checked = !toggleSidebar.checked;
});
