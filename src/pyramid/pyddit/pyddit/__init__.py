from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    )


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('vote_up', '/vote_up/{hash_url}')
    config.add_route('vote_down', '/vote_down/{hash_url}')
    config.add_route('add_post', '/add_post')
    config.add_route('add_post_submit', '/add_post_submit')
    config.add_route('get_post', '/post/{hash_url}')
    config.scan()
    return config.make_wsgi_app()
