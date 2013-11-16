from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    Post
    )

@view_config(route_name='home', renderer='templates/index.pt')
def index(request):
    try:
        posts = DBSession.query(Post).all()
    except DBAPIError:
        return Response("error !", content_type='text/plain', status_int=500)

    return {'posts': posts, "hide_add_button": False}

@view_config(route_name="add_post", renderer="templates/add_post.pt")
def add_post(request):
    return {"hide_add_button": True}
