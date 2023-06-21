from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import *
from ..cart.views import CartList

router = routers.DefaultRouter()
router.register(r'products', ProductAPIView)
router.register(r'categories', CategoryList)
router.register(r'review', ReviewList)
router.register(r'brands', BrandList)
router.register(r'order', OrderView)
router.register(r'cart', CartList)


urlpatterns = [

    # path('product/post/', ProductImageAPIView.as_view()),
    path('product/', ProductImageAPIView.as_view(), name='product-delete'),
    path('drf-auth/', include('rest_framework.urls')),
    path('product/retrive /<int:pk>', ProductRetrieveUpdateDestroyView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('', include(router.urls)),
]