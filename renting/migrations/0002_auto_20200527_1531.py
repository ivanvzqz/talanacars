# Generated by Django 3.0.6 on 2020-05-27 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='doors',
            field=models.IntegerField(verbose_name='Doors'),
        ),
    ]