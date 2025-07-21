from django.contrib import admin
# from .models import Product

from product.models import Product

# Register your models here.

# 1st ways


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price']


# 2nd way
# admin.site.register(Product)

# 3rd way
# admin.site.register(ModelName, AdminClassName)
# admin.site.register(Product, ProductAdmin)
