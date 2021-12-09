from django.urls import path
from .views import *

urlpatterns = [
   path('',index,name='index'),
   path('listar_cidades/',listagem_cidades,name='listar_cidades'),
   path('form_cidade/',cadastrar_cidade,name='cadastrar_cidade'),
   path('detalhe_cidade/<int:id_cidade>/', detalhe, name='detalhe_cidade'),
   path('quem_somos/', quem_somos ,name='quem_somos'),
] 
