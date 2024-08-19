import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from bot.models import BaseModel, BotCompany, BotUser


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
        ordering = ['-created_at']
        verbose_name = _('Product')
        verbose_name_plural = _('Product')

    def __str__(self):
        return self.name


class CartItem(BaseModel):
    order_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    bot_company_id = models.ForeignKey(BotCompany, on_delete=models.CASCADE, related_name='company_order', null=True,
                                       blank=True)
    bot_user_id = models.ForeignKey(BotUser, on_delete=models.CASCADE, related_name='company_order', null=True,
                                    blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    quantity = models.PositiveIntegerField(default=1)


    def total_price(self):
        return self.quantity * self.product.price

    def clean(self):
        if not self.bot_company_id and not self.bot_user_id:
            raise ValidationError('Either bot_company_id or bot_user_id must be set.')
        if self.bot_company_id and self.bot_user_id:
            raise ValidationError('Only one of bot_company_id or bot_user_id must be set.')

    class Meta:
        ordering = ['-created_at']




class Shares(BaseModel):
    title = models.CharField(_('title'), max_length=100)
    description = models.TextField(_('description'))
    image = models.ImageField()
    interest = models.CharField(max_length=20, null=True, blank=True)
    price = models.FloatField()

    class Meta:
        ordering = ['-created_at']
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

