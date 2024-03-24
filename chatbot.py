import random

# Dictionary containing predefined questions and answers
qa_pairs = {
    "Hello": ["Hello! How can I assist you?", "Hi there! How can I help you?"],
    "What is your name?": ["My name is ChatBot.", "You can call me ChatBot."],
    "How are you?": ["I'm doing well, thank you!", "I'm fine, thanks for asking."],
    "What can you do?": ["I can answer your questions.", "I can assist you with various queries."],
    "Who created you?": ["I was created by crazynetweb.", "My creators prefer to remain anonymous."],
    "Goodbye": ["Goodbye!", "See you later!", "Bye!"]
}

# Function to generate a response to the user's input from QnA
def generate_response(user_input):
    if user_input in qa_pairs:
        # If the question is predefined, randomly select and return an answer to the user
        return random.choice(qa_pairs[user_input])
    else:
        # If the question is not predefined, return a default response to the user
        return "I'm sorry, I don't understand that question."

# Main loop for interacting
while True:
    user_input = input("You: ").strip().capitalize()

    if user_input.lower() == 'exit':
        print("ChatBot: Goodbye!")
        break  # Exit the loop if the user wants to quit

    response = generate_response(user_input)
    print("ChatBot:", response)
