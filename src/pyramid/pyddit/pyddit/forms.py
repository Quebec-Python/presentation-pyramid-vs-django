# coding: utf-8

from wtforms_alchemy import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['votes', 'hash_url']