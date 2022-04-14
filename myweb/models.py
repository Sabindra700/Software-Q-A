
from django.db import models
class Person(models.Model):
    Name = models.CharField(max_length=64)
    Surname = models.CharField(max_length=64)
    email = models.EmailField('Email Address', blank=True)

