def chatbot():
    print("Hello! I'm here to assist you. Type 'exit' to end the conversation.")
    
    while True:
        # Get user input
        user_input = input("You: ").strip().lower()
        
        # Check for exit condition
        if user_input == "exit":
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Responses based on rules
        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I help you today?")
        
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but thanks for asking! How can I assist you?")
        
        elif "name" in user_input:
            print("Chatbot: I'm a simple rule-based chatbot.")
        
        elif "help" in user_input:
            print("Chatbot: I'm here to answer simple questions or chat with you. Feel free to ask anything!")
        
        elif "thank you" in user_input or "thanks" in user_input:
            print("Chatbot: You're welcome! Let me know if there's anything else I can help with.")
        
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Could you please rephrase?")
    
# Run the chatbot
chatbot()
