from rest_framework import serializers
from .models import PedidoFornecedor

class PedidoFornecedorSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = PedidoFornecedor
        fields = "__all__"  
        
