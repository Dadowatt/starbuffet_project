# Star Buffet - Plateforme de gestion de traiteurs

## Description

Star Buffet est une application web développée avec Django permettant de gérer un annuaire de traiteurs et de mettre en relation des prestataires pour différents types d’événements.

## Installation du projet

### 1. Cloner le repository

```bash
git clone <repo_url>
cd starbuffet
```

### 2. Créer un environnement virtuel

```bash
python3 -m venv env
source env/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
pip install Pillow
```

### 4. Appliquer les migrations

```bash
python manage.py migrate
```

### 5. Créer un super utilisateur (admin)

```bash
python manage.py createsuperuser
```

### 6. Lancer le serveur

```bash
python manage.py runserver
```

## Accès à l'administration

http://127.0.0.1:8000/admin

## Fonctionnalités

### Gestion des traiteurs

* Affichage de la liste des traiteurs
* Consultation des détails d’un traiteur
* Ajout de traiteur via formulaire
* Upload d’image pour chaque traiteur
* Gestion de l’état des traiteurs : affichage de la liste des traiteurs vérifiés uniquement

### Authentification

* Connexion utilisateur (login)
* Déconnexion (logout)
* Protection des pages sensibles (login_required)
* Redirection automatique après connexion

### Expérience utilisateur

* Affichage dynamique des boutons (connexion / déconnexion)
* Navigation adaptée selon l’état de connexion
* Gestion des erreurs de connexion

## Technologies utilisées

* Python
* Django
* HTML
* CSS

## Dépendances importantes

* Pillow (gestion des images)

## Accès utilisateur

Certaines fonctionnalités comme l’ajout de traiteur nécessitent une authentification.
