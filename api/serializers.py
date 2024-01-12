from rest_framework import serializers

from api.models import ApiUser, Warehouse, Product


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiUser
        fields = ['email', 'password', 'user_type']
        extra_kwargs = {'id': {'read_only': True}}


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}