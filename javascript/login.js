document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const errorMessage = document.getElementById('errorMessage');

    // Sample credentials for demonstration
    const validUsername = 'user';
    const validPassword = 'password';

    if (username === validUsername && password === validPassword) {
        alert('Login successful!');
        errorMessage.textContent = '';
        // Redirect to another page or perform other actions
    } else {
        errorMessage.textContent = 'Invalid username or password';
    }


    function register() {
        window.location.href = "register.html"; // Replace "register.html" with your registration page URL
    }
});
