# Generated by Django 5.0.3 on 2024-03-21 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_delete_reservationemail'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EmailTemplate',
        ),
        migrations.AddField(
            model_name='email',
            name='template',
            field=models.CharField(choices=[('APPROVED', 'Approved'), ('WAITING_APPROVAL', 'Waiting_approval')], default='APPROVED', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='email',
            table='email',
        ),
    ]
