from rest_framework import serializers
from .models import Rim

class RimSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Rim
        fields = ('id', 'code', 'medico', 'created_at')