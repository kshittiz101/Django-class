from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User

from .models import Student
# Create your views here.


def home(request):
    return render(request, 'account/home.html')


def login_page(request):
    return render(request, 'account/login.html')


def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        reg_last_name = request.POST.get('last_name')
        reg_username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return HttpResponse('password not match')

        if User.objects.filter(email=email).exists():
            return HttpResponse('email is already exists')

        if User.objects.filter(username=reg_username).exists():
            return HttpResponse('username is already exists')

        User.objects.create_user(
            username=reg_username, first_name=first_name,
            last_name=reg_last_name, email=email,
            password=confirm_password
        )
        return redirect('home')

    return render(request, 'account/register.html')
