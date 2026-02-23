#!/bin/bash
set -e

echo "🚀 Début du pipeline CI/CD..."

echo "📦 [CI] Build de l'image Backend..."
cd ~/Projet_DevSecOps/backend
sudo docker build -t backend-api:v2 .
sudo docker save backend-api:v2 | sudo k3s ctr images import -

echo "📦 [CI] Build de l'image Frontend..."
cd ~/Projet_DevSecOps/frontend
sudo docker build -t frontend-web:v2 .
sudo docker save frontend-web:v2 | sudo k3s ctr images import -

echo "⚙️ [CD] Mise à jour des Manifests (Versionnement simule)..."
cd ~/Projet_DevSecOps/k8s
sed -i 's/backend-api:v1/backend-api:v2/g' deploy.yaml
sed -i 's/frontend-web:v1/frontend-web:v2/g' deploy.yaml

echo "🚢 [CD] Déploiement automatisé sur Kubernetes..."
kubectl apply -f deploy.yaml

echo "✅ Pipeline terminé avec succès !"
