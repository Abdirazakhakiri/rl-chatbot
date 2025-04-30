
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Reinforcement learning chatbot is live."

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json(force=True)
        message = data.get("query", "")
        print("Received:", message)

        response = {
            "chatbot_response": f"You asked: {message}. Let me help you out."
        }

        return jsonify(response)

    except Exception as e:
        print("Webhook error:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

