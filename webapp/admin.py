from django.contrib import admin
from webapp.models import Product, CartItem
from modeltranslation.admin import TranslationAdmin


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ('id', 'name', 'image', 'price', 'description')
    search_fields = ('id', 'name')
    list_filter = ('id', 'name', 'price', 'description')


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity', 'total_price')
    search_fields = ('id', 'product', 'quantity')
    list_filter = ('id', 'product', 'quantity', 'total_price')
