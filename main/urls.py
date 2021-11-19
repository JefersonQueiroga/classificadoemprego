from django.urls import path
from .views import *

urlpatterns = [
   path('',index,name='index'),
   path('lista_cidades/',listar_cidades,name='lista_cidades'),
   path('detalhe_cidade/<int:pk>',detalhe_cidade,name='detalhe_cidade'),
   
] 
