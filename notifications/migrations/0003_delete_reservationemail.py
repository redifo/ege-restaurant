# Generated by Django 5.0.3 on 2024-03-20 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_alter_reservationemail_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ReservationEmail',
        ),
    ]
