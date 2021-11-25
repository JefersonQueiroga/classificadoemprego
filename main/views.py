from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Cidade

def index(request):
    lista = Cidade.objects.all()
    return render(request,'index.html', context={ "cidades": lista})

def acai_bom(request):
    return HttpResponse("Açai 500g - Leite Condensaddo - Granola - Nutella")

def listagem_cidades( request ):
    lista = Cidade.objects.all()
    return render(request,'listar_cidades.html', context={ "cidades" : lista  })    

def detalhe( request, id_cidade  ):
    cidade = Cidade.objects.get(id= id_cidade )
    return render(request, 'main/detalhe.html', context={'cidade':cidade})  

def quem_somos(request):
    return render(request,'quem_somos.html')  