# Generated by Django 5.0.3 on 2024-03-20 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0008_remove_table_location_table_table_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='table_location',
            field=models.CharField(choices=[('Garden', 'Garden'), ('Bar', 'Bar')], max_length=50),
        ),
    ]