from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# class BotUser(BaseModel):
#     # class Language(models.TextChoices):
#     #     UZBEK = 'UZ', 'Uzbek'
#     #     RUSSIAN = 'RU', 'Russian'
#
#     telegram_id = models.BigIntegerField(unique=True)
#     name = models.CharField(_('name'), max_length=100)
#     contact = models.CharField(max_length=30)
#     add_contact = models.CharField(max_length=30)
#     # language = models.CharField(max_length=2,
#     #                             choices=Language.choices,
#     #                             default=Language.UZBEK)
#
#     class Meta:
#         ordering = ['-created_at']
#         verbose_name = _('BotUser')
#         verbose_name_plural = _('BotUsers')
#
#     def __str__(self):
#         return self.name


class BotUser(BaseModel):
    telegram_id = models.BigIntegerField(unique=True)
    is_company = models.BooleanField(default=False)  # Indicates if this is a user
    name = models.CharField(_('name'), max_length=100)
    contact = models.CharField(max_length=30)
    add_contact = models.CharField(max_length=30)

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('BotUser')
        verbose_name_plural = _('BotUsers')

    def __str__(self):
        return self.name


# class BotCompany(BaseModel):
#     # class Language(models.TextChoices):
#     #     UZBEK = 'UZ', 'Uzbek'
#     #     RUSSIAN = 'RU', 'Russian'
#
#     telegram_id = models.BigIntegerField(unique=True)
#     company_name = models.CharField(_('company_name'), max_length=30)
#     company_employee_name = models.CharField(_('company_employee_name'), max_length=30)
#     company_contact = models.CharField(max_length=30)
#     employee_number = models.IntegerField()
#     lifetime = models.IntegerField()
#
#     # language = models.CharField(max_length=2,
#     #                             choices=Language.choices,
#     #                             default=Language.UZBEK)
#
#     class Meta:
#         ordering = ['-created_at']
#         verbose_name = _('BotCompany')
#         verbose_name_plural = _('BotCompany')


class BotCompany(BaseModel):
    telegram_id = models.BigIntegerField(unique=True)
    is_company = models.BooleanField(default=True)  # Foydalanuvchi yoki kompaniya
    company_name = models.CharField(_('company_name'), max_length=30)
    company_employee_name = models.CharField(_('company_employee_name'), max_length=30)
    company_contact = models.CharField(max_length=30)
    employee_number = models.IntegerField()
    lifetime = models.IntegerField()

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('BotCompany')
        verbose_name_plural = _('BotCompanies')

    def __str__(self):
        return self.company_name


class BotCompanyOrder(BaseModel):
    bot_company_id = models.ForeignKey(BotCompany, on_delete=models.CASCADE, related_name='order_company')
    product_name = models.CharField(_("product_name"), max_length=30)
    quantity = models.IntegerField()

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('BotCompanyOrder')
        verbose_name_plural = _('BotCompanyOrders')
