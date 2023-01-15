from rest_framework import viewsets
from .models import Engineer, Manager
from .serializers import EngineerSerializer, ManagerSerializer


class EngineerViewSet(viewsets.ModelViewSet):
    queryset = Engineer.objects.all()
    serializer_class = EngineerSerializer


class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
