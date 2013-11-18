from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from sqlalchemy.exc import DBAPIError

import transaction

from .models import DBSession, Post
from .forms import PostForm
from .helpers import create_hashed_url

@view_config(route_name='home', renderer='templates/index.pt')
def index(request):
    try:
        posts = DBSession.query(Post).order_by("votes DESC")
    except DBAPIError:
        return Response("error !", content_type='text/plain', status_int=500)

    return {'posts': posts, "hide_add_button": False}

@view_config(route_name="get_post", renderer="templates/get_post.pt")
def get_post(request):
    hash_url = request.matchdict['hash_url']
    post = DBSession.query(Post).filter(Post.hash_url == hash_url).first()

    return {"post": post, "hide_add_button": True}

@view_config(route_name="add_post", renderer="templates/add_post.pt")
def add_post(request):
    return {"hide_add_button": True, "form": PostForm()}

@view_config(route_name="add_post_submit", request_method="POST", renderer="templates/add_post.pt")
def add_post_submit(request):
    post = Post()
    form = PostForm(request.POST, post)

    if request.POST and form.validate():
        form.populate_obj(post)
        post.hash_url = create_hashed_url(post.title)

        with transaction.manager:
            DBSession.add(post)

        # redirection
        url = request.route_url('home')
        return HTTPFound(location=url)

    return {"hide_add_button": True, "form": form}

@view_config(route_name="vote_up")
def vote_up(request):
    hash_url = request.matchdict['hash_url']
    post = DBSession.query(Post).filter(Post.hash_url == hash_url).first()

    if post:
        post.votes = post.votes + 1

        with transaction.manager:
            DBSession.add(post)

    # redirection
    url = request.route_url('home')
    return HTTPFound(location=url)

@view_config(route_name="vote_down")
def vote_down(request):
    hash_url = request.matchdict['hash_url']

    post = DBSession.query(Post).filter(Post.hash_url == hash_url).first()

    if post:
        post.votes = post.votes - 1

        with transaction.manager:
            DBSession.add(post)

    # redirection
    url = request.route_url('home')
    return HTTPFound(location=url)

