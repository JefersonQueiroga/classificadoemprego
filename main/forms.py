from django.forms import ModelForm
from main.models import Cidade, Vaga 

class CidadeForm(ModelForm):
    class Meta:
        model= Cidade
        fields = '__all__'

class VagasForm(ModelForm):
    class Meta:
        model=Vaga
        fields = ['descricao']
