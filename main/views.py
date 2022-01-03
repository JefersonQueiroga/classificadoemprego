from django.http.response import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from main.forms import CidadeForm,VagasForm
from .models import Vaga,Cidade
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    vagas = Vaga.objects.all()
    return render(request,'index.html', context={"vagas": vagas })




# entrar primeira para pegar o formulário
# e segunda para salvar
def criar_cidade(request):
    
    if request.method == 'GET':
        form = CidadeForm()
        context = { 'primeiro_form': form }
        return render(request,'main/form_cidade.html',context)
    else:
        form = CidadeForm(request.POST)

        if form.is_valid():
            form.save()  
            form = CidadeForm()
            messages.success(request, 'Cidade Cadastrada com Sucesso!')

        context = { 'primeiro_form': form } 
        return render(request,'main/form_cidade.html',context)

def criar_vagas(request):
    if request.method == 'GET':
        form = VagasForm() 
        context = {'form': form}
        return render(request,'main/form_vagas.html',context)
    else:
        form = VagasForm(request.POST)
        if form.is_valid():
            form.save()
            form = VagasForm()

        context = {'form': form}
        return render(request,'main/form_vagas.html',context)

@login_required
def lista_vagas(request):
    vagas = Vaga.objects.all()
    return render(request,'main/listar_vagas.html', context={"vagas": vagas })

@login_required
def editar_vagas (request,id_vaga):
    vaga = get_object_or_404(Vaga, pk=id_vaga) # traz a vaga pelo id passado.
    
    if request.method == 'POST':
        form = VagasForm(request.POST,instance=vaga)
        if form.is_valid():
            form.save()
            return redirect('lista_vagas')
    else:
        form = VagasForm(instance=vaga)        

## criando e preenchendo o formulário
    return render(request,'main/form_vagas.html', context={"form": form })


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