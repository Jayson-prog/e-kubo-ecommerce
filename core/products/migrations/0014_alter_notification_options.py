# Generated by Django 5.0.6 on 2025-01-31 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_rename_user_order_buyer_remove_order_seller_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ['created_at']},
        ),
    ]
