import os
import requests
from flask import Flask

app = Flask(__name__)

# L'URL du backend sera passée par Kubernetes
BACKEND_URL = os.environ.get('BACKEND_URL', 'http://localhost:8080')

@app.route('/')
def index():
    try:
        # Le Frontend interroge le Backend
        response = requests.get(f"{BACKEND_URL}/api/data")
        data = response.json()
        return f"<h1>Frontend Actif</h1><p>Réponse du Backend : {data}</p>"
    except Exception as e:
        return f"<h1>Erreur</h1><p>Impossible de joindre le Backend : {e}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
