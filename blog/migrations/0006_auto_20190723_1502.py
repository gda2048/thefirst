# Generated by Django 2.2.3 on 2019-07-23 15:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0005_auto_20190720_1246'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-release_date'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
    ]
