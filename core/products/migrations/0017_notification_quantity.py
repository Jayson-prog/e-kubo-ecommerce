# Generated by Django 5.0.6 on 2025-02-01 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_order_order_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
