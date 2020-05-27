from django.db import models

class BlogPost(models.model):
    title = models.TextField()
    content = models.TextField(null=True, blank=True)
