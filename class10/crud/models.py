from django.db import models

# Create your models here.
# model => table
# tuple
# ('key', 'value')


class Student(models.Model):
    GERDER_CHOICES = [
        ('male', 'male'),
        ('female', 'female'),
        ('others', 'others'),
    ]
    stu_name = models.CharField(max_length=100)
    stu_age = models.IntegerField()
    stu_email = models.EmailField(unique=True)
    gender = models.CharField(choices=GERDER_CHOICES, max_length=50)
