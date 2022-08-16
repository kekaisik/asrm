# Generated by Django 4.0.6 on 2022-08-16 12:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('acpm', '0011_rename_education_conference_alter_conference_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('upcoming', 'Предстоящие мероприятия'), ('archive', 'Архив')], max_length=15, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='user',
            name='expiration_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 8, 16, 12, 33, 43, 940865, tzinfo=utc), verbose_name='Подписка действительна до'),
        ),
    ]