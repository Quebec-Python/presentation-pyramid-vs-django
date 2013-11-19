from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=250, null=False, blank=False)
    hash_url = models.CharField(max_length=255, db_index=True)
    url = models.URLField(null=False, blank=False)
    votes = models.IntegerField(default=0)
