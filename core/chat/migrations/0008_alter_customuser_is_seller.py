# Generated by Django 5.0.6 on 2025-03-01 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_customuser_is_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_seller',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=45),
        ),
    ]
