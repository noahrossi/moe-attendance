# Generated by Django 2.0.6 on 2018-06-03 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birthday',
            field=models.DateField(verbose_name='student birthday'),
        ),
    ]
