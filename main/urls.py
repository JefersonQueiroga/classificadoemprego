from django.urls import path
from .views import *

urlpatterns = [
   path('',index,name='index'),
   path('listar_cidades/',listagem_cidades,name='listar_cidades'),
   path('detalhe_cidade/<int:id_cidade>/', detalhe, name='detalhe_cidade'),
   path('quem_somos/', quem_somos ,name='quem_somos'),
   path('form_cidade/',criar_cidade,name='criar_cidade'),
   path('form_vagas/',criar_vagas, name='criar_vagas'),
   path('lista_vagas/',lista_vagas, name="lista_vagas"),
   path('editar_vagas/<int:id_vaga>/',editar_vagas,name='editar_vagas')
] 
