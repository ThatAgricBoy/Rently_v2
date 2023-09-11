// signup.js
document.addEventListener('DOMContentLoaded', function() {
    const passwordField = document.getElementById('password');
    const confirmPasswordField = document.getElementById('confirm-password');

    confirmPasswordField.addEventListener('input', function() {
        if (passwordField.value !== confirmPasswordField.value) {
            confirmPasswordField.setCustomValidity("Passwords don't match");
        } else {
            confirmPasswordField.setCustomValidity("");
        }
    });
});

document.querySelector('.search-box form').addEventListener('submit', function(event) {
        event.preventDefault();
        const location = document.querySelector('#location-input').value;
        window.location.href = '/templates/listings.html?location=' + encodeURIComponent(location);
    });
