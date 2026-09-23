🔐 Docker Security + Trivy + GitHub Actions

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-API-black?logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED?logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF?logo=githubactions&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Tests-0A9EDC?logo=pytest&logoColor=white)
![Trivy](https://img.shields.io/badge/Trivy-Security-1904DA?logo=aquasecurity&logoColor=white)

📌 Description

Projet DevOps orienté sécurité des conteneurs Docker.

L'application utilise une API Flask conteneurisée, testée automatiquement avec pytest, puis analysée avec Trivy dans une pipeline GitHub Actions.

Le pipeline vérifie successivement les tests Python, la construction de l'image Docker et les vulnérabilités HIGH et CRITICAL détectées dans l'image.

🎯 Objectifs

Cette mission permet de pratiquer :

Docker
Python / Flask
pytest
GitHub Actions
CI/CD
analyse de vulnérabilités
sécurité des images Docker
Trivy

🏗️ Architecture
                 👩‍💻 Developer
                      │
                      │ git push
                      ▼
             ┌──────────────────┐
             │  GitHub Actions  │
             └────────┬─────────┘
                      │
                      ▼
             ┌──────────────────┐
             │  Python Tests    │
             │     pytest       │
             └────────┬─────────┘
                      │
                   Tests OK
                      │
                      ▼
             ┌──────────────────┐
             │   Docker Build   │
             └────────┬─────────┘
                      │
                      ▼
             ┌──────────────────┐
             │ Trivy Security   │
             │      Scan        │
             └────────┬─────────┘
                      │
                      ▼
              🔐 HIGH / CRITICAL

📁 Structure du projet
docker-security-trivy/
│
├── app/
│   ├── .dockerignore
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
│
├── tests/
│   └── test_app.py
│
├── .github/
│   └── workflows/
│       └── security.yml
│
├── .gitignore
├── docker-compose.yml
└── README.md

🌐 API Flask

L'application expose trois endpoints :

Méthode	Endpoint	Fonction
GET	/	Vérifier que l'API fonctionne
GET	/health	Vérifier l'état de l'API
GET	/info	Afficher les informations du projet
Tester l'API
curl http://localhost:5000/
curl http://localhost:5000/health
curl http://localhost:5000/info

Exemple :

{
  "message": "Docker Security Demo",
  "status": "running"
}

🐳 Docker

L'application utilise une image basée sur :

python:3.12-slim

Le Dockerfile :

définit l'image Python
crée le répertoire de travail
installe les dépendances
copie l'application
expose le port 5000
démarre Flask

Construction de l'image :

docker build -t docker-security-trivy:latest ./app

🧪 Tests automatisés

Les tests utilisent pytest.

Fichier :

tests/test_app.py

Les tests vérifient :

l'endpoint /
l'endpoint /health
l'endpoint /info

Lancer les tests :

pytest

Résultat attendu :

3 passed

⚙️ GitHub Actions

Le workflow est situé dans :

.github/workflows/security.yml

Il se déclenche lors :

d'un push sur main
d'une pull request vers main
Pipeline CI
Git Push / Pull Request
          │
          ▼
     Python Tests
          │
          ▼
     Docker Build
          │
          ▼
    Trivy Security Scan

Les jobs sont exécutés dans cet ordre grâce à :

needs: test

et :

needs: docker

Le scan de sécurité intervient donc après la réussite des tests et de la construction Docker.

🔐 Analyse de sécurité avec Trivy

Trivy analyse l'image Docker afin d'identifier les vulnérabilités connues.

Le workflow recherche principalement :

HIGH
CRITICAL

Configuration utilisée :

severity: CRITICAL,HIGH

Les vulnérabilités sans correctif disponible sont ignorées :

ignore-unfixed: true

Pour cette mission, le scan utilise :

exit-code: 0

Le pipeline affiche donc les résultats sans bloquer automatiquement le workflow.

Dans un environnement de production, une politique plus stricte pourrait utiliser :

exit-code: 1

afin de bloquer la pipeline lorsqu'une vulnérabilité répondant aux critères définis est détectée.

🐳 Docker Compose

Le fichier docker-compose.yml permet de lancer l'application avec :

docker compose up -d

Vérifier le conteneur :

docker compose ps

Arrêter l'application :

docker compose down

🚀 Installation

1. Cloner le repository
git clone https://github.com/cis-debug/docker-security-trivy.git
cd docker-security-trivy
2. Installer les dépendances
pip install -r app/requirements.txt
3. Lancer les tests
pytest
4. Construire l'image Docker
docker build -t docker-security-trivy:latest ./app
5. Démarrer avec Docker Compose
docker compose up -d
6. Tester l'application
curl http://localhost:5000/

🔧 Commandes utiles
Voir les images Docker
docker images
Voir les conteneurs
docker ps
Voir les logs
docker compose logs
Arrêter les services
docker compose down
Reconstruire l'image
docker compose build

🛠️ Technologies utilisées
🐍 Python 3.12
🌐 Flask
🧪 Pytest
🐳 Docker
🧩 Docker Compose
⚙️ GitHub Actions
🔐 Trivy
🐧 Linux / WSL
🔧 Git / GitHub
🔐 Bonnes pratiques de sécurité

Pour aller plus loin dans un environnement réel :

utiliser des images Docker minimales
maintenir les dépendances à jour
scanner régulièrement les images
utiliser GitHub Secrets pour les informations sensibles
éviter les secrets dans le code source
utiliser un utilisateur non-root dans les conteneurs
définir une politique de blocage pour les vulnérabilités critiques
intégrer le scan de sécurité avant le déploiement

🚀 Améliorations possibles
Ajouter un scan des dépendances Python
Ajouter un scan du code avec Bandit
Ajouter un scan des secrets
Ajouter une analyse Dockerfile
Publier l'image sur Docker Hub
Ajouter un déploiement automatique
Utiliser exit-code: 1 pour bloquer certaines vulnérabilités
Ajouter une étape de sécurité avant le déploiement cloud

👩‍💻 Auteur

Cisse Ndeye

GitHub :
https://github.com/cis-debug
