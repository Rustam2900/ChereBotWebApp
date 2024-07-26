from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BotUser(BaseModel):
    telegram_id = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=30)
    add_contact = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'BotUser'
        verbose_name_plural = 'BotUsers'


class BotCompany(BaseModel):
    telegram_id = models.BigIntegerField(unique=True)
    company_name = models.CharField(max_length=30)
    company_employee_name = models.CharField(max_length=30)
    company_contact = models.CharField(max_length=30)
    employee_number = models.IntegerField()
    lifetime = models.IntegerField()

    class Meta:
        verbose_name = 'BotCompany'
        verbose_name_plural = 'BotCompanies'


class BotCompanyOrder(BaseModel):
    bot_company_id = models.ForeignKey(BotCompany, on_delete=models.CASCADE, related_name='order_company')
    product_name = models.CharField(max_length=30)
    quantity = models.IntegerField()

    class Meta:
        verbose_name = 'BotCompanyOrder'
        verbose_name_plural = 'BotCompanyOrders'


class BotUserOrder(BotCompany):
    bot_user_id = models.ForeignKey(BotUser, on_delete=models.CASCADE, related_name='order_user')
    product_name = models.CharField(max_length=30)
    quantity = models.IntegerField()

    class Meta:
        verbose_name = 'BotUserOrder'
        verbose_name_plural = 'BotUserOrders'


class rustam(BaseModel):
    pass