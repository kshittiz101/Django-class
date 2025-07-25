from django.urls import path
from .views import home, about

urlpatterns = [
    # syntax
    # path('unique_url/', view, name="")
    path('', home, name="home"),
    path('about/', about, name="about"),
]
