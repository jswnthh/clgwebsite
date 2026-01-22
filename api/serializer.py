from rest_framework import serializers
from core.models import PersonDb

class Serializer(serializers.ModelSerializer):
    class Meta:
        model = PersonDb
        fields = '__all__'