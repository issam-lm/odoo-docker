# Projet Odoo Docker

Bonjour ! Ce README explique comment utiliser ce projet Odoo avec Docker.

J'ai mis en place une configuration Docker Compose pour faire tourner Odoo 17 avec une base de données PostgreSQL 16. Il y a aussi un module personnalisé pour la gestion des évaluations que j'ai développé.

## Ce qu'il faut avoir

- Docker installé sur votre machine
- Docker Compose (normalement inclus avec Docker Desktop)

## Comment démarrer

1. Ouvrez un terminal dans le dossier `odoo-docker`
2. Lancez la commande suivante :

```bash
docker-compose up -d
```

3. Patientez un peu (30 secondes à 1 minute) le temps que tout démarre
4. Ouvrez votre navigateur et allez sur `http://localhost:8069`

C'est tout ! Vous devriez voir la page de configuration d'Odoo.

## Configuration de la base de données

Quand vous créez la base de données dans Odoo, voici les infos à utiliser :
- Utilisateur : `odoo`
- Mot de passe : `odoo`
- Nom de la base : `odoo_db` (ou ce que vous voulez)
- Hôte : `db` (c'est le nom du service dans docker-compose)

Le port PostgreSQL est 5432 si jamais vous avez besoin d'y accéder directement.

## Structure du projet

```
odoo-docker/
├── docker-compose.yml
├── config/              # Config Odoo (vide pour l'instant)
├── addons/
│   └── tp_gestion_evaluations/  # Mon module perso
└── README.md
```

## Le module tp_gestion_evaluations

C'est un module que j'ai fait pour gérer des évaluations. Il permet de :
- Créer des évaluations avec un nom, un responsable, une date de début
- Voir le statut de chaque évaluation
- Afficher tout ça dans une liste et un formulaire

Version actuelle : 17.0.1.0.0

Développé par M. AIT DAOUD

## Commandes utiles

**Démarrer tout :**
```bash
docker-compose up -d
```

**Arrêter :**
```bash
docker-compose down
```

**Voir les logs (très utile pour débugger) :**
```bash
docker-compose logs -f
```

**Redémarrer :**
```bash
docker-compose restart
```

**Se connecter au conteneur Odoo :**
```bash
docker exec -it odoo_app bash
```

**Se connecter à la base de données :**
```bash
docker exec -it odoo_db psql -U odoo -d odoo_db
```

## Les données sont sauvegardées

Les volumes Docker gardent vos données même si vous arrêtez les conteneurs :
- `odoo-web-data` : tout ce qui concerne Odoo
- `odoo-db-data` : la base de données PostgreSQL

Donc pas de panique, vos données ne disparaîtront pas !

## Problèmes courants

**Les conteneurs ne démarrent pas :**
- Vérifiez que les ports 8069 et 5432 ne sont pas déjà utilisés par autre chose
- Regardez les logs : `docker-compose logs`

**Odoo ne se connecte pas à la base :**
- Attendez un peu, PostgreSQL met quelques secondes à être prêt
- Regardez les logs du conteneur `odoo_db`

**Je ne vois pas mon module dans Odoo :**
- Vérifiez qu'il est bien dans le dossier `addons`
- Activez le mode développeur dans Odoo (Paramètres > Activer le mode développeur)
- Allez dans Applications et cliquez sur "Mettre à jour la liste des applications"

## Quelques notes

- Le mode dev est activé par défaut (`--dev=xml`) pour faciliter le développement
- Les modules perso sont dans `/mnt/extra-addons` dans le conteneur
- La config Odoo vient du dossier `./config` (mais il est vide pour l'instant)

## Auteur

M. AIT DAOUD

---

*Note : Ce projet est pour usage éducatif et développement. N'hésitez pas à modifier ce qui vous convient !*
