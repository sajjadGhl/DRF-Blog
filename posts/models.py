from django.db import models
from authentication.models import User
from django_jalali.db import models as jmodels
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, max_length=255)
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_at = jmodels.jDateTimeField(default=timezone.now)


