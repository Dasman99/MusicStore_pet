from rest_framework import serializers
from .models import *
from ..order.models import Order


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField()

    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    # image = ImageSerializer()

    class Meta:
        model = Product
        fields = '__all__'

    def validate(self, data):
        if 'image' not in data or not data['image']:
            raise serializers.ValidationError('At least one image is required')
        print(data)
        return data

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['image'] = ImageSerializer(instance.images.all(), many=True, context=self.context).data
        return rep

    def create(self, validated_data):
        # print(validated_data)
        image = validated_data.pop('image')
        # print(image)
        product = Product.objects.create(**validated_data)
        if image:
            ProductImage.objects.bulk_create([ProductImage(product=product, **img) for img in image])
        return product


# class ProductImageSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Product
#         fields = '__all__'
#
#     # def validate(self, data):
#     #     if 'image' not in data or not data['image']:
#     #         raise serializers.ValidationError('At least one image is required')
#     #     print(data)
#     #     return data
#
#     # def to_representation(self, instance):
#     #     rep = super().to_representation(instance)
#     #     rep['images'] = ProductImageSerializer(instance.images.all(), many=True, context=self.context).data
#     #     return rep
#
#     def create(self, validated_data):
#         print(validated_data)
#         images = validated_data.pop('image')
#         print(images)
#         product = Product.objects.create(**validated_data)
#         if images:
#             ProductImage.objects.bulk_create([ProductImage(product=product, **img) for img in images])
#         return product


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
