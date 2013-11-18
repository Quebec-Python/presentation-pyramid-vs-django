# Pyddit avec Django

Chacune des commandes suivantes supposent que vous vous trouviez:

* dans le répertoire ```src/django``` si **vous n'utilisez pas** *Vagrant*
* dans le répertoire ```opt/django``` si **vous utilisez** *Vagrant*

## 1. Installation des dépendances

    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt

## 2. Initialisation de la base de données

    $ python manage.py migrate pyddit_app

## 3. Démarrer le serveur de développement

    !bash
    $ cd pyddit
    $ python manage.py runserver 0.0.0.0:8080

Vous pouvez maintenant admirer l'app à l'adresse suivante: [http://localhost:8080](http://localhost:8080)