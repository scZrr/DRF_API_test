# from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Engineer
from .serializers import EngineerSerializer


# Create your views here.
class EngineerViewSet(viewsets.ModelViewSet):
    queryset = Engineer.objects.all()
    serializer_class = EngineerSerializer
