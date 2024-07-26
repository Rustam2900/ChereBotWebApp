from modeltranslation.translator import register, TranslationOptions
from . import models


@register(models.Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)
