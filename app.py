
@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json(force=True)
        message = data.get("query", "")  # safer access

        print("User said:", message)

        if not message:
            return jsonify({"chatbot_response": "Hmm, I didn't catch that. Can you rephrase?"})

        response = {
            "chatbot_response": f"You asked: {message}"
        }

        return jsonify(response)

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"chatbot_response": "Oops, something went wrong. Try again."}), 500

