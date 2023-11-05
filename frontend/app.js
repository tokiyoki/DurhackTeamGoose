function generateGraph() {
    // Assuming you have the select element with an ID or another way to select it
    var selectElement = document.getElementById("metricDisplayedInput"); // Replace "yourSelectId" with the actual ID

    // Get the selected value
    var selectedValue_data_type = selectElement.value;

    // Assuming you have the radio button elements with the same name attribute
    var checkboxButtons = document.getElementsByName("price");

    // Initialize a variable to store the selected value
    var selectedValue_price = ["","",""];

    // Loop through the radio buttons to find the selected one
    for (var i = 0; i < checkboxButtons.length; i++) {
        if (checkboxButtons[i].checked) {
            selectedValue_price[i] = checkboxButtons[i].value;
        }
    }
    // Assuming you have the radio button elements with the same name attribute
    var radioButtons = document.getElementsByName("time");

    // Initialize a variable to store the selected value
    var selectedValue_time;

    // Loop through the radio buttons to find the selected one
    for (var i = 0; i < radioButtons.length; i++) {
        if (radioButtons[i].checked) {
            selectedValue_time = radioButtons[i].value;
            break; // Exit the loop once a checked radio button is found
        }
    }

    const payload = { data_type: selectedValue_data_type, price: selectedValue_price, time: selectedValue_time };

    // Convert the payload to a query string
    const queryString = Object.keys(payload)
        .map(key => encodeURIComponent(key) + '=' + encodeURIComponent(payload[key]))
        .join('&');

    console.log(queryString);

    // Make a GET request to the endpoint
    fetch('http://127.0.0.1:5000/api/endpoint?' + queryString)
        .then(response => {
            if (response.ok) {
                return response.blob(); // Get the image data as a blob
            }
            throw new Error('Network response was not ok.');
        })
        .then(blob => {
            const imageURL = URL.createObjectURL(blob);
            const mainGraphImage = document.getElementById('mainGraph');

            // Replace the image source with the received image
            mainGraphImage.src = imageURL;
        })
        .catch(error => {
            console.error('Error:', error);
        });
}
