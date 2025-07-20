from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about-us.html')


def service(request):
    return render(request, 'main/service.html')
