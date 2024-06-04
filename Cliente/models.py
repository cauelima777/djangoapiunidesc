from django.db import models

# Create your models here.

class Cliente(models.Model): 
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    cep = models.IntegerField()
    telefone = models.IntegerField()
    pedido = models.CharField(max_length=100)
