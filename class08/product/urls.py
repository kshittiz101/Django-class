from django.urls import path
from .views import home, about, create


urlpatterns = [
    # path(unique_url, views, name="")
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('create/', create, name="create"),
]
