from rest_framework import serializers # type: ignore
from .models import Apiary, Hive

class HiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hive
        fields = '__all__'

class ApiarySerializer(serializers.ModelSerializer):
    hives = HiveSerializer(many=True, read_only=True)

    class Meta:
        model = Apiary
        fields = '__all__'