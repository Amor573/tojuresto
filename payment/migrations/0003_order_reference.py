# Generated by Django 5.1.2 on 2024-12-08 19:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_shippingaddress_shipping_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='reference',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]