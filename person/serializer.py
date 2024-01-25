from rest_framework.serializers import ModelSerializer
from .models import Employee, Client
from rest_framework import serializers


class ClientSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = ('id', 'name', 'phone', 'debt', 'date')


class ClientCreateSerializer(serializers.Serializer):
    name = serializers.CharField()
    phone = serializers.CharField()
    debt = serializers.FloatField()
    date = serializers.DateField()


class EmployeeSerializer(ModelSerializer):

    class Meta:
        model = Employee
        fields = ('id',  'name', 'phone', 'password', )


class EmployeeCreateSerializer(serializers.Serializer):
    name = serializers.CharField()
    phone = serializers.CharField()
    password = serializers.CharField()
