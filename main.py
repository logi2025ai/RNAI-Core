from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>RNAI Core Backend Activo ✅</h1>"

@app.route("/zoom")
def zoom_integration():
    return "🟢 Integración con Zoom preparada."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
