from django.shortcuts import render, redirect

from pyddit_app.forms import PostForm
from pyddit_app.models import Post
from pyddit_app.helpers import create_hashed_url

def home(request):
    context = {
        'hide_add_button': False,
        "posts": Post.objects.all().order_by("-votes")
    }
    return render(request, 'index.html', context)

def add_post(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            url = form.cleaned_data['url']

            post = Post(
                title = title,
                hash_url = create_hashed_url(title),
                url = url
            )
            post.save()

            return redirect("home")
    else:
        form = PostForm()

    context = dict(hide_add_button=True, form=form)

    return render(request, 'add_post.html', context)

def get_post(request, hash_url):
    context = dict(
        hide_add_button = True,
        post = Post.objects.get(hash_url=hash_url)
    )
    return render(request, 'get_post.html', context)

def vote_up(request, hash_url):
    post = Post.objects.get(hash_url=hash_url)

    if post:
        post.votes += 1
        post.save()

    return redirect("home")

def vote_down(request, hash_url):
    post = Post.objects.get(hash_url=hash_url)

    if post:
        post.votes -= 1
        post.save()

    return redirect("home")
