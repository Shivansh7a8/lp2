# Define a dictionary to store predefined responses
responses = {
    "hello": "Hello! How can I assist you today?",
    "help": "Sure, I'm here to help! What do you need assistance with?",
    "bye": "Goodbye! Have a great day!",
    "default": "I'm sorry, I didn't understand. Can you please rephrase your request?"
}

# Define a function to process user inputs and generate appropriate responses
def process_input(user_input):
    # Convert user input to lowercase for easier matching
    user_input = user_input.lower()

    # Check if user input matches any predefined responses
    if user_input in responses:
        return responses[user_input]
    else:
        return responses["default"]

# Main interaction loop
print("Welcome to the Customer Interaction Bot!")
print("How can I assist you today?")

while True:
    user_input = input("User: ")
    response = process_input(user_input)
    print("Bot: " + response)

    # Check if user wants to end the conversation
    if user_input.lower() == "bye":
        break
