from django.shortcuts import render, redirect
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


def create(request):
    if request.method == "POST":
        print(request.method)
        pr_name = request.POST.get("name")
        pr_des = request.POST.get("description")
        pr_price = request.POST.get("price")
        # print(pr_name)
        # print(pr_des)
        # print(pr_price)

        # ORM
        Product.objects.create(
            name=pr_name, description=pr_des, price=pr_price
        )
        return redirect('home')

    return render(request, 'product/create.html')
