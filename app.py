
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Your reinforcement learning chatbot is live. How can I help you?"

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json(force=True)
        message = data.get("query", "I didn't get that.")
        print("Received message:", message)

        # Smarter AI-style response
        if "price" in message.lower():
            reply = "Our service starts at $3,000. Want a breakdown?"
        elif "how" in message.lower():
            reply = "We run Facebook ads + DMs + a sales funnel that converts."
        else:
            reply = f"Good question. Here's what I think: {message}"

        response = {
            "chatbot_response": reply
        }

        return jsonify(response)

    except Exception as e:
        print("Webhook error:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

