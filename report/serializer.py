from rest_framework.serializers import ModelSerializer
from .models import Order, Checkout
from person.serializer import ClientSerializer
from products.serializer import ProductSerializer
from rest_framework import serializers


class OrderSerializer(ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'total', 'quantity', 'product')


class OrderCreateSerializer(serializers.Serializer):
    total = serializers.FloatField()
    quantity = serializers.IntegerField()
    product = serializers.CharField()


class CheckoutSerializer(ModelSerializer):
    order = OrderSerializer(many=True)
    client = ClientSerializer(read_only=True)

    class Meta:
        model = Checkout
        fields = ('id', 'total', 'quantity', 'deadline', 'date_now', 'client', 'order', 'type_payment')


class CheckoutCreateSerializer(serializers.Serializer):
    total = serializers.FloatField()
    quantity = serializers.IntegerField()
    deadline = serializers.DateField()
    client = serializers.IntegerField()
    order = serializers.CharField()
    type_payment = serializers.IntegerField()