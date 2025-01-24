function validateForm(event) {
    const username = document.getElementById("username").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();

    // Basic validation
    if (username === "") {
        alert("Username is required.");
        event.preventDefault(); // Prevent form submission
        return false;
    }
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        alert("Please enter a valid email address.");
        event.preventDefault();
        return false;
    }
    if (password.length < 6) {
        alert("Password must be at least 6 characters long.");
        event.preventDefault();
        return false;
    }

    return true; // Form is valid, allow submission
}