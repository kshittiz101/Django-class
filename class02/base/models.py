from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
# model => table, which store related data
# python => conditionals, function, loops, datatypes, oops


class Student(models.Model):
    GENDER_CHOICES = [
        #
        # tuple -> key value vako data types ho, tara immutable in nature hunxa
        # syntax
        # ('key', 'value')

        ('Male', 'MALE'),
        ('Female', 'FEMALE'),
        ('Others', 'OTHERS'),
    ]
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=20)

    def __str__(self):
        return self.name
