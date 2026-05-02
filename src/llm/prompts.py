# Prompts prédéfinis pour l'analyse santé
HEALTH_ANALYSIS_PROMPT = """
Tu es un coach santé personnel. Voici les données santé de l'utilisateur :
{health_data}

Analyse ces données et donne :
1. Un résumé des tendances (3 points clés).
2. 3 recommandations personnalisées.
3. Un avertissement si une métrique est anormale (ex: fréquence cardiaque élevée).

Format de réponse :
---
**Résumé** :
1. [Point 1]
2. [Point 2]
3. [Point 3]

**Recommandations** :
1. [Recommandation 1]
2. [Recommandation 2]
3. [Recommandation 3]

**Avertissements** :
- [Avertissement si nécessaire, sinon "Aucun"]
---
"""

WORKOUT_SUGGESTION_PROMPT = """
Propose un entraînement personnalisé pour un utilisateur avec les objectifs suivants :
{goals}

Contraintes :
- Durée : {duration} minutes
- Équipement disponible : {equipment}

Format de réponse :
---
**Entraînement du jour** :
1. [Exercice 1] - [Durée/Séries]
2. [Exercice 2] - [Durée/Séries]
3. [Exercice 3] - [Durée/Séries]

**Conseils** :
- [Conseil 1]
- [Conseil 2]
---
"""