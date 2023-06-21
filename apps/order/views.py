from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action

from MusicStore.apps.cart.models import Cart
from MusicStore.apps.order.models import OrderItem, Order
from MusicStore.apps.product.serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=False, methods=['post'])
    def create_from_cart(self, request):
        # Получаем текущего пользователя
        user = request.user

        # Получаем текущую корзину пользователя
        cart = Cart.objects.get(user=user, active=True)

        # Создаем новый заказ для этого пользователя
        order = Order.objects.create(user=user)

        # Переносим товары из корзины в заказ
        for item in cart.items.all():
            order_item = OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.price
            )

        # Отмечаем корзину как неактивную
        cart.active = False
        cart.save()

