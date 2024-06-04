from django.db import models

# Create your models here.

class Fornecedor(models.Model): 
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cep = models.IntegerField()
    telefone = models.IntegerField()
    pedfor = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=100)

