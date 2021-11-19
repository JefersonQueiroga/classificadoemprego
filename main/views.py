from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Cidade

def index(request):
    lista = Cidade.objects.all()
    return render(request,'main/index.html', context={ "cidades": lista})

def acai_bom(request):
    return HttpResponse("Açai 500g - Leite Condensaddo - Granola - Nutella")