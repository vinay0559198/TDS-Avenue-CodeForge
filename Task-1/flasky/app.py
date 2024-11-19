from flask import Flask, request, render_template

app = Flask(__name__)

# Chatbot response logic
def chatbot_response(user_input):
    user_input = user_input.strip().lower()
    
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a program, but thanks for asking! How can I assist you?"
    elif "name" in user_input:
        return "I'm a simple rule-based chatbot."
    elif "help" in user_input:
        return "I'm here to answer simple questions or chat with you. Feel free to ask anything!"
    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome! Let me know if there's anything else I can help with."
    else:
        return "I'm sorry, I didn't understand that. Could you please rephrase?"

# Route for the main page
@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        response = chatbot_response(user_input)
    
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
