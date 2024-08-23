from rest_framework import serializers

from bot.models import BotUser, BotCompany, BotCompanyOrder


class BotUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotUser
        fields = [
            'telegram_id',  # Ushbu qatorni qo'shish kerak
            'name',
            'contact',
            'add_contact'
        ]


class BotCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = BotCompany
        fields = [
            'telegram_id',  # Ushbu qatorni qo'shish kerak
            'company_name',
            'company_employee_name',
            'company_contact',
            'employee_number',
            'lifetime'
        ]


class BotCompanyOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotCompanyOrder
        fields = ['bot_company_id', 'product_name', 'quantity']
