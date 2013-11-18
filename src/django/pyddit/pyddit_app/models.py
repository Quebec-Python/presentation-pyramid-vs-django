from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=250, null=False)
    hash_url = models.CharField(max_length=255, db_index=True)
    url = models.URLField()
    votes = models.IntegerField(default=0)
