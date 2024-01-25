from .models import User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    phone_model = serializers.CharField()
    limit = serializers.CharField()
    shop_name = serializers.CharField()
    first_name = serializers.CharField()


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'phone_model', 'shop_name', 'used_limit', 'first_name', 'limit', 'created_at',)

