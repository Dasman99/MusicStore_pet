from django.urls import path, include
from rest_framework import routers
from .views import *
from ..cart.views import CartList

router = routers.DefaultRouter()
router.register(r'products/post', ProductCreateAPIView)
router.register(r'categories', CategoryList)
router.register(r'review', ReviewList)
router.register(r'brands', BrandList)
router.register(r'order', OrderView)
router.register(r'cart', CartList)


urlpatterns = [
    path('', include(router.urls)),
    # path('products/post/', ProductCreateAPIView.as_view()),
    path('products/', ProductList.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view()),
]