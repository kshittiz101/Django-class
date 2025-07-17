from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)  # string
    description = models.TextField()  # string
    price = models.IntegerField()  # number or interger types
    author = models.CharField(max_length=200)  # string
    gener = models.CharField(max_length=200, null=True, default="horror")

    def __str__(self):
        return self.title
