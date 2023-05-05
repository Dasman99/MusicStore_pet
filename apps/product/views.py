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


class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductImageSerializer

    # def create(self, request, *args, **kwargs):
    #     image_files = request.FILES.getlist('image')
    #     product_data = request.data
    #     print(image_files)
    #     product_serializer = self.get_serializer(data=product_data)
    #     product_serializer.is_valid(raise_exception=True)
    #     product = product_serializer.save()
    #     print(product)
    #     for image_file in image_files:
    #         ProductImage.objects.create(product=product, image=image_file)
    #
    #     response_serializer = ProductSerializer(product)
    #     return Response(response_serializer.data, status=status.HTTP_201_CREATED)


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
