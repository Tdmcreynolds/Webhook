from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Webhook received:", data)  # This will show up in Railway logs
    return jsonify({"status": "received", "data": data}), 200

@app.route("/", methods=["GET"])
def home():
    return "Webhook receiver is live!", 200
    updated main.py to log webhook data
