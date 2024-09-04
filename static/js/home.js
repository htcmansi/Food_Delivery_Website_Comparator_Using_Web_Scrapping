function openSignupModal() {
    var modal = document.getElementById('signupModal');
    modal.style.display = 'block';
}

function closeSignupModal() {
    var modal = document.getElementById('signupModal');
    modal.style.display = 'none';
}

// home.js

document.addEventListener('DOMContentLoaded', function () {
    var aboutUsDropdown = document.getElementById('aboutUsDropdown');

    // Function to toggle the dropdown
    function toggleDropdown() {
        aboutUsDropdown.classList.toggle('show-dropdown');
    }

    // Add click event listener to the "About Us" anchor
    aboutUsDropdown.addEventListener('click', toggleDropdown);

    // Close the dropdown if the user clicks outside of it
    window.onclick = function (event) {
        if (!event.target.matches('.nav-link')) {
            var dropdowns = document.getElementsByClassName('dropdown-content');
            for (var i = 0; i < dropdowns.length; i++) {
                var openDropdown = dropdowns[i];
                if (openDropdown.classList.contains('show-dropdown')) {
                    openDropdown.classList.remove('show-dropdown');
                }
            }
        }
    };
});

// Add this function to handle clicking outside of the dropdown
document.addEventListener('click', function (event) {
    var aboutUsDropdown = document.getElementById('aboutUsDropdown');
    if (!event.target.closest('.dropdown') && aboutUsDropdown.classList.contains('show-dropdown')) {
        aboutUsDropdown.classList.remove('show-dropdown');
    }
});
//  search icon has a class 'search-icon'
document.querySelector('.search-icon').addEventListener('click', function() {
    window.location.href = 'login_page.html'; // Redirect to the search page
});


