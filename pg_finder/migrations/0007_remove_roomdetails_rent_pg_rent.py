# Generated by Django 5.2.4 on 2025-07-06 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pg_finder', '0006_pg_pg_ac_pg_pg_food_pg_pg_parking_pg_pg_wifi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomdetails',
            name='rent',
        ),
        migrations.AddField(
            model_name='pg',
            name='rent',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
