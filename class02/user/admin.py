from django.contrib import admin
# from .models import Student
# syntax
# with the help of app name
# from appName.models improt modelName

from user.models import Student

# Register your models here.
# 1st way
# admin.site.register(Student)


# 2nd way (using decorators)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'email', 'gender']
    search_fields = ['name', 'email']
    ordering = ['name']
