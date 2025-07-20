from django.urls import path
from .views import home, about, service

urlpatterns = [
    # syntax
    # path(unique-url-path, view, name="")
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("service/", service, name="service"),
]
