
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('conta/login/', my_login ,name="login"),
    path('conta/logout/', logout_request, name='logout'),
    path("conta/registrar/", register, name="register")

  ] 
