# Generated by Django 2.2.3 on 2019-07-24 10:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0006_auto_20190723_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlephotoreport',
            name='main',
            field=models.BooleanField(default=False, help_text='Если отмечено несколько картинок, то выбирается любая',
                                      verbose_name='Отображать в preview'),
        ),
    ]
