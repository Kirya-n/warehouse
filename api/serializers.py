from rest_framework import serializers

from api.models import ApiUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiUser
        fields = ['email', 'password', 'user_type']

