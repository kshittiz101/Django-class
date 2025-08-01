from django.urls import path
# from .views import *
# from . import views
# from .views import home, login_page, register_page
from account.views import home, login_page, register_page

urlpatterns = [
    path('', home, name="home"),
    path('login/', login_page, name="login"),
    path('register/', register_page, name='register'),
]
