# Generated by Django 5.2.4 on 2025-07-12 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pg_finder', '0010_alter_pg_full_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pg',
            name='gate_closing_time',
            field=models.TimeField(null=True),
        ),
    ]
