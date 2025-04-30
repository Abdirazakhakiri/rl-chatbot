from flask import Flask, request, jsonify
import sys
import traceback

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json(force=True, silent=True)
        if data is None:
            return jsonify({"error": "Invalid or missing JSON"}), 400

        print("Received data:", data)

        # Support multiple formats
        query = data.get("query") or \
                data.get("queryResult", {}).get("queryText") or \
                data.get("payload", {}).get("query")

        if not query:
            return jsonify({"error": "Query not found in request"}), 400

        response = f"You asked: {query}. Here's how to get more leads: Use Facebook Ads, automate follow-ups, and qualify leads with a funnel."
        return jsonify({"chatbot_response": response})

    except Exception as e:
        print("Error:", str(e))
        traceback.print_exc(file=sys.stdout)
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def home():
    return "Chatbot is live."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
