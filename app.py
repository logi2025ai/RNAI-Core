from flask import Flask, render_template, request
import base64
import requests

app = Flask(__name__)

# Credenciales Zoom - integradas
client_id = "_0e_lS9YTLq7X8oklZeaeA"
client_secret = "6wG0LMpGiww0ZAyhJmx6MbfLK3dG5wUP"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/join", methods=["POST"])
def join_meeting():
    auth_string = f"{client_id}:{client_secret}"
    encoded_auth = base64.b64encode(auth_string.encode()).decode()

    headers = {
        "Authorization": f"Basic {encoded_auth}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {
        "grant_type": "client_credentials"
    }

    response = requests.post("https://zoom.us/oauth/token", headers=headers, data=payload)

    if response.status_code == 200:
        return "✅ Autenticado con éxito. Zoom Token generado."
    else:
        return f"❌ Error autenticando: {response.text}"

if __name__ == "__main__":
    app.run(debug=True)
