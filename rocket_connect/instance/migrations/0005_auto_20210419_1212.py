# Generated by Django 3.1.7 on 2021-04-19 12:12

from django.db import migrations, models
import instance.models


class Migration(migrations.Migration):

    dependencies = [
        ('instance', '0004_auto_20210408_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connector',
            name='external_token',
            field=models.CharField(default=instance.models.random_string, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='server',
            name='external_token',
            field=models.CharField(default=instance.models.random_string, max_length=50, unique=True),
        ),
    ]
