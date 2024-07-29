from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from bot.models import BotUser, BotCompany, BotCompanyOrder


@admin.register(BotUser)
class BotUserAdmin(TranslationAdmin):
    list_display = ['id', 'name', 'contact', 'add_contact']
    search_fields = ['name', 'contact', 'contact']


@admin.register(BotCompany)
class BotCompanyAdmin(TranslationAdmin):
    list_display = ['id', 'company_name', 'company_employee_name', 'company_contact']
    search_fields = ['company_name', 'company_employee_name', 'company_contact']


@admin.register(BotCompanyOrder)
class BotCompanyOrderAdmin(TranslationAdmin):
    list_display = ['id', 'product_name', 'quantity', 'total_price', 'create_at']
    search_fields = ['id', 'product_name']
