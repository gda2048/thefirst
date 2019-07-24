# Generated by Django 2.2.3 on 2019-07-19 09:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0016_auto_20190719_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author',
                                    to='main.Person', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='articlephotoreport',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos',
                                    to='main.Article', verbose_name='Статья'),
        ),
    ]
