# Generated by Django 5.0.6 on 2025-03-18 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0031_alter_product_product_image1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='default_product.jpg', upload_to='product_images/'),
        ),
    ]
