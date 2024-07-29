from modeltranslation.translator import register, TranslationOptions
from . import models


@register(models.BotCompanyOrder)
class BotCompanyOrderTranslationOptions(TranslationOptions):
    fields = ('product_name',)
