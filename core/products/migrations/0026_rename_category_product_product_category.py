# Generated by Django 5.0.6 on 2025-03-17 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_category_product_product_image1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='product_category',
        ),
    ]
