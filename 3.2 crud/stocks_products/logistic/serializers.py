from rest_framework import serializers
from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = StockProduct
        fields = '__all__'


class StockProductSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(max_digits=10, decimal_places=2, coerce_to_string=False)

    class Meta:
        model = StockProduct
        fields = ['id', 'product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = StockProductSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']

    def create(self, validated_data):
        positions_data = validated_data.pop('positions')
        stock = Stock.objects.create(**validated_data)

        for position_data in positions_data:
            StockProduct.objects.create(stock=stock, product=position_data['product'],
                                        defaults={'price': position_data['price'],
                                                  'quantity': position_data['quantity']})

        return stock

    def update(self, instance, validated_data):
        positions_data = validated_data.pop('positions')
        instance.address = validated_data.get('address', instance.address)
        instance.save()

        existing_positions = {position.id: position for position in instance.positions.all()}

        for position_data in positions_data:
            position_id = position_data.get('id')
            if position_id in existing_positions:
                position = existing_positions.pop(position_id)
                position.product = position_data.get('product', position.product)
                position.quantity = position_data.get('quantity', position.quantity)
                position.price = position_data.get('price', position.price)
                position.save()
            else:
                StockProduct.objects.create(stock=instance, **position_data)

        for position in existing_positions.values():
            position.delete()

        return instance