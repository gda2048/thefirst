# Generated by Django 2.1.7 on 2019-06-27 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20190627_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='photo',
            field=models.ImageField(height_field='height', null=True, upload_to='', verbose_name='Изображение', width_field='width'),
        ),
        migrations.AlterField(
            model_name='articlephotoreport',
            name='photo',
            field=models.ImageField(height_field='height', null=True, upload_to='', verbose_name='Изображение', width_field='width'),
        ),
    ]