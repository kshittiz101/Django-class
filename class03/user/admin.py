from django.contrib import admin
# from .models import Book
from user.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'author', 'gener']
    search_fields = ['title', 'gener']
