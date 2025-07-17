from django.shortcuts import render

# Create your views here.

# function based view
# class based view


def home(request):
    return render(request, 'user/about.html')
