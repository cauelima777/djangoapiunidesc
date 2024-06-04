from django.shortcuts import render
from rest_framework import generics
from .models import Cliente
from .serializers import ClienteSerializer
from rest_framework import viewsets
# Create your views here.

class ClienteView(viewsets.ModelViewSet): 

    query = Cliente.objects.all()
    serializer_clss = ClienteSerializer
