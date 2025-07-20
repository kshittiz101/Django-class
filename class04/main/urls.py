from django.urls import path
from .views import home, about, experince

urlpatterns = [
    path('', home),
    path('about/', about),
    path('experince/', experince)
]
