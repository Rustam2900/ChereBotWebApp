# Generated by Django 5.0.7 on 2024-08-20 12:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0006_alter_botcompany_options_botcompany_is_company_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botcompanyorder',
            name='bot_company_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='bot.botcompany'),
        ),
        migrations.AlterField(
            model_name='botcompanyorder',
            name='product_name',
            field=models.CharField(default='20 L', max_length=30, verbose_name='product_name'),
        ),
        migrations.AlterField(
            model_name='botcompanyorder',
            name='product_name_ru',
            field=models.CharField(default='20 L', max_length=30, null=True, verbose_name='product_name'),
        ),
        migrations.AlterField(
            model_name='botcompanyorder',
            name='product_name_uz',
            field=models.CharField(default='20 L', max_length=30, null=True, verbose_name='product_name'),
        ),
    ]
