# Generated by Django 4.2.20 on 2025-04-01 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_restaurant_rating_restaurant'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='ratings',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
