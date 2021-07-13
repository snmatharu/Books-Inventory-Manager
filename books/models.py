from django.db import models
from django.db.models.fields import TimeField
from django.utils import timezone


class Addbooks(models.Model):
    title = models.CharField(max_length=100,unique=False, default='Not Provided')
    author = models.CharField(max_length=100,unique=False, default='Not Provided')
    # file = models.FileField()
    # time = models.DateTimeField(auto_now=False, auto_now_add=True)
    genre = models.CharField(max_length=100,unique=False, default='Not Provided')
    language = models.CharField(max_length=100,unique=False, default='Not Provided')
