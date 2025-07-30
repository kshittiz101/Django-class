from django.urls import path
from .views import student_table, register_student, update_student, student_delete
urlpatterns = [
    path('stud-table/', student_table, name="student-table"),
    path('register/', register_student, name="register"),
    path('update/<int:pk>/', update_student, name="update"),
    path('delete/<int:pk>/', student_delete, name="delete"),
]
