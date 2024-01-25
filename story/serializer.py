from rest_framework.serializers import ModelSerializer
from .models import StoreAbout, DebtMarket, Cost
from rest_framework import serializers


class StoreAboutSerializer(ModelSerializer):

    class Meta:
        model = StoreAbout
        fields = ('id', 'name', 'plastic_number', 'address')


class StoreAboutCreateSerializer(serializers.Serializer):
    name = serializers.CharField()
    plastic_number = serializers.IntegerField()
    address = serializers.CharField()


class DebtMarketSerializer(ModelSerializer):

    class Meta:
        model = DebtMarket
        fields = ('id', 'name', 'price', 'deadline', 'date',)


class DebtMarketCreateSerializer(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.FloatField()
    deadline = serializers.DateField()
    date = serializers.DateField()


class CostSerializer(ModelSerializer):

    class Meta:
        model = Cost
        fields = ('id',  'name', 'price', 'extra', 'date')


class CostCreateSerializer(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.FloatField()
    extra = serializers.CharField()