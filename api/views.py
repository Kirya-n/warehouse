from django.shortcuts import render
from rest_framework import viewsets, permissions

from api.models import ApiUser
from api.serializers import UserSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = ApiUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]