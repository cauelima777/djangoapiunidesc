from django.db import models

# Create your models here.

class PedidoFornecedor(models.Model): 
    codfornecedor = models.AutoField(primary_key=True)
    datarecebimento = models.DateField()
    