from django.shortcuts import render, redirect

from pyddit_app.forms import PostForm

def home(request):
    context = {'hide_add_button': False}
    return render(request, 'index.html', context)

def add_post(request):
    context = dict(hide_add_button=True, form=PostForm())
    return render(request, 'add_post.html', context)

def get_post(request, hash_url):
    context = dict(hide_add_button=True)
    return render(request, 'get_post.html', context)

def vote_up(request, hash_url):
    return redirect("home")

def vote_down(request, hash_url):
    return redirect("home")
