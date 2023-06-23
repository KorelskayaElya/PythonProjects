from logistic.models import Product, Stock, StockProduct
from logistic.serializers import ProductSerializer, StockSerializer, ProductPositionSerializer
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    def create(self, request, *args, **kwargs):
        positions_data = request.data.get('positions', [])
        stock_data = request.data.copy()
        stock_data.pop('positions', None)

        stock_serializer = self.get_serializer(data=stock_data)
        stock_serializer.is_valid(raise_exception=True)
        stock = stock_serializer.save()

        positions = []
        for position_data in positions_data:
            position_data['stock'] = stock.id
            position_serializer = ProductPositionSerializer(data=position_data)
            position_serializer.is_valid(raise_exception=True)
            position = position_serializer.save()
            positions.append(position)

        stock.positions.set(positions)

        stock_serializer = self.get_serializer(stock)
        response_data = stock_serializer.data

        return Response(response_data, status=status.HTTP_201_CREATED)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        positions_data = request.data.get('positions', [])

        for position_data in positions_data:
            product_id = position_data.get('product')
            quantity = position_data.get('quantity')
            price = position_data.get('price')

            try:
                stock_product = StockProduct.objects.get(stock=instance, product_id=product_id)
                stock_product.quantity = quantity
                stock_product.price = price
                stock_product.save()
            except StockProduct.DoesNotExist:
                continue

        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


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






