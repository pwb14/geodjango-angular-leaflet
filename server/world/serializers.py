from .models import WorldBorder
from rest_framework import serializers

class WorldBorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorldBorder
        fields = ['name', 'un']