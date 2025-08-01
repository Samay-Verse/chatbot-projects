// Wait for the DOM to be fully loaded before running the script
document.addEventListener('DOMContentLoaded', () => {

    // Get references to the HTML elements
    const chatBox = document.getElementById('chat-box');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');

    // Store the conversation history. This will be sent with each request.
    // We start with the initial bot message from the HTML for context.
    const messageHistory = [
        {"role": "assistant", "content": "Hey! I'm your new best friend. What's up? How can I make your day better? ✨"}
    ];

    // Helper function to create a new chat message element
    function createMessageElement(text, isUser) {
        // Create the main container div for the message
        const messageDiv = document.createElement('div');
        messageDiv.className = `flex ${isUser ? 'justify-end' : 'justify-start'}`;

        // Create the inner message bubble div
        const bubbleDiv = document.createElement('div');
        bubbleDiv.className = `p-4 rounded-xl max-w-[85%] shadow-sm ${isUser ? 'bg-emerald-100 text-gray-900' : 'bg-gray-100 text-gray-800'}`;
        bubbleDiv.textContent = text;
        
        // Append the bubble to the main container
        messageDiv.appendChild(bubbleDiv);
        
        // Append the new message to the chat box
        chatBox.appendChild(messageDiv);
        
        // Automatically scroll to the bottom to show the latest message
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    // Function to handle sending a message
    async function sendMessage() {
        const userMessage = userInput.value.trim();
        if (!userMessage) {
            return;
        }

        // Add the user's message to the history and display it
        messageHistory.push({"role": "user", "content": userMessage});
        createMessageElement(userMessage, true);
        
        // Clear the input field and disable the button
        userInput.value = '';
        sendButton.disabled = true;

        // Display a "typing" indicator
        const typingIndicator = document.createElement('div');
        typingIndicator.id = 'typing-indicator';
        typingIndicator.className = 'flex justify-start';
        typingIndicator.innerHTML = `
            <div class="p-4 rounded-xl max-w-[85%] bg-gray-100 text-gray-800 shadow-sm animate-pulse">
                <span class="inline-block w-2 h-2 bg-gray-400 rounded-full mx-0.5"></span>
                <span class="inline-block w-2 h-2 bg-gray-400 rounded-full mx-0.5"></span>
                <span class="inline-block w-2 h-2 bg-gray-400 rounded-full mx-0.5"></span>
            </div>
        `;
        chatBox.appendChild(typingIndicator);
        chatBox.scrollTop = chatBox.scrollHeight;

        try {
            // Make an asynchronous API call to the FastAPI backend
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ messages: messageHistory }),
            });
            
            // Check if the response was successful
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            // Parse the JSON response
            const data = await response.json();
            const botResponse = data.response;

            // Add the bot's response to the history and display it
            messageHistory.push({"role": "assistant", "content": botResponse});
            
            // Remove the typing indicator before showing the response
            chatBox.removeChild(typingIndicator);
            createMessageElement(botResponse, false);

        } catch (error) {
            console.error('Error fetching chat response:', error);
            // Display an error message to the user
            chatBox.removeChild(typingIndicator);
            createMessageElement("Oops! I'm having trouble connecting right now. Please try again later.", false);
        } finally {
            // Re-enable the send button
            sendButton.disabled = false;
            userInput.focus(); // Keep the input field focused for easy typing
        }
    }

    // Event listener for the send button
    sendButton.addEventListener('click', sendMessage);

    // Event listener for the Enter key on the input field
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    // Focus on the input field when the page loads
    userInput.focus();
});
