from django.urls import path
from .views import student_table, register_student
urlpatterns = [
    path('stud-table/', student_table, name="student-table"),
    path('register/', register_student, name="register"),
]
