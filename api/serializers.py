from rest_framework import serializers, validators

from api.models import ApiUser, Warehouse, Product


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[
            validators.UniqueValidator(ApiUser.objects.all())
        ]
    )
    password = serializers.CharField(min_length=6, max_length=20, write_only=True)
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

    def create(self, validated_data):
        if 'supplier' == validated_data.get('user_type'):
            product = Product.object.create()
            product.save()
        print(validated_data)
        return validated_data