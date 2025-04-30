
from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Get your OpenAI key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET"])
def home():
    return "Your RL Chatbot is live and powered by GPT-4!"

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json()
        if not data or "query" not in data:
            return jsonify({"error": "Missing 'query' in request"}), 400

        user_message = data["query"]

        # GPT-4 AI Response
        completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You're a helpful sales chatbot for a marketing agency. Always guide people toward booking a strategy call."},
                {"role": "user", "content": user_message}
            ]
        )

        ai_reply = completion.choices[0].message["content"]

        return jsonify({"chatbot_response": ai_reply})

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": "Server error"}), 500

if __name__ == "__main__":
    app.run(debug=True)
