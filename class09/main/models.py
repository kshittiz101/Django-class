from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)  # string 225
    desc = models.TextField()  # string
    price = models.IntegerField()  # number
