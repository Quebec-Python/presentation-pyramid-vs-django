from django.forms import ModelForm
from pyddit_app.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "url"]
