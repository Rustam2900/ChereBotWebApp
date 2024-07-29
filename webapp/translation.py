from modeltranslation.translator import register, TranslationOptions
from . import models


@register(models.Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


@register(models.Shares)
class SharesTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
