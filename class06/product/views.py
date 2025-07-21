from django.shortcuts import render
from .models import Product

# Create your views here.


def home(request):
    products = Product.objects.all()
    # Queryset => collection or list of query instance or model instance
    # model intance => actual value or object
    # <QuerySet [<Product: Laptop>, <Product: Mobile>]>
    print(products)
    context = {'key': products, 'course': 'Django'}

    # return render(request, 'product/index.html', {'products': products})
    return render(request, 'product/index.html', context=context)
