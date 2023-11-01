from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .models import Cart
from .serializers import CartSerializer


class CartList(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated, )
