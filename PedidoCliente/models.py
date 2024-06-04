from django.db import models

# Create your models here.

class PedidoCliente(models.Model): 
    codigo = models.AutoField(primary_key=True)
    dataremessa = models.DateField()

    