/*
const form = document.getElementById("form");
const popup = document.getElementById("popup");

function validateForm() {
    // Get all input fields
    const inputs = form.querySelectorAll("input[required], textarea[required], select[required]");
    let isValid = true;

    // Check if all required fields are filled
    inputs.forEach(input => {
        if (!input.value.trim()) {
            isValid = false;
            input.classList.add("error"); // Add an error class if needed
        } else {
            input.classList.remove("error"); // Remove error class if fixed
        }
    });

    return isValid;
}

function openPopup() {
    if (validateForm()) {
        // Open the popup
        popup.classList.add("open-popup");
        form.reset(); // Reset the form fields
        submitFormData(); // Call function to send form data via AJAX
    } else {
        alert("Please fill all required fields before submitting.");
    }
}

function closePopup() {
    popup.classList.remove("open-popup");
}

// Function to submit form data via AJAX
function submitFormData() {
    const formData = new FormData(form);  // Create a FormData object with form data

    // Send the form data via AJAX to the Flask backend
    fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())  // Parse the JSON response from Flask
    .then(data => {
        // Handle success
        if (data.message) {
            alert(data.message);  // Show success message
            document.getElementById("popup").style.display = "block";  // Show the popup
        }
    })
    .catch(error => {
        // Handle error
        console.error("Error:", error);
    });
}

// Attach the event listener
form.addEventListener("submit", (e) => {
    e.preventDefault(); // Prevent form submission
    openPopup(); // Open popup if validation passes
});
*/

const form = document.getElementById("form");
const popup = document.getElementById("popup");

function validateForm() {
    // Get all input fields
    const inputs = form.querySelectorAll("input[required], textarea[required], select[required]");
    let isValid = true;

    // Check if all required fields are filled
    inputs.forEach(input => {
        if (!input.value.trim()) {
            isValid = false;
            input.classList.add("error"); // Add an error class if needed
        } else {
            input.classList.remove("error"); // Remove error class if fixed
        }
    });

    return isValid;
}

function openPopup() {
    popup.classList.add("open-popup"); // Show the popup
}

function closePopup() {
    popup.classList.remove("open-popup"); // Close the popup
}

// AJAX call to submit the form data using Fetch
function submitFormData() {
    if (!validateForm()) {
        alert("Please fill all required fields before submitting.");
        return; // Prevent submission if form is not valid
    }

    const formData = new FormData(form);  // Collect form data using FormData

    // Send the form data via AJAX to the Flask backend
    fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        body: formData // Automatically sets the correct content type
    })
    .then(response => response.json())  // Parse the JSON response from Flask
    .then(data => {
        // Handle success
        if (data.message) {
            openPopup();  // Show the popup if data is successfully saved
            form.reset(); // Reset the form fields after submission
        }
    })
    .catch(error => {
        // Handle error
        console.error("Error:", error);
    });
}

// Attach the event listener for form submission
form.addEventListener("submit", (e) => {
    e.preventDefault(); // Prevent the form from submitting the traditional way
    submitFormData();   // Trigger the AJAX submission
});
