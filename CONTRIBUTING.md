# 📖 Guide de Contribution pour PHC (Personal Health Coach)

Merci de contribuer à **PHC** ! 🎉
Ce guide explique comment participer au projet, que ce soit pour signaler un bug, proposer une fonctionnalité, ou contribuer au code.

---

## 📜 Code de Conduite
En participant à ce projet, vous acceptez de respecter notre **[Code de Conduite](CODE_OF_CONDUCT.md)**.
Soyez bienveillant, respectueux et inclusif.

---

---

## 🚀 Comment Contribuer

### 1. **Signaler un Bug**
Si vous trouvez un bug, merci de :
1. Vérifier que le bug n’a pas déjà été signalé dans les [issues](https://github.com/<ton-org>/phc/issues).
2. Créer une nouvelle issue en utilisant le template **[Bug Report](https://github.com/<ton-org>/phc/issues/new?assignees=&labels=bug&template=bug_report.md&title=[Bug]%20)**.
3. Inclure :
   - Une description claire du bug.
   - Les étapes pour le reproduire.
   - Votre environnement (OS, version de Docker, navigateur, etc.).
   - Des captures d’écran si utile.

---

### 2. **Proposer une Nouvelle Fonctionnalité**
Pour proposer une nouvelle fonctionnalité :
1. Vérifiez que la fonctionnalité n’a pas déjà été demandée dans les [issues](https://github.com/<ton-org>/phc/issues).
2. Créez une nouvelle issue en utilisant le template **[Feature Request](https://github.com/<ton-org>/phc/issues/new?assignees=&labels=enhancement&template=feature_request.md&title=[Feature]%20)**.
3. Décrivez :
   - La fonctionnalité souhaitée.
   - Son utilité pour le projet.
   - Des exemples ou maquettes si possible.

---

### 3. **Contribuer au Code**
#### **Étapes pour contribuer :**
1. **Forker le dépôt** :
   - Cliquez sur le bouton **"Fork"** en haut à droite de la page du dépôt.
   - Clonez votre fork localement :
     ```bash
     git clone https://github.com/<votre-username>/phc.git
     cd phc
     ```

2. **Configurer l’environnement de développement** :
   - Suivez les instructions dans le [Guide de Setup](docs/setup.md) pour configurer Docker et les dépendances.
   - Créez une branche pour vos modifications :
     ```bash
     git checkout -b feature/ma-nouvelle-fonctionnalite
     ```
     > **Conseil** : Utilisez des noms de branche clairs et descriptifs (ex: `feature/ollama-integration`, `fix/db-backup`).

3. **Faire des modifications** :
   - Respectez les **standards de code** (voir ci-dessous).
   - Ajoutez des **tests** pour vos nouvelles fonctionnalités (voir [Tests](#-tests)).
   - Mettez à jour la **documentation** si nécessaire.

4. **Commiter vos changements** :
   - Utilisez des messages de commit clairs et suivis des [Conventional Commits](https://www.conventionalcommits.org/) :
     - `feat:` pour une nouvelle fonctionnalité.
     - `fix:` pour une correction de bug.
     - `docs:` pour une mise à jour de la documentation.
     - `refactor:` pour un refactoring de code.
     - `chore:` pour des modifications mineures (ex: mise à jour des dépendances).
     - Exemple :
       ```bash
       git commit -m "feat: ajouter l'authentification Firebase"
       ```

5. **Pousser vos changements** :
   ```bash
   git push origin feature/ma-nouvelle-fonctionnalite