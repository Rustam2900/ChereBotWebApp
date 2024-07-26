from django.db import models
from bot.models import BaseModel
from django.utils.translation import gettext_lazy as _


class Product(BaseModel):
    name = models.CharField(_("name"), max_length=30)
    description = models.TextField(_("description"))
    image = models.ImageField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    calcium = models.IntegerField()
    bicarbonates = models.IntegerField()
    magnesium = models.IntegerField()
    chlorides = models.IntegerField()

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Product')

    def __str__(self):
        return self.name


class CartItem(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.quantity * self.product.price
