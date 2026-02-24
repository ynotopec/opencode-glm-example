# Cas d'Usage - USE_CASE.md

## Description du problème métier

Ce projet modélise le fonctionnement d'un **système de vote électronique simplifié** pour les élections locales. La problématique traitée est :

> **Comment permettre aux citoyens de voter efficacement tout en garantissant la transparence et la rapidité des résultats ?**

## Scénario d'utilisation

### Contexte métier
Dans un contexte municipal, les élections locales nécessitent :
- Une interface simple pour les électeurs
- Une procédure de vote rapide et intuitive
- Un système de comptage efficace
- Des résultats consultables en temps réel

### Protagonistes
1. **Électeurs** : Citoyens de la commune
2. **Ministère de l'Intérieur** : Organisateur de l'élection
3. **Système de vote** : Application web proposée

## Cas d'utilisation typique

### Flux utilisateur principal

1. **Accès au système** (Durée : 30 secondes)
   - L'électeur ouvre un navigateur
   - Se connecte à l'URL du système
   - Navigate jusqu'à la page de vote

2. **Vote** (Durée : 45 secondes)
   - L'électeur examine les candidats disponibles
   - Sélectionne son préféré via un clic
   - Confirme le vote en cliquant sur un bouton

3. **Résultats** (Durée : Instantané)
   - Page de redirection vers résultats
   - Visualisation des pourcentages mis à jour
   - Confirmation du vote effectué

## Exigences fonctionnelles

### Critères E2E (End-to-End)

| Critère | Valeur attendue | Mesure |
|---------|----------------|--------|
| Temps de chargement initial | < 2 secondes | Performance browser |
| Temps de vote (click-to-redirect) | < 0,5 secondes | Performance backend |
| Temps de calcul résultats | < 0,1 secondes | Performance algorithmique |
| Disponibilité 24/7 | 100% (simulation) | Uptime monitoring |
| Interface mobile-friendly | 100% responsive | Browser tests |
| Précision à 2 décimales | Exacte | Calcul mathématique |

### Scénarios de succès

1. ✅ **Vote unique** : Un électeur vote sans erreur
2. ✅ **Mise à jour immédiate** : Résultats visibles instantanément
3. ✅ **Multi-votants** : Plusieurs électeurs peuvent voter
4. ✅ **Réinitialisation** : Admin peut remettre à zéro
5. ✅ **Tri automatique** : Classement par ordre de votes

### Scénarios d'erreur

1. ❌ **ID invalide** : Réception d'un ID hors plage (1-5) → Traitement safe, pas de crash
2. ❌ **Double vote** : Pas de persistance (session limitée) → Pas de vote compté deux fois
3. ❌ **Navigation directe** : URL /results sans vote → Affichage des données actuelles

## Exemple de test de validation

### Entrée
```
GET http://127.0.0.1:5000/
```
### Sortie attendue
```
200 OK
HTML Content-Type avec templates/index.html
Contient 5 cartes de candidats
Contient formulaire POST /vote
Contient formulaire POST /reset
```

### Entrée
```
POST http://127.0.0.1:5000/vote
candidate_id: 2
```
### Sortie attendue
```
302 Temporary Redirect
Location: /results
Session data updated (votes[2] += 1)
```

### Entrée
```
GET http://127.0.0.1:5000/results
```
### Sortie attendue
```
200 OK
HTML Content-Type avec templates/results.html
Contient total_votes calculé
Contient liste classée par percentage décroissant
Graphiques/barres de progression affichées
```

## Indicateurs de succès (KPIs)

| KPI | Definition | Cible | Méthode de mesure |
|-----|-----------|-------|-------------------|
| **Taux de votes réussis** | Votes valides / Total votes | > 95% | Backend logs |
| **Temps de réponse** | Time from click to page load | < 1,5 sec | Browser DevTools |
| **UX Score** | Satisfaction utilisateur (visuelle) | Interface intuitive | Feedback qualitative |
| **Compréhension** | Temps pour comprendre l'interface | < 2 minutes | Onboarding test |
| **Erreur minimale** | Taux d'erreurs (non valides) | < 5% | Error handling |

## Hypothèses métier

**H1 :** Les électeurs maîtrisent l'utilisation d'un navigateur web
**H2 :** Le système est utilisé dans un environnement contrôlé (pas de public de masse)
**H3 :** 1 candidat = 1 parti (champ simplifié réduit à une chaîne)
**H4 :** Les votes ne nécessitent pas de persistance (suffit pour démonstration)
**H5 :** L'identité des électeurs n'est pas traitée (anonymat simplifié)

## Conditions environnementales

- ✅ Internet disponible (pour charger Bootstrap depuis CDN)
- ✅ Navigateur moderne (Chrome, Firefox, Safari, Edge)
- ✅ Device mobile ou desktop
- ✅ Python 3.8+ installé
- ✅ Pip access pour dépendances

## Limites connues

1. **Pas d'authentification** : Aucun login obligatoire
2. **Pas de IP tracking** : Pas de prévention de double vote
3. **Pas de base de données** : Données perdues à chaque redémarrage
4. **Pas de sécurité HTTPS** : Utilisation HTTP local seulement
5. **Pas de logging** : Pas de suivi des votes par audit
6. **Pas de notifications** : Pas d'avertissement après vote

## Cas d'usage avancés (futurs)

1. **Export CSV** : Sauvegarde des résultats en tableurs
2. **API REST** : Connexibilité avec applications externes
3. **Gestion des candidats dynamique** : Ajout/suppression via admin panel
4. **Déploiement Cloud** : Service hébergé (Heroku, AWS, Azure)
5. **Test automation** : Scénarios de vote en masse
6. **Dashboard admin** : Vue statistique approfondie

## Valeur ajoutée réelle pour une entreprise

Bien que ceci reste un démonstration (POC), ce système pourrait être adapté pour :
- **Élections interne** : Vote pour le choix de délégués
- **Votes participatifs** : Consultations populaires
- **Enquêtes internes** : Sondages anonymes
- **Hackathons** : Votations pour les meilleures idées
- **Concours** : Vote public pour le prix du projet

**Coût de réalisation** : ~15-20 heures de développement
**Temps de déploiement** : < 30 minutes
**ROI estimé** : Dépend du contexte de déploiement réel