from django.shortcuts import render

# Create your views here.

# def ==> function


# def home(request):
#     return render(request, 'main/index.html')


def student_table(request):

    return render(request, 'crud/student-table.html')
