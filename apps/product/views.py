from rest_framework import viewsets, status, generics
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *


class BrandList(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ProductImageAPIView(APIView):

    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)


    def post(self, request):
        product_id = request.data.get('product')
        product = Product.objects.get(id=product_id)
        images = request.FILES.getlist('image')
        for image in images:
            ProductImage.objects.create(product=product, image=image)
        serializer = ProductSerializer(product, context=self.get_renderer_context())

        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    model = Product
    serializer_class = ProductDeleteSerializer
    queryset = Product.objects.all()


class ProductAPIView(viewsets.ModelViewSet):
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
