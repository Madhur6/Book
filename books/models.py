from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)