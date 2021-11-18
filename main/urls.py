from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('recebe_texto/<str:texto>/', numero_recebido, name='numero_recebido'),
    path('lista_cidades/', lista_cidades, name='lista_cidades'),
] 



