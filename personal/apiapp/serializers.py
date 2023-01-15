from rest_framework import serializers

from .models import Engineer, Manager


class EngineerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engineer
        fields = ('__all__')


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ('__all__')