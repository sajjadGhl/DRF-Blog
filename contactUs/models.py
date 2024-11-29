from django.db import models
from django_jalali.db import models as jmodels


class ContactUs(models.Model):
    name = models.CharField(max_length=63)
    email = models.EmailField()
    message = models.TextField()
    created_at = jmodels.jDateTimeField(auto_now_add=True)


