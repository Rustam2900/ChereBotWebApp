# Generated by Django 5.0.7 on 2024-08-19 06:03

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_cartitem_order_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='id',
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='order_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
