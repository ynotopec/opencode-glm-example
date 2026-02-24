# Architecture du Système

## Diagramme de haute niveau

```mermaid
flowchart TD
    A[Utilisateur] --> B[HTTP Request]
    B --> C[Flask Server]
    C --> D{Endpoint}
    D -->|GET /| E[Index Page]
    D -->|POST /vote| F[Voting Logic]
    D -->|POST /reset| G[Reset Logic]
    D -->|GET /results| H[Results Page]
    
    F --> I[Data Management]
    G --> I
    H --> I
    
    I --> J[Candidates Array]
    J --> K[Vote Counter]
    J --> L[Percentage Calculator]
    J --> M[Sort Engine]
    
    I --> N[Template Engine]
    E --> N
    H --> N
    
    N --> O[HTML Response]
    E --> P[Bootstrap 5 Styles]
    H --> P
    
    P --> R[Browser Display]
    O --> R
```

## Flux de données détaillé

### Vote Flow
```mermaid
sequenceDiagram
    participant U as Utilisateur
    participant B as Browser
    participant S as Flask Server
    participant D as Data Store
    participant T as Template Engine

    U->>B: Click "Vote" button
    B->>S: POST /vote (candidate_id)
    S->>S: Validate candidate ID
    S->>D: Increment votes[candidate_id]

    D-->>S: Updated data
    S->>S: Calculate percentages
    S->>S: Sort by votes (desc)

    S->>T: Pass candidates & percentages
    T-->>S: HTML template rendered
    S-->>B: REDIRECT /results

    B->>S: GET /results
    S->>T: Pass data
    T-->>S: Results HTML
    S-->>B: DISPLAY Results
```

## Architecture modulaire

### Layer 1: Interface (Templates)
- **Format** : HTML5 + Bootstrap 5
- **Responsiveness** : Mobile-first design
- **Interactivité** : AJAX-ready, animated elements

### Layer 2: Logic (Flask Routes)
- **index()** : Render voting page
- **vote()** : Process voting request
- **reset()** : Reset election data
- **results()** : Display statistics

### Layer 3: Data (In-memory)
- **Structure** : List of dictionaries
- **Content** : Candidate IDs, names, parties, votes
- **Scope** : Session-only (default Flask behavior)

### Layer 4: Engine (Flask Application)
- **Framework** : Flask (MVC simplified)
- **Routing** : URL-to-function mapping
- **Rendering** : Jinja2 template engine
- **Session Management** : Built-in Flask sessions

## Technologies employées

### Front-end
- **Bootstrap 5** : Framework CSS
- **CDN** : External dependencies (scripts, styles)
- **HTML** : Semantic markup
- **CSS** : Custom styles + gradients
- **JavaScript** : Bootstrap integration

### Back-end
- **Python 3** : Language d'exécution
- **Flask** : Web framework micro
- **Jinja2** : Template processor
- **Werkzeug** : Security & utils (part of Flask)

## Structure de contrôle

```mermaid
graph LR
    A[Flask App Instance] --> B[Route: /]
    A --> C[Route: /vote]
    A --> D[Route: /reset]
    A --> E[Route: /results]
    
    B --> F[MinistryOfInteriorApp]
    C --> F
    D --> F
    E --> F
    
    F --> G[Candidate Data]
    F --> H[Voting Logic]
    F --> I[Results Logic]
```

## Sécurité basique

- Input validation sur `candidate_id` (int)
- Protection contre injection (Jinja2 auto-escaping)
- Redirection sécurisée (Flask url_for)
- Pas de persistance de données sensibles

## Scalabilité

- **Oui** : Micro-framework, simple à étendre
- **Oui** : Architecture modulaire
- **Non** : Limité par Flask (pas d'ORM natif)
- **Non** : Pas de support natif HTTP/2

## Maintenance et évolution

- **Tests unitaires** : À ajouter
- **Migrations** : À prévoir si base de données
- **Monitoring** : Flask debug mode (dev) uniquement
- **Logging** : Manquant (à ajouter)