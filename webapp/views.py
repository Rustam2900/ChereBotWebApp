from django.shortcuts import render

from rest_framework import generics
from .models import Product, Banner, MinAmount, CartItem, Shares
from webapp.serializer import ProductSerializer, BannerSerializer, MinAmountSerializer, CartItemSerializer, \
    SharesSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CartItemListCreateView(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def order_detail(request, some_id):
        order = CartItem.objects.get(id=some_id)
        context = {
            'order_id': order.order_id,
        }
        return render(request, context)


class SharesListCreateView(generics.ListAPIView):
    queryset = Shares.objects.all()
    serializer_class = SharesSerializer


class BannerListView(generics.ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


class MinAmountListView(generics.ListAPIView):
    queryset = MinAmount.objects.all()
    serializer_class = MinAmountSerializer
