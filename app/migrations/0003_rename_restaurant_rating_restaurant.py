# Generated by Django 4.2.20 on 2025-04-01 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_restaurant_restaurant_type_sale_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='Restaurant',
            new_name='restaurant',
        ),
    ]
