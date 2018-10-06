var sentence = "";      // Global variable which stores the complete sentence inputted upto this point
var last_word = "";     // Global variable which stores the last inputted word in the sentence

function key_pressed(event) {
    var pressed_key_code = event.keyCode;                                            // Get the Unicode value
    var pressed_key_char = String.fromCharCode(pressed_key_code).toLowerCase();      // Convert the value into a character

    if (pressed_key_code == 0 || pressed_key_code == 32) {             // If the pressed key is space
        var current_word = last_word;                                  // Save the last word into variable current_word

        sentence += pressed_key_char;                     // Add the current character to the end of sentence
        last_word = "";                                   // Reset last_word variable

        document.getElementById("next_words_list").innerHTML = current_word

        print_next_words(current_word);                   // Print the next words for the current word
    }
    else if (pressed_key_code == 8 || pressed_key_code == 46) {          // If backspace is pressed
        sentence = sentence.slice(0, -1);            // Remove the last character from sentence
        last_word = last_word.slice(0, -1);          // Remove the last character from last_word
    }
    else {
        sentence += pressed_key_char;            // Add the current character to the end of sentence
        last_word += pressed_key_char;           // Add the current character to the end of last word variable
    }
}

function print_next_words(current_word) {
    // Open up a WebSocket connection
    var connection = new WebSocket('ws://localhost:8080');

    // When the connection is open, send the current_word to the server
    connection.onopen = function(current_word) {
        connection.send(current_word);
    }

    // Handle any errors
    connection.onerror = function(error) {
        alert("WebSocket error: " + error);
    }

    // Receive the next_words list from the server
    connection.onmessage = function(msg) {
        document.getElementById("next_words_list").innerHTML = msg.data;
    }
}