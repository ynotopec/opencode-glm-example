# Overview du Projet

## Vue d'ensemble

Ce projet est une application web de vote électronique développée avec **Flask (Python)**. Il propose une interface intuitive pour permettre aux citoyens de voter pour 5 candidats lors d'élections locales, avec visualisation en temps réel des résultats.

## Objectif pédagogique

La démonstration illustre les concepts suivants :
- Architecture web simple avec Flask
- Gestion d'état par session
- Templates HTML dynamiques
- Interface responsive adaptée aux mobiles
- Calcul automatique de pourcentages
- Redirections et routing

## Composition technique

### Composants principaux

1. **Application Flask (`app.py`)**
   - Classe `MinistryOfInteriorApp` encapsulant la logique métier
   - Routing RESTful pour les endpoints : `/`, `/vote`, `/reset`, `/results`
   - Gestion des données en mémoire (5 candidats)

2. **Templates HTML**
   - `templates/index.html` : Interface de vote utilisateur
   - `templates/results.html` : Tableau de bord des résultats

3. **Configuration**
   - Déploiement local (host `0.0.0.0`)
   - Mode debug activé
   - Port : 5000

## Données manipulées

Chaque candidat est représenté par :
- `id` : Identifiant unique (1-5)
- `name` : Nom du candidat
- `party` : Parti politique
- `votes` : Nombre de votes reçus

## Exemples de flux utilisateur

1. Utilisateur accède à **http://127.0.0.1:5000**
2. Système affiche les 5 cartes des candidats
3. Utilisateur clique sur "Voter pour [nom]" → POST `/vote`
4. Serveur incrémente les votes et redirige vers `/results`
5. Tableau de bord met à jour avec pourcentages classés

## Interfaces utilisateur

- Design moderne avec dégradés et ombres
- Responsive Bootstrap 5
- Animations fluides (barres de progression)
- Feedback visuel immédiat

## Limitations et améliorations futures

- [ ] Persistance des données (base de données)
- [ ] Authentification des électeurs
- [ ] IP tracking pour prévenir double vote
- [ ] Export des résultats
- [ ] Mode production (Gunicorn/Uvicorn)
- [ ] Tests unitaires
- [ ] Déploiement cloud