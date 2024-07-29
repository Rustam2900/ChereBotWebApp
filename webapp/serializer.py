from rest_framework import serializers

from webapp.models import Product, CartItem, Shares, MinAmount, Banner


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'image',
            'price',
            'description',
            'calcium',
            'bicarbonates',
            'magnesium',
            'chlorides'
        ]


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


class SharesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shares
        fields = '__all__'


class MinAmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinAmount
        fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'
