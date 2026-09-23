"""
Pytest charge ce fichier automatiquement.

Objectif:
- Ajouter la racine du projet dans sys.path
- Permettre les imports: from app.app import create_app
même en CI (où le contexte d'exécution peut varier).
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
