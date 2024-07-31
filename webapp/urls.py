from django.urls import path
from webapp.views import ProductListView, BannerListView, MinAmountListView, CartItemListCreateView, \
    SharesListCreateView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('cart-items/', CartItemListCreateView.as_view(), name='cart-item-list-create'),
    path('shares/', SharesListCreateView.as_view(), name='shares-list-create'),
    path('banner/', BannerListView.as_view(), name='banner'),
    path('min-amount/', MinAmountListView.as_view(), name='minamount')
]
