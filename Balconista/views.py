from django.shortcuts import render
from rest_framework import generics
from .models import Balconista
from .serializers import BalconistaSerializer
from rest_framework import viewsets
# Create your views here.

class BalconistaView(viewsets.ModelViewSet): 

    query = Balconista.objects.all()
    serializer_clss = BalconistaSerializer
