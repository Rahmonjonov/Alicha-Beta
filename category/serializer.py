from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Category


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'image', )


class CategoryCreateSerializer(serializers.Serializer):
    name = serializers.CharField()
    image = serializers.FileField()