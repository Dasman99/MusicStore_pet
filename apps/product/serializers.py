from rest_framework import serializers
from .models import *
from ..order.models import Order


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# class ImageSerializer(serializers.ModelSerializer):
#     image = serializers.ImageField()
#
#     class Meta:
#         model = ProductImage
#         fields = ('image')


# class ProductSerializer(serializers.ModelSerializer):
#     # image = ImageSerializer(many=True)
#
#     class Meta:
#         model = Product
#         fields = '__all__'

    # def validate(self, data):
    #     if 'image' not in data or not data['image']:
    #         raise serializers.ValidationError('At least one image is required')
    #     print(data)
    #     return data

    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     rep['image'] = ImageSerializer(instance.images.all(), many=True, context=self.context).data
    #     return rep
    #
    # def create(self, validated_data):
    #     # print(validated_data)
    #     image = validated_data.pop('image')
    #     # print(image)
    #     product = Product.objects.create(**validated_data)
    #     if image:
    #         ProductImage.objects.bulk_create([ProductImage(product=product, **img) for img in image])
    #     return product

class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    # image = ImageSerializer(many=True, read_only=False)

    class Meta:
        model = Product
        fields = '__all__'

    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     rep['product_images'] = ImageSerializer(instance.images.all(), many=True, context=self.context).data
    #     return rep


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['images'] = ImageSerializer(instance.images.all(), many=True, context=self.context).data
        return rep

    def create(self, validated_data):
        image = self.context.get('image').request.FILES
        product = Product.objects.create(**validated_data)
        for image in image.values():
            ProductImage.objects.create(product=product, image=image)
        return product




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
