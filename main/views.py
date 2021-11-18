from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Cidade

def index(request):
    return render(request,'main/index.html')

def numero_recebido(request,texto):
    return HttpResponse("Valor passado: " + texto )

def lista_cidades(request):
    lista = Cidade.objects.all()
    return render(request, 'main/listagem_cidades.html', context={"cidades": lista} )


