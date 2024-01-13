from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from api.models import ApiUser, Warehouse, Product
from api.serializers import UserSerializer, WarehouseSerializer, ProductSerializer


# Create your views here.
class UserModelViewSet(viewsets.ModelViewSet):
    queryset = ApiUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class WarehouseModelViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @login_required
    @permission_required('api.add_product', raise_exception=True)
    def add_product(self, request):
        print(request)