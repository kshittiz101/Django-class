from django.contrib import admin
from django.urls import path, include

# 1st ways
from main.views import home

# 2nd ways
from main import views

# 3rd ways (recommeded ways)


urlpatterns = [
    path('django-admin/', admin.site.urls),
    # syntax
    # path('unique_url/', view, name="")
    # path('', home, name="home"),
    # path('', views.home, name="home"),
    path('', include('main.urls')),
]
