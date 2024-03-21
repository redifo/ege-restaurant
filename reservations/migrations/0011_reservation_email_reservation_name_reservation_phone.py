# Generated by Django 5.0.3 on 2024-03-21 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0010_rename_request_text_specialrequest_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='email',
            field=models.EmailField(default='kaanredif@gmail.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='name',
            field=models.CharField(default='kaan', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='phone',
            field=models.CharField(default='1564132151', max_length=12),
            preserve_default=False,
        ),
    ]
