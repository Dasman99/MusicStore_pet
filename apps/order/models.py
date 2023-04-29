from django.db import models
from django.contrib.auth.models import User
from ..cart.models import Cart


class Order(models.Model):
    STATUS_NEW = "new"
    STATUS_CONFIRMED = "confirmed"
    STATUS_REJECTED = "rejected"
    STATUS_DELIVERED = "delivered"
    STATUS_ARCHIVED = "archived"
    STATUS_CHOICES = (
        (STATUS_NEW, "Новый"),
        (STATUS_CONFIRMED, "Подтвержден"),
        (STATUS_REJECTED, "Отменен"),
        (STATUS_DELIVERED, "Доставлен"),
        (STATUS_ARCHIVED, "Архивирован"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    address = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.address
