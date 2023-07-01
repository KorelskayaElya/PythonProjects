from logistic.models import Product, Stock, StockProduct
from logistic.serializers import ProductSerializer, StockSerializer, ProductPositionSerializer
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView, ListAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from logistic.pagination import CustomPagination
from rest_framework.filters import BaseFilterBackend
from django.db.models import Q
from rest_framework.filters import SearchFilter


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['title', 'description']


class StockFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        products = request.query_params.getlist('product')
        if products:
            q_objects = Q()
            for product in products:
                q_objects |= Q(positions__product_id=product)
            queryset = queryset.filter(q_objects).distinct()
        return queryset


class StockAPIView(APIView):
    def post(self, request):
        serializer = StockSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StockDeleteView(DestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [StockFilterBackend, DjangoFilterBackend]
    filter_fields = ['positions__product']
    pagination_class = CustomPagination


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']





