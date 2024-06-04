from django.shortcuts import render
from rest_framework import generics
from .models import Livro
from .serializers import LivroSerializer
from rest_framework import viewsets
# Create your views here.

class LivroView(viewsets.ModelViewSet): 

    query = Livro.objects.all()
    serializer_clss = LivroSerializer
