from django.contrib import admin
from .models import *
from ..product.models import *


# class ProductInline(admin.TabularInline):
#     model = ProductImage

@admin.register(Cart)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["user"]


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    # inlines = [ProductInline]
    list_display = ['cart', 'product']