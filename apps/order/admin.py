from django.contrib import admin

from .models import Order


# class OrderItemInline(admin.StackedInline):
#     model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["address", "user", "status", "id"]
    list_filter = ["status", "created"]
    list_editable = ["status"]
