# Generated by Django 4.0.6 on 2022-08-14 18:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('acpm', '0009_event_en_announcement_event_kz_announcement_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='expiration_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 8, 14, 18, 25, 3, 891536, tzinfo=utc), verbose_name='Подписка действительна до'),
        ),
    ]
