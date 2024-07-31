from django.db import models
from bot.models import BaseModel, BotCompany, BotUser
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
    bot_company_id = models.ForeignKey(BotCompany, on_delete=models.CASCADE, related_name='company_order')
    bot_user_id = models.ForeignKey(BotUser, on_delete=models.CASCADE, related_name='company_order')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.quantity * self.product.price


class Shares(BaseModel):
    title = models.CharField(_('title'), max_length=100)
    description = models.TextField(_('description'))
    image = models.ImageField()
    interest = models.CharField(max_length=20, null=True, blank=True)
    price = models.FloatField()

    class Meta:
        verbose_name = _('Shares')
        verbose_name_plural = _('Shares')

    def __str__(self):
        return self.title


class Banner(models.Model):
    image = models.ImageField()

    class Meta:
        verbose_name = _('Banner')
        verbose_name_plural = _('Banners')


class MinAmount(models.Model):
    min_price = models.IntegerField()

    class Meta:
        verbose_name = _('Minimum amount')
        verbose_name_plural = _('Minimum amounts')
