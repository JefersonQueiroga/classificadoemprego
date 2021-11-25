from django.urls import path
from .views import *

urlpatterns = [
   path('',index,name='index'),
   path('pagina_teste',pagina_teste,name='pagina_teste'),
   path('listar_cidades/',listagem_cidades,name='listar_cidades'),
   path('detalhe_cidade/<int:id_cidade>/', detalhe, name='detalhe_cidade'),
] 
