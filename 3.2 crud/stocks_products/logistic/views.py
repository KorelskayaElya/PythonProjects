from logistic.models import Product, Stock, StockProduct
from logistic.serializers import ProductSerializer, StockSerializer, ProductPositionSerializer
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from logistic.pagination import CustomPagination
from rest_framework.filters import BaseFilterBackend
from django.db.models import Q
from rest_framework.filters import SearchFilter


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']


class StockFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        products = request.query_params.getlist('product')
        if products:
            q_objects = Q()
            for product in products:
                q_objects |= Q(positions__product_id=product)
            queryset = queryset.filter(q_objects).distinct()
        return queryset


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [StockFilterBackend, DjangoFilterBackend]
    filterset_fields = ['products']
    pagination_class = CustomPagination




