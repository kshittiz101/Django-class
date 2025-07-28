from django.shortcuts import render
from .models import Student

# Create your views here.

# def ==> function


# def home(request):
#     return render(request, 'main/index.html')


# class based views
# fbv - Function based views
# function functionName(){}


def student_table(request):

    # Student ko all data fetch garnu xa vane talko code use garne
    # orm = modelName.objects.all()
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'crud/student-table.html', context)
