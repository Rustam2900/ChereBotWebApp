from django.contrib import admin
from webapp.models import Product, CartItem, Shares, MinAmount, Banner
from modeltranslation.admin import TranslationAdmin

admin.site.register(MinAmount)
admin.site.register(Banner)


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ('id', 'name', 'image', 'price', 'description')
    search_fields = ('id', 'name')
    list_filter = ('id', 'name')


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity')
    search_fields = ('id', 'product', 'quantity')
    list_filter = ('id', 'product', 'quantity')


@admin.register(Shares)
class SharesAdmin(admin.ModelAdmin):
    list_display = ('id', 'price')
    search_fields = ('id',)
    list_filter = ('id',)
