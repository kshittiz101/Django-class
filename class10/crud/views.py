from django.shortcuts import render, redirect, get_object_or_404
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


def update_student(request, pk):

    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        update_name = request.POST.get('update-name')
        update_age = request.POST.get('update-age')
        update_email = request.POST.get('update-email')
        update_gender = request.POST.get('update-gender')

        # orm update (error )
        # update_status = Student.objects.update(
        #     stu_name=update_name, stu_age=update_age,
        #     stu_email=update_email, gender=update_gender
        # )

        # actual ways of updating data
        student.stu_name = update_name
        student.stu_age = update_age
        student.stu_email = update_email
        student.gender = update_gender
        student.save()
        return redirect('student-table')

    # sunil@gmail.com
    # print(student)
    context = {'key': student}

    return render(request, 'crud/student-update.html', context)


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student-table')
