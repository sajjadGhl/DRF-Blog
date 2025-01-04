from django.db import models
from posts.models import Post


class Category(models.Model):
    title = models.CharField(max_length=255)
    posts = models.ManyToManyField(Post, related_name='categories')

