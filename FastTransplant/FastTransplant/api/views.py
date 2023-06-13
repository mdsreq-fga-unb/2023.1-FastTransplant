from django.shortcuts import render
from rest_framework import generics
from .serializers import RimSerializer
from .models import Rim

# Create your views here

class RimView(generics.ListAPIView):
    queryset = Rim.objects.all()
    serializer_class = RimSerializer



