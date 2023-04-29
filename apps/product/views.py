from django.core.exceptions import ValidationError
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView, get_object_or_404, CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *


class BrandList(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ProductCreate(CreateAPIView):
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        image = data.pop('image', None)
        brand_id = data.get('brand')
        # print(images)
        if brand_id:
            brand = get_object_or_404(Brand, id=brand_id)
            print(brand)
        else:
            raise ValidationError('Brand ID is required.')
        product_serializer = self.get_serializer(data=data)
        product_serializer.is_valid(raise_exception=True)
        product = product_serializer.save(brand=brand)
        print(product)
        if image:
            for image in image:
                a = ProductImage.objects.create(product=product, image=image)
                print(a)
        response_serializer = self.get_serializer(product)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)


class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ReviewList(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()


class OrderView(viewsets.ModelViewSet, GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CategoryList(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
