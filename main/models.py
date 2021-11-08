from django.db import models

class Cidade (models.Model):
    nome = models.CharField(max_length=150)
    sigla_estado = models.CharField(max_length=2)

class Empresa (models.Model):
    nome = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=15)
    telefone = models.CharField(max_length=15)
    endereco =models.CharField(max_length=15)
    cidade = models.ForeignKey(Cidade,on_delete=models.CASCADE) 


class TipoVaga (models.Model):
    nome = models.CharField(max_length=150)
   

class Vaga(models.Model):
    descricao = models.TextField()
    salario = models.DecimalField(max_digits=8, decimal_places=2)
    quantidade_vagas = models.IntegerField()
    escolaridade_exigida = models.CharField(max_length=150)
    data_inscricao = models.DateTimeField()
    cidade = models.ForeignKey(Cidade,on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE)
    tipo_vaga = models.ForeignKey(TipoVaga,on_delete=models.CASCADE)