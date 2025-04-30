
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Your reinforcement learning chatbot is live. How can I help you?"

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json(force=True)
        message = data.get("query", "").lower()

        print("Received:", message)

        if not message:
            return jsonify({"chatbot_response": "Sorry, I didn't catch that. Can you rephrase?"})

        if "price" in message or "$" in message:
            response_text = "We focus on results first. Let’s talk about what you need."
        elif "help" in message or "start" in message:
            response_text = "Sure! Just tell me what you're looking for and I’ll guide you."
        elif "how" in message:
            response_text = "Here’s how it works: we get leads to come to you. Want in?"
        else:
            response_text = f"You said: {message}"

        return jsonify({"chatbot_response": response_text})

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"chatbot_response": "Oops, something went wrong. Please try again later."}), 500

if __name__ == "__main__":
    app.run(debug=True)

