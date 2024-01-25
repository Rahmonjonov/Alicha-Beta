from rest_framework.serializers import ModelSerializer
from category.serializer import CategorySerializer
from .models import *
from rest_framework import serializers


class ProductSerializer(ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'product_name', 'barcodes', 'purchase_price', 'sel_price', 'quantity', 'image', 'category', )


class ProductCreateSerializer(serializers.Serializer):
    product_name = serializers.CharField()
    barcodes = serializers.IntegerField()
    purchase_price = serializers.FloatField()
    sel_price = serializers.FloatField()
    quantity = serializers.IntegerField()
    image = serializers.FileField()
    category_id = serializers.IntegerField()


class ProductFileterCategorySerializer(serializers.Serializer):
    category = serializers.Serializer()


class ProductFileterBarcodesSerializer(serializers.Serializer):
    barcodes = serializers.Serializer()
