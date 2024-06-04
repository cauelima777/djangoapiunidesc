from rest_framework import serializers
from .models import Balconista

class BalconistaSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Balconista
        fields = "__all__"  
        
