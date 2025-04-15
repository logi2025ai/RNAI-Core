from flask import Flask, jsonify
import requests
import base64
import os

app = Flask(__name__)

ZOOM_CLIENT_ID = os.getenv("ZOOM_CLIENT_ID")
ZOOM_CLIENT_SECRET = os.getenv("ZOOM_CLIENT_SECRET")
ZOOM_BASE64 = os.getenv("ZOOM_BASE64")  # client_id:client_secret codificado en base64

@app.route('/')
def home():
    return '<h2>✅ RNAI-Core conectado a Zoom</h2>'

@app.route('/zoom/token')
def get_zoom_token():
    url = "https://zoom.us/oauth/token?grant_type=account_credentials&account_id=" + os.getenv("ZOOM_ACCOUNT_ID")
    headers = {
        "Authorization": f"Basic {ZOOM_BASE64}"
    }
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch Zoom token", "details": response.text})

if __name__ == '__main__':
    app.run(debug=True)
