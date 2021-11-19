from django.urls import path
from .views import *

urlpatterns = [
   path('',index,name='index'),
   path('acai/',acai_bom,name='acai'),
   
] 
