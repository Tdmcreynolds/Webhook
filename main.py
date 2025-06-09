from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Webhook service is up", 200

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Received webhook:", data)
    return jsonify({"status": "ok"}), 200

# Only include this if you're running locally (NOT on Railway)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
