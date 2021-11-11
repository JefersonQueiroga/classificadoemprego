from django.shortcuts import render
from .models import Cidade

# Create your views here.
def index(request):
    lista = Cidade.objects.all()
    return render(request,'main/lista.html',{'dados': lista})