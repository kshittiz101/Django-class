from django.contrib import admin
from .models import Student, StudentProfile, ClassTable, Coures

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
 list_display = ['id','name','age','email']


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
 list_display = ['student','address','mobile_number']

@admin.register(ClassTable)
class ClassTableAdmin(admin.ModelAdmin):
 list_display = ['id','student','class_name', 'section']

@admin.register(Coures)
class CoursesAdmin(admin.ModelAdmin):
 list_display = ['id', 'coures_name', 'coures_price']
