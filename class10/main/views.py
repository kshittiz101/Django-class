from django.shortcuts import render
from .models import Product

# Create your views here.


def home(request):
    '''
    selet * from table_name;
    '''
   # orm :- Object Relational Mapping
    products = Product.objects.all()
    # <QuerySet [<Product: laptop>]>
    # Queryset => collection of model instance
    # <Product: laptop> => single instance of model
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')
