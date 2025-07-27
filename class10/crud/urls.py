from django.urls import path
from .views import student_table
urlpatterns = [
    path('stud-table/', student_table, name="student-table"),
]
