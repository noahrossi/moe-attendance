# Generated by Django 2.0.6 on 2018-06-03 22:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_auto_20180603_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='time',
            field=models.TimeField(default=datetime.time(22, 10, 33, 723866), verbose_name='meeting time'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='meeting',
            name='date',
            field=models.DateField(primary_key=True, serialize=False, verbose_name='meeting date'),
        ),
    ]
