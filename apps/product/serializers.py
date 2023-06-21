from rest_framework import serializers
from .models import *
from ..order.models import Order


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    # images = ImageSerializer(many=True, read_only=True)
    id = serializers.IntegerField()

    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['images'] = ImageSerializer(instance.images.all(), many=True, context=self.context).data
        return rep

class ProductDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_id(self, value):
        if not Product.objects.filter(id=value).exists():
            raise serializers.ValidationError("Product with the specified ID does not exist.")
        return value

# class ProductImageSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = ProductImage
#         fields = '__all__'

    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     rep['product'] = ProductSerializer(instance.product).data
    #     return rep

    # def create(self, validated_data):
    #     image = self.context.get('image')
    #     if image is not None and 'request' in image:
    #         image = image['request'].FILES
    #     product = Product.objects.create(**validated_data)
    #     if image is not None:
    #         for img in image.values():
    #             ProductImage.objects.create(product=product, image=img)
    #     return product





class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
