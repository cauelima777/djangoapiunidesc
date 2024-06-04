from django.shortcuts import render
from rest_framework import generics
from .models import PedidoFornecedor
from .serializers import PedidoFornecedorSerializer
from rest_framework import viewsets
# Create your views here.

class PedidoFornecedorView(viewsets.ModelViewSet): 

    query =  PedidoFornecedor.objects.all()
    serializer_clss = PedidoFornecedorSerializer
