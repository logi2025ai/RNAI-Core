from flask import Flask, render_template
import requests
import base64
import json

app = Flask(__name__)

client_id = "_0e_lS9YTLq7X8oklZeaeA"
client_secret = "6wG0LMpGiww0ZAyhJmx6MbfLK3dG5wUP"

def get_access_token():
    auth_str = f"{client_id}:{client_secret}"
    headers = {
        "Authorization": f"Basic {base64.b64encode(auth_str.encode()).decode()}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = {
        "grant_type": "client_credentials"
    }
    res = requests.post("https://zoom.us/oauth/token", headers=headers, data=payload)
    return res.json().get("access_token")

def create_meeting():
    token = get_access_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {
        "topic": "Reunión RNAI",
        "type": 1
    }
    res = requests.post("https://api.zoom.us/v2/users/me/meetings", headers=headers, data=json.dumps(data))
    return res.json().get("join_url")

@app.route("/")
def index():
    join_url = create_meeting()
    return render_template("index.html", join_url=join_url)

if __name__ == "__main__":
    app.run(debug=True)
