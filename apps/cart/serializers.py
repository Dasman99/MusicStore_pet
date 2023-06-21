from rest_framework import serializers

from .models import *
from apps.product.serializers import ImageSerializer


class CartProductSerializer(serializers.HyperlinkedModelSerializer):
    products = ImageSerializer(many=True)

    class Meta:
        model = CartItem
        fields = '__all__'


class CartSerializer(serializers.HyperlinkedModelSerializer):
    cart_item = CartProductSerializer(many=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Cart
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    cart = CartSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'