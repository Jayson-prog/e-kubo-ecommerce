# Generated by Django 5.0.6 on 2025-03-17 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_rename_category_product_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default='default_category/', upload_to='product_category/'),
        ),
    ]
