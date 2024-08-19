from django.contrib import admin
from webapp.models import Product, CartItem, Shares, MinAmount, Banner
from modeltranslation.admin import TranslationAdmin

admin.site.register(MinAmount)


# admin.site.register(Banner)


@admin.register(Banner)
class BannerAdmin(TranslationAdmin):
    list_display = ('id',)
    search_fields = ('id',)


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ('id', 'name', 'image', 'price', 'description')
    search_fields = ('id', 'name')
    list_filter = ('id', 'name')


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'product', 'quantity')
    search_fields = ('order_id', 'product__name')  # Agar product name bilan qidirishni istasangiz
    list_filter = ('product',)  # Filtr faqat mavjud maydonlar uchun ishlatiladi


@admin.register(Shares)
class SharesAdmin(admin.ModelAdmin):
    list_display = ('id', 'price')
    search_fields = ('id',)
    list_filter = ('id',)
