from django.shortcuts import render, redirect
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
    context = {'keys': students}
    return render(request, 'crud/student-table.html', context)


def register_student(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        # orm --> modelName.objects.create(modelAttributes=Value )

        success = Student.objects.create(
            stu_name=name, stu_age=age,
            stu_email=email, gender=gender
        )
        if success:
            return redirect('student-table')

    return render(request, 'crud/student-register.html')
