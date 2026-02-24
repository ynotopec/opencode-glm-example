# Opencode GLM Example

Application web de vote électronique pour élections locales. Ce projet démontre une solution complète de gestion électorale avec suivi en temps réel, résultats interactifs et interface utilisateur intuitive.

## 🚀 Démarrage rapide

### Prérequis
- Python 3.8+
- pip

### Installation
```bash
# Cloner le repository
git clone https://github.com/ynotopec/opencode-glm-example.git
cd opencode-glm-example

# Créer l'environnement virtuel
python3 -m venv venv

# Activer l'environnement
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Installer les dépendances
pip install flask

# Lancer l'application
python app.py
```

### Exécution
L'application se lance automatiquement sur **http://127.0.0.1:5000**

## 📚 Fonctionnalités

- 🗳️ **Système de vote** : Interface intuitive pour les électeurs
- 📊 **Résultats en temps réel** : Données mises à jour immédiatement
- 🔄 **Comptage automatique** : Calcul des pourcentages et classements
- 🎯 **5 candidats** : Multi-partis avec suivi détaillé
- 📈 **Tableaux de bord** : Visualisation claire et interactive
- 🎮 **Interface française** : Expérience utilisateur native

## 🛠️ Technologies

- **Back-end** : Python 3 + Flask
- **Front-end** : HTML5 + CSS + JavaScript
- **Hébergement** : Local (simulation)

## 📂 Structure

```
opencode-glm-example/
├── app.py                  # Application Flask
├── templates/              # Templates HTML (index, results)
├── venv/                   # Environnement virtuel Python
├── docs/                   # Documentation technique
│   ├── overview.md        # Vue d'ensemble technique
│   └── architecture.md    # Architecture du système
├── README.md               # Documentation principale
├── USE_CASE.md            # Cas d'usage détaillé
├── VALUE.md               # Analyse de valeur métier
└── INNOVATION_STATUS.md   # Trajectoire d'innovation
```

## 🎓 Usage Exemple

1. **Ouvrir** : Accéder à http://127.0.0.1:5000
2. **Voter** : Sélectionner un candidat et valider
3. **Voir les résultats** : Affichage automatique des pourcentages
4. **Réinitialiser** : Remettre à zéro les votes

## 📝 Licence

Propriétaire : ynotopec