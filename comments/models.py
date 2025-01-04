from django.db import models
from authentication.models import User
from posts.models import Post


class Comment(models.Model):
    content = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=False, related_name='comments')
