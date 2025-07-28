from django.contrib import admin
from .models import Student

# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'stu_name', 'stu_age', 'stu_email', 'gender']
    search_fields = ['stu_name',  'stu_email']
