// Preview image before uploading
function previewImage(event, previewId) {
    const reader = new FileReader();
    reader.onload = function() {
        const output = document.getElementById(previewId);
        output.src = reader.result;
        output.style.display = "block"; // Show image after loading
    };
    if (event.target.files[0]) {
        reader.readAsDataURL(event.target.files[0]);
    }
}

// Toggle password visibility
function togglePassword(id) {
    const passField = document.getElementById(id);
    if (passField.type === "password") {
        passField.type = "text";
    } else {
        passField.type = "password";
    }
}

// Simple form validation
function validateForm() {
    const image = document.querySelector('input[name="image"]').files.length;
    const password = document.querySelector('input[name="password"]').value.trim();
    const messageField = document.querySelector('input[name="message"]');
    const message = messageField ? messageField.value.trim() : "ok";

    if (!image || !password || !message) {
        alert("Please complete all fields before submitting.");
        return false;
    }
    return true;
}
