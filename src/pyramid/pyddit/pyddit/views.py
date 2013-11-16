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

    return {'posts': posts}