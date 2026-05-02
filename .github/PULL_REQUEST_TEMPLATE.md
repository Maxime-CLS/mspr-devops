---
name: Pull Request
about: Template pour soumettre une pull request
title: ''
labels: ''
assignees: ''
---

---

## 📌 **Description**
**Décrivez brièvement les changements apportés par cette PR.**
- Quelle fonctionnalité est ajoutée ?
- Quel bug est corrigé ?
- Quelle amélioration est apportée ?

**Exemples :**
- `feat: ajouter l'authentification Firebase`
- `fix: corriger l'erreur de connexion à SQLite`
- `docs: mettre à jour le README avec les instructions de déploiement`

---

---

## 🎯 **Type de Changement**
**Sélectionnez le type de changement correspondant (cochez toutes les cases pertinentes) :**
- [ ] ✅ **Nouvelle fonctionnalité** (ajout d'une capacité non existante)
- [ ] 🐛 **Correction de bug** (réparation d'un problème existant)
- [ ] 📚 **Documentation** (mise à jour de la documentation)
- [ ] 🔄 **Refactoring** (modification du code sans changer son comportement)
- [ ] 🔧 **Chore** (mise à jour des dépendances, configuration, etc.)
- [ ] ⚡ **Amélioration des performances** (optimisation du code)
- [ ] 🧪 **Tests** (ajout ou mise à jour de tests)
- [ ] 🎨 **UI/UX** (modifications de l'interface utilisateur)
- [ ] 🔒 **Sécurité** (correction de vulnérabilités ou amélioration de la sécurité)

---

---

## 🔗 **Issues Liées**
**Liez cette PR à une ou plusieurs issues en utilisant les mots-clés suivants :**
- `Clôt #123` (ferme automatiquement l'issue #123 lorsque la PR est mergée)
- `Relie #456` (lie la PR à l'issue #456 sans la fermer)
- `Fixes #789` (indique que cette PR corrige l'issue #789)

**Exemple :**
> Clôt #42

---
---

## 📝 **Détails des Changements**
**Décrivez en détail les modifications apportées :**
- Quels fichiers ont été modifiés ?
- Quelles sont les principales modifications ?
- Pourquoi ces changements sont-ils nécessaires ?

**Exemple :**
> - **Fichiers modifiés** : `src/database/db_manager.py`, `src/auth/auth_manager.py`
> - **Modifications** :
>   - Ajout d'une fonction `backup_database()` pour sauvegarder automatiquement la base SQLite.
>   - Intégration de l'authentification dans les requêtes à la base de données.
> - **Raison** : Assurer la persistance des données et sécuriser l'accès à la base.

---
---

## 📸 **Captures d'Écran / Démos (si applicable)**
**Si votre PR modifie l'interface utilisateur ou ajoute une nouvelle fonctionnalité visible, ajoutez des captures d'écran ou des GIFs pour illustrer les changements.**

**Exemple :**
> **Avant :**
> ![Avant](https://via.placeholder.com/400x200?text=Ancienne+interface)
>
> **Après :**
> ![Après](https://via.placeholder.com/400x200?text=Nouvelle+interface)

---
---

## ✅ **Checklist avant Soumission**
**Vérifiez que votre PR respecte les critères suivants avant de la soumettre :**

- [ ] **Le code suit les standards du projet** (PEP 8, conventions de nommage, etc.).
- [ ] **Tous les tests passent localement** (`python -m pytest tests/`).
- [ ] **Le linter ne rapporte aucune erreur** (`flake8 src/`).
- [ ] **Les nouvelles fonctionnalités sont couvertes par des tests**.
- [ ] **La documentation est mise à jour** (README, docs/, etc.).
- [ ] **Les messages de commit sont clairs et descriptifs** (suivent [Conventional Commits](https://www.conventionalcommits.org/)).
- [ ] **Aucun secret ou information sensible** n'est inclus dans le code (vérifiez `.env`, tokens, etc.).
- [ ] **La PR est assignée à un ou plusieurs mainteneurs** pour revue.
- [ ] **Le titre de la PR est clair et descriptif**.

---
---

## 🧪 **Tests et Validation**
**Décrivez comment tester vos changements :**
- Quelles commandes exécuter ?
- Quels scénarios tester ?
- Comment valider que tout fonctionne ?

**Exemple :**
> Pour tester cette PR :
> 1. Exécutez `docker-compose up -d` pour démarrer les services.
> 2. Accédez à [http://localhost:8501](http://localhost:8501) et testez la nouvelle fonctionnalité d'authentification.
> 3. Vérifiez que les sauvegardes de la base de données sont créées dans `./backups/`.
> 4. Exécutez `python -m pytest tests/test_db.py` pour valider les tests de la base de données.

---
---

## 📊 **Impact et Risques**
**Décrivez l'impact de vos changements et les risques potentiels :**

- **Impact positif :**
  - Exemple : "Améliore la sécurité en ajoutant une authentification."
  - Exemple : "Réduit le temps de réponse de l'API de 50%."

- **Risques potentiels :**
  - Exemple : "Modification de la structure de la base de données (nécessite une migration)."
  - Exemple : "Changement de l'API (nécessite une mise à jour des clients)."

---
---

## 🔄 **Notes pour les Revueurs**
**Ajoutez ici des notes spécifiques pour les personnes qui vont revoir votre PR :**
- Points à vérifier particulièrement.
- Questions ou incertitudes.
- Contexte supplémentaire utile.

**Exemple :**
> @mainteneur1, peux-tu vérifier que l'intégration avec Ollama fonctionne correctement ?
> J'ai testé localement, mais je n'ai pas accès à l'environnement de staging.

---
---
## 📜 **Licence**
En soumettant cette PR, vous acceptez que vos contributions soient licenciées sous la **[LICENSE](LICENSE)** du projet (MIT).

---
---
**Merci pour votre contribution !** 🙌
Votre travail aide à améliorer **PHC** pour tout le monde.