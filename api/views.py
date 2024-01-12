from django.shortcuts import render
from rest_framework import viewsets, permissions

from api.models import ApiUser, Warehouse, Product
from api.serializers import UserSerializer, WarehouseSerializer, ProductSerializer


# Create your views here.
class UserModelViewSet(viewsets.ModelViewSet):
    queryset = ApiUser.objects.all()
    serializer_class = UserSerializer


class WarehouseModelViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = ProductSerializer