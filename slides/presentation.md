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

<img src="static/img/streetfighter.jpg" style="width:auto; display:block;">

---

# Round 1: la procédure d'installation

---

## Installation de Pyramid

    !bash
    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install pyramid

## Installation de Django

    !bash
    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install django

---

# Round 2: Démarrer un projet

---

## Démarrage de projet sous Pyramid

    !bash
    $ pcreate -s starter pyddit

pour installer SQLAlchemy dès le départ:

    !bash
    $ pcreate -s alchemy pyddit

## Démarrage de projet sous Django

    !bash
    $ python manage.py startproject pyddit
    $ python manage.py startapp pyddit_app

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

    !python
    from django.db import models

    class Post(models.Model):
        title = models.CharField(
            max_length=250, null=False
        )
        hash_url = models.CharField(
            max_length=255, db_index=True
        )
        url = models.URLField()
        votes = models.IntegerField(default=0)

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

Autogénération de nos models en début de projet:

    !bash
    $ python manage.py syncdb
    $ python manage.py schemamigration pyddit_app --initial
    $ python manage.py migrate pyddit_app

Création d'une nouvelle migration:

    !bash
    $ python manage.py schemamigration southtut --auto

Upgrader/Downgrader:

    !bash
    # Je ne le trouve pas dans la documentation !

---

# Round 5: Démarrer le serveur de développement

---

## Serveur de dév. sous Pyramid

    !bash
    $ pserver development.ini

## Serveur de dév. sous Django

    !bash
    $ python manage.py runserver 0.0.0.0:8080

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
        config.add_route('home', '/')
        config.add_route(
            'vote_up', '/vote_up/{hash_url}'
        )
        config.scan()
        return config.make_wsgi_app()

---

## Routing sous Django

pyddit/urls.py:

    !python
    from django.conf.urls import patterns, include, url

    urlpatterns = patterns('pyddit_app.views',
        # url(r'^admin/', include(admin.site.urls)),
        url(r'^$', 'home', name="home"),
        url(r'^vote_up/(?P<hash_url>.+)$', 'vote_up', name="vote_up"),
        url(r'^vote_down/(?P<hash_url>.+)$', 'vote_down', name="vote_down"),
        url(r'^add_post$', 'add_post', name="add_post"),
        url(r'^post/(?P<hash_url>.+)$', 'get_post', name="get_post"),
    )

---

# Round 7: Views (a.k.a. controllers)

---

## Views sous Pyramid

    !python
    from pyramid.response import Response
    from pyramid.view import view_config
    from .models import DBSession, Post

    @view_config(
        route_name='home',
        renderer='templates/index.pt'
    )
    def home(request):
        posts = DBSession.query(Post).order_by(
            "votes DESC"
        )
        return {'posts': posts, "hide_add_button": False}

---

## Views sous Django

    !python
    from django.shortcuts import render, redirect
    from pyddit_app.models import Post

    def home(request):
        context = {
            'hide_add_button': False,
            "posts": Post.objects.all().order_by("-votes")
        }
        return render(request, 'index.html', context)

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

Template de base:

    !html
    <!DOCTYPE html>
    <html>
        <head></head>
        <body>
            {% block content %}
            {% endblock %}
        </body>
    </html>

---

## Templates sous Django partie 2

Template héritant de base.html:

    !html
    {% extends "base.html" %}
    {% block content %}
        du contenu !
    {% endblock %}

---

# Ce que je n'ai pas couvert

* Mise en production (WSGI)
* Protection contre le *Cross-site request forgery*
* Déploiement des fichiers statiques

---

# Questions ?

## Commentaires/Bashing ?

---

# Merci !

* Je pars en cavale et j'apporte: ma guitare
* Film que je regarderai éternellement: Mononoke Hime
* bernardchhun.com
