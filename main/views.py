from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Cidade

def index(request):
    return render(request,'main/index.html')

# View para pegar cidades e retornar para url
def listar_cidades(request):
    lista = Cidade.objects.all()
    return render(request,'main/lista_cidades.html',{"cidades": lista })



def detalhe_cidade(request,pk):
   
    cidade = Cidade.objects.get(id=pk)

    return render(request,'main/detalhe_cidade.html',{"cidade": cidade})