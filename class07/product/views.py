from django.shortcuts import render
from .models import Product

# Create your views here.


def home(request):
    # select * from table_name
    # orm
    products = Product.objects.all()
    # <QuerySet [<Product: Lava>, <Product: Iphone>]>
    # QuerySet --> collection or list of model instance
    # model instance --> actual data of the table
    print(products)
    context = {'key': products}
    # return render(request, 'product/index.html', {'key': products})
    return render(request, 'product/index.html', context=context)


def about(request):
    return render(request, 'product/about.html')
