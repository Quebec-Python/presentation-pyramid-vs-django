# QuébecPython: 2e édition

## Pyramid VS Django: construction d'un clone grandement simplifié de Reddit

### affectueusement nommé *Pyddit*...

###### Oui, je sais. Reddit est déjà monté en Python.

---

# But de la présentation ??

* Démontrer scientifiquement que Django est mieux que Pyramid
* Foutre le feu dans des frameworks qui souillent des noms de musiciens connus

---

<img src="static/img/hellogrumpy.jpg" style="width:auto; display:block;">

---

# But de la présentation

* Démontrer toutes les étapes de construction d'une app fictive sous Pyramid et Django
* Cerner les différences entre ces 2 frameworks pour faire un choix éclairé lors de la construction de notre prochaine app web

---

# Les spécifications de Pyddit

* Soumettre des liens de façon anonyme
* Système de vote anonyme
* Ordonner les liens par plus grand nombre de vote

---

# Round 1: la procédure d'installation

---

## Installation de Pyramid

    !bash
    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install pyramid


---

## Installation de Django

    !bash
    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install django

---

# Round 2: Démarrer un projet

---

## Démarrage sous Pyramid

    !bash
    $ pcreate -s starter pyddit

pour installer SQLAlchemy dès le départ:

    !bash
    $ pcreate -s alchemy pyddit

---

## Démarrage sous Django

    TODO

---

# Round 3: Les models

---

## Models sous Pyramid / SQLAlchemy

    !python
    import sqlalchemy as sa
    from sa.ext.declarative import declarative_base
    Base = declarative_base()

    class Post(Base):
        __tablename__ = "posts"
        id = sa.Column(sa.Integer, primary_key=True)
        title = sa.Column(sa.String(250), nullable=False)


---

## Models sous Django

    TODO: django orm

---

# Round 4: Migration

---

## Migration sous Pyramid / Alembic

Autogénération de nos models en début de projet:

    !bash
    $ alembic revision --autogenerate -m "blabla"

Création d'une nouvelle révision:

    !bash
    $ alembic revision -m "une révision"

Upgrader/Downgrader:

    !bash
    $ alembic upgrade +2 # head
    $ alembic downgrade -1 # base

---

## Migration sous Django / South

    TODO: South

---

# Round 5: Démarrer le serveur de développement

---

## Serveur de dév. sous Pyramid

    !bash
    $ pserver development.ini

---

## Serveur de dév. sous Django

    TODO

---

# Round 6: Routing

---

## Routing sous Pyramid

pyddit/__init__.py:

    !python

    def main(global_config, **settings):
        # engin de templating
        config.include('pyramid_chameleon')
        # path vers les fichiers static
        config.add_static_view(
            'static', 'static', cache_max_age=3600
        )
        # la page d'accueil
        config.add_route('home', '/')
        config.scan()
        return config.make_wsgi_app()

---

## Routing sous Django

    TODO

---

# Round 7: Views (a.k.a. controllers)

---

## Views sous Pyramid

    !python
    from pyramid.response import Response
    from pyramid.view import view_config

    @view_config(
        route_name='home',
        renderer='templates/index.pt'
    )
    def home(request):
        return Response("home !")

---

## Views sous Django

    TODO

---

# Round 8: Templates

---

## Templates sous Pyramid / Chameleon

Template de base:

    !html
    <!DOCTYPE
        html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml"
        xml:lang="en"
        xmlns:tal="http://xml.zope.org/namespaces/tal">
        <head></head>
        <body>
            <metal:content define-slot="content" />
        </body>
    </html>

---

## Templates sous Pyramid / Chameleon part. 2

Template héritant de base.pt:

    !html
    <metal:main use-macro="load: base.pt">
        <div metal:fill-slot="content">
            <ul>
                <li tal:repeat="billet billets">
                    ${billet.title}
                </li>
            </ul>
        </div>
    </metal:main>

---

## Templates sous Django

    TODO

---

# Questions ?

## Commentaires/Bashing ?

---

# Merci !

* Je pars en cavale et j'apporte: ma guitare
* Film que je regarderai éternellement: Mononoke Hime
* bernardchhun.com
