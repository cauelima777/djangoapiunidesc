from django.shortcuts import render
from rest_framework import generics
from .models import Fornecedor
from .serializers import FornecedorSerializer
from rest_framework import viewsets
# Create your views here.

class FornecedorView(viewsets.ModelViewSet): 

    query = Fornecedor.objects.all()
    serializer_clss = FornecedorSerializer
