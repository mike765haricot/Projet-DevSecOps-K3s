import os
import logging
from flask import Flask, jsonify

# Configuration des logs (volontairement verbeux pour l'étape d'observabilité)
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

# Utilisation d'une variable d'environnement (vulnérabilité potentielle si mal gérée)
SECRET_DATA = os.environ.get('SECRET_DATA', 'Donnee_Sensible_Par_Defaut')

@app.route('/api/data')
def get_data():
    app.logger.info("Appel à l'API /api/data reçu.")
    return jsonify({
        "status": "success",
        "service": "Backend API",
        "secret_leaked": SECRET_DATA
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
