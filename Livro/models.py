from django.db import models

# Create your models here.

class Livro(models.Model): 
    codigo = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    auto = models.CharField(max_length=100)
    preco = models.CharField(max_length=100)
