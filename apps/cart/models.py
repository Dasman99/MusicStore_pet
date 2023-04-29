from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from ..product.models import Product


# class CartManager(models.Manager):
#     def active(self):
#         return self.filter(is_active=True)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
