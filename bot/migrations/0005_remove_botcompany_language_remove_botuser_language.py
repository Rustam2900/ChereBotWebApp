# Generated by Django 5.0.7 on 2024-08-19 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0004_alter_botcompany_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='botcompany',
            name='language',
        ),
        migrations.RemoveField(
            model_name='botuser',
            name='language',
        ),
    ]
