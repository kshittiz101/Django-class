from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def experince(request):
    pass
