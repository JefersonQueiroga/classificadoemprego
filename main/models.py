from django.db import models
from django.contrib.auth.models import User


class Cidade (models.Model):
    nome = models.CharField(max_length=150)
    sigla_estado = models.CharField(max_length=2)

    def __str__(self):
        return self.nome

class Empresa (models.Model):
    nome = models.CharField(max_length=150,blank=False)
    cnpj = models.CharField(max_length=15,blank=False)
    telefone = models.CharField(max_length=15,blank=True)
    endereco =models.CharField(max_length=150,blank=True)
    cidade = models.ForeignKey(Cidade,on_delete=models.CASCADE)
    image = models.FileField(upload_to='imagens/',blank=True)


class TipoVaga (models.Model):
    nome = models.CharField(max_length=150)
    
    def __str__(self):
        return self.nome

class Vaga(models.Model):
    descricao = models.TextField()
    salario = models.DecimalField(max_digits=8, decimal_places=2)
    quantidade_vagas = models.IntegerField()
    escolaridade_exigida = models.CharField(max_length=150)
    data_inscricao = models.DateTimeField()
    cidade = models.ForeignKey(Cidade,on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE)
    tipo_vaga = models.ForeignKey(TipoVaga,on_delete=models.CASCADE)
    usuarios = models.ManyToManyField(User)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descricao