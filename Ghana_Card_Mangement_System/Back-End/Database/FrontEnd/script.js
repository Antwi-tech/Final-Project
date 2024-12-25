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
*/


// function searchCard(event) {
//     event.preventDefault();

//     var lastName = document.querySelector(".search_input").value;

//     fetch(`http://127.0.0.1:5001/search_card/${lastName}`)
//         .then(response => response.json())
//         .then(data => {
//             const displayResults = document.getElementById("results");

//             if (data.error) {
//                 displayResults.innerHTML = `<p>${data.error}</p>`;
//             } else {
//                 displayResults.innerHTML = `
//                     <h2>Card Found</h2>
//                     <p>First Name: ${data.card_found.first_name}</p>
//                     <p>Last Name: ${data.card_found.last_name}</p>
//                     <p>ID Number: ${data.card_found.id_number}</p>
//                     <p>Middle Name: ${data.card_found.middle_name}</p>
//                     <p>Sex: ${data.card_found.sex}</p>
//                     <p>Citizenship: ${data.card_found.citizenship}</p>
//                     <p>${data.message}</p>
//                 `;
//             }

//         })
//         .catch(error => {
//             document.getElementById("results").innerHTML = `<p>Error: ${error}</p>`;
//         });
// }
document.addEventListener("DOMContentLoaded", () => {
    const searchInput = document.querySelector(".search_input");
    const resultsContainer = document.getElementById("results");

    searchInput.addEventListener("keypress", async (event) => {
        if (event.key === "Enter") {
            event.preventDefault(); // Prevent form submission
            var lastName = document.querySelector(".search_input").value;

            if (!lastName) {
                alert("Please enter a last name to search.");
                return;
            }

            try {
               
                const response = await fetch(`http://127.0.0.1:5001/search_card`);
                
                if (!response.ok) {
                    throw new Error(`Error: ${response.statusText}`);
                }

                const data = await response.json();

                // Check if a card was found
                if (data["Card Found"]) {
                    displayCardDetails(data["Card Found"]);
                } else {
                    resultsContainer.innerHTML = `<p>No card found for the given last name.</p>`;
                }
            } catch (error) {
                console.error("An error occurred:", error);
                resultsContainer.innerHTML = `<p>An error occurred while fetching data. Please try again.</p>`;
            }
        }
    });

    function displayCardDetails(card) {
        resultsContainer.innerHTML = `
            <div>
                <p>First Name:</p>
                <input type="text" value="${card.first_name}" readonly>
            </div>
            <div>
                <p>Last Name:</p>
                <input type="text" value="${card.last_name}" readonly>
            </div>
            <div>
                <p>Middle Name(s):</p>
                <input type="text" value="${card.middle_name}" readonly>
            </div>
            <div>
                <p>ID Number:</p>
                <input type="text" value="${card.id_number}" readonly>
            </div>
            <div>
                <p>Sex:</p>
                <input type="text" value="${card.sex}" readonly>
            </div>
            <div>
                <p>Citizenship:</p>
                <input type="text" value="${card.citizenship}" readonly>
            </div>
        `;
    }
});
