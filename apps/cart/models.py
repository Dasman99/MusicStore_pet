from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from ..product.models import ProductImage


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductImage, on_delete=models.CASCADE, null=True)
