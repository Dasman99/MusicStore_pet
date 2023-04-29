from django.urls import path, include
from rest_framework import routers
from .views import *
from ..cart.views import CartList

router = routers.DefaultRouter()
# router.register(r'products', ProductList)
router.register(r'categories', CategoryList)
router.register(r'review', ReviewList)
router.register(r'brands', BrandList)
router.register(r'order', OrderView)
router.register(r'cart', CartList)
# router.register(r'categories/<int:pk>', CategoryDetail)


urlpatterns = [
    path('', include(router.urls)),
    path('products/post/', ProductCreate.as_view()),
    # path('products/<int:pk>', ProductDetailView.as_view()),
    path('products/', ProductList.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view()),
    # path('cart/', CartList.as_view(), name='cart-list'),
    # path('category/<int:pk>/', CartDetail.as_view(), name='category_detail'),
    # path('cart-item/create/', CartItemCreate.as_view(), name='cart-item-create'),
    # path('cart-item/<int:pk>/', CartItemDetail.as_view(), name='cart-item-detail'),
]