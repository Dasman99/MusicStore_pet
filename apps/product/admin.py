from django.contrib import admin
from .models import *

admin.site.register(Review)


class ImageInline(admin.TabularInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ["name"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ["name"]


# class OrderItemInline(admin.StackedInline):
#     model = OrderItem
#
#
# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     inlines = [OrderItemInline]
#     list_display = ["address", "user", "status", "id"]
#     list_filter = ["status", "created"]
#     list_editable = ["status"]
