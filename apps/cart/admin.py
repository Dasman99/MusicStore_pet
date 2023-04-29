from django.contrib import admin
from .models import *


class CartInline(admin.StackedInline):
    model = CartItem


@admin.register(Cart)
class ProductAdmin(admin.ModelAdmin):
    inlines = [CartInline]
    list_display = ["user", "created"]