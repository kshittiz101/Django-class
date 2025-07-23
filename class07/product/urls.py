from django.urls import path
from .views import home, about


urlpatterns = [
    # path(unique_url, views, name="")
    path('', home, name="home"),
    path('about/', about, name="about"),
]
