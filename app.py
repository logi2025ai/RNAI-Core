from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '¡Hola desde Revolution AI Crypto!'

@app.route('/tokenomics')
def tokenomics():
    return {
        "total_supply": "10,000,000 RNAI",
        "creators_pool": "10%",
        "team_allocation": "4% (vested)",
        "community_partners": "6%"
    }

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

