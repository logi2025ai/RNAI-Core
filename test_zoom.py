import requests
import base64
import json

# 🔐 Credenciales Zoom (modo directo)
client_id = "_0e_lS9YTLq7X8oklZeaeA"
client_secret = "6wG0LMpGiww0ZAyhJmx6MbfLK3dG5wUP"
account_id = "H47iWXbTU24W54HOma5_A"

# Codificación Base64
credentials = f"{client_id}:{client_secret}"
credentials_b64 = base64.b64encode(credentials.encode()).decode()

# Obtener token
auth_url = "https://zoom.us/oauth/token"
headers = {
    "Authorization": f"Basic {credentials_b64}"
}
params = {
    "grant_type": "account_credentials",
    "account_id": account_id
}

print("🔐 Obteniendo token de acceso...")

auth_response = requests.post(auth_url, headers=headers, params=params)
auth_data = auth_response.json()
access_token = auth_data.get("access_token")

if not access_token:
    print("❌ Error al obtener token:", auth_data)
    exit()

print("✅ Token recibido correctamente.")

# Crear reunión instantánea
create_meeting_url = "https://api.zoom.us/v2/users/me/meetings"
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

data = {
    "topic": "Reunión de prueba RNAI 🤖",
    "type": 1,
    "settings": {
        "host_video": True,
        "participant_video": True
    }
}

print("📞 Creando reunión...")

response = requests.post(create_meeting_url, headers=headers, json=data)

if response.status_code == 201:
    meeting_info = response.json()
    print("🎉 Reunión creada con éxito:")
    print("🔗 Join URL:", meeting_info["join_url"])
    print("🧑‍💼 Start URL (host):", meeting_info["start_url"])
else:
    print("❌ Error al crear reunión:", response.text)
