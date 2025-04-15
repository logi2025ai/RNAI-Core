import requests
import base64
import json

client_id = "_0e_lS9YTLq7X8oklZeaeA"
client_secret = "6wG0LMpGiww0ZAyhJmx6MbfLK3dG5wUP"

def get_access_token():
    url = "https://zoom.us/oauth/token"
    auth_str = f"{client_id}:{client_secret}"
    headers = {
        "Authorization": f"Basic {base64.b64encode(auth_str.encode()).decode()}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = {
        "grant_type": "client_credentials"
    }
    response = requests.post(url, headers=headers, data=payload)
    return response.json().get("access_token")

def create_meeting():
    token = get_access_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {
        "topic": "Reunión de prueba RNAI",
        "type": 1
    }
    response = requests.post(
        "https://api.zoom.us/v2/users/me/meetings",
        headers=headers,
        data=json.dumps(data)
    )
    result = response.json()
    print("🔗 Join URL:", result.get("join_url"))

if __name__ == "__main__":
    create_meeting()
