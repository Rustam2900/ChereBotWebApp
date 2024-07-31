from modeltranslation.translator import TranslationOptions, register
from . import models


@register(models.BotUser)
class BotUserTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(models.BotCompany)
class BotCompanyTranslationOptions(TranslationOptions):
    fields = ('company_name', 'company_employee_name')


@register(models.BotCompanyOrder)
class BotCompanyOrderTranslationOptions(TranslationOptions):
    fields = ('product_name',)
