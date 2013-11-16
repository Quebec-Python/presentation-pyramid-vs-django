# Pyddit avec Pyramid

Chacune des commandes suivantes supposent que vous vous trouviez dans le répertoire ```src/pyramid```.

## 1. Installation des dépendances

    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt

## 2. Installation du projet *pyddit*

    $ cd pyddit
    $ python setup.py develop

## 3. Initialisation de la base de données

    $ cd pyddit/pyddit
    $ alembic upgrade head

## 4. Démarrer le serveur de développement

    $ cd pyddit
    $ pserve development.ini

Vous pouvez maintenant admirer l'app à l'adresse suivante: [http://localhost:6543](http://localhost:6543)