from flask import Flask

app = Flask(__name__)

MY_SECRET_KEY = "mi_clave_ultra_secreta"

@app.route("/")
def home():
    return f"¡Hola desde Revolution AI Crypto! Tu clave secreta es: {MY_SECRET_KEY}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
