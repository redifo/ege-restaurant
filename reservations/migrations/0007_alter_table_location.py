# Generated by Django 5.0.3 on 2024-03-20 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0006_alter_table_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='location',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
