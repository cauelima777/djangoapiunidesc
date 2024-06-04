from django.shortcuts import render
from rest_framework import generics
from .models import Pedido
from .serializers import PedidoSerializer
from rest_framework import viewsets
# Create your views here.

class PedidoView(viewsets.ModelViewSet): 

    query = Pedido.objects.all()
    serializer_clss = PedidoSerializer
