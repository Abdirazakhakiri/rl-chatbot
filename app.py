
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Your reinforcement learning chatbot is live. How can I help you?"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    message = data.get("message", {}).get("content", "")
    print("Received message:", message)

    response = {
        "chatbot_response": f"You said: {message}"
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)