from django.db import models

# Create your models here.
# models ==> table
# relatioships
# database relations
# one to one
# many to many
# one to many (foregin key)
# many to one (foregin key)



class Student(models.Model):
 name = models.CharField(max_length=200)
 age = models.IntegerField()
 email = models.EmailField(unique=True)

 def __str__(self):
  return self.name



# one to one relationships use
# Single table ko data lai more information gather gara help garxa

# Sinle data of 1st table is related to single data of another table data
# is called one to one relationship

class StudentProfile(models.Model):
 student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="student_profile")
 address = models.CharField(max_length=200)
 mobile_number = models.CharField(max_length=10)

 def __str__(self):
  return self.mobile_number


# one to many or many to one (foreign key)

# signle data of 1st table is related with 2 or more data of another table so this types of
# relation is called one to many or many to one relationship
class ClassTable(models.Model):
 student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='stu_class', null=True)
 class_name = models.CharField(max_length=200, default="null")
 section = models.CharField(max_length=200, default='null')

 def __str__(self):
  return self.class_name


# many to many
# if 1 or more data of 1st table is in relation with 1 or more data of another table such types of
# relationships is called many to many

class Coures(models.Model):
 student = models.ManyToManyField(Student)
 coures_name = models.CharField(max_length=200)
 coures_price = models.CharField(max_length=200)

 def __str__(self):
  return self.coures_name
