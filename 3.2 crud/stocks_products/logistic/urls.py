from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)

urlpatterns = router.urls + [
    path('api/v1/stocks/<int:pk>/', StockDeleteView.as_view(), name='stock-delete'),
    path('api/v1/products/', ProductListView.as_view(), name='product-list'),
]
