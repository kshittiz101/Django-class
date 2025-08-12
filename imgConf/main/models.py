from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to='student_profile')

    def __str__(self):
        return self.name
