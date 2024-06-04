from django.shortcuts import render
from rest_framework import generics
from .models import PedidoCliente
from .serializers import PedidoClienteSerializer
from rest_framework import viewsets
# Create your views here.

class PedidoClienteView(viewsets.ModelViewSet): 

    query =  PedidoCliente.objects.all()
    serializer_clss = PedidoClienteSerializer
