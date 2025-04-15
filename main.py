from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "<h1>RNAI Core Backend Activo ✅</h1>"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("🚀 Webhook recibido:", data)
    return jsonify({"status": "success", "data": data}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
