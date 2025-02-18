# Notes perso

## fonctionnement de Semantic Release
Pour que Semantic Release fonctionne correctement, il faut que tu utilises des messages de commit bien formatés selon une convention. La convention la plus courante est Conventional Commits.

### Voici un exemple de règles de commit
- feat: Nouvelle fonctionnalité (pour un changement majeur ou mineur).
- fix: Correction de bug.
- docs: Modifications de la documentation.
- chore: Changements mineurs, de style ou de configuration.
- BREAKING CHANGE : Pour une modification majeure (la version augmente de manière significative, ex. de 1.x à 2.0).

### lint
Tu peux également configurer un commit linter pour t'assurer que les messages de commit respectent cette convention. Cela peut être fait avec un package comme commitlint et husky pour les hooks Git.

## installation
### Étape 1 : Préparer ton projet
Avant de commencer, assure-toi que ton projet est versionné avec Git et que tu as un dépôt GitHub configuré. Dans cet exemple, nous allons utiliser un projet avec le dossier src pour le code et le dossier test pour les tests.

### Étape 2 : Installer les dépendances nécessaires
1. Installer Node.js et npm : Semantic Release est basé sur Node.js, donc tu dois avoir Node.js et npm installés sur ton environnement. Si tu n'as pas encore installé Node.js, tu peux le faire depuis nodejs.org.
2. Installer les outils nécessaires pour Semantic Release : Dans ton terminal, dans le dossier de ton projet, exécute ces commandes pour installer les packages nécessaires :
```bash
# Initialise un package.json si tu n'en as pas encore
npm init -y

# Installe Semantic Release et ses plugins nécessaires
npm install --save-dev semantic-release @semantic-release/changelog @semantic-release/git @semantic-release/commit-analyzer @semantic-release/release-notes-generator @semantic-release/github
```

Ces packages vont permettre à Semantic Release de :

Analyser les messages de commit pour déterminer la version à appliquer (commit-analyzer),
Générer et maintenir le changelog (changelog),
Mettre à jour le changelog et faire des commits pour le tag de la version (git),
Publier une nouvelle version sur GitHub (github).

3. Configurer le fichier .releaserc
4. Ajouter un Workflow GitHub Actions