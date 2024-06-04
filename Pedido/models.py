from django.db import models

# Create your models here.


class Pedido(models.Model): 
    codigo = models.AutoField(primary_key=True)
    datapedido = models.DateField()
    listalivro = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    valor = models.FloatField()
