# Generated by Django 2.2.3 on 2019-07-21 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0003_auto_20190721_0048'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='helpitem',
            options={'ordering': ['-id'], 'verbose_name': 'Пункт помощи', 'verbose_name_plural': 'Пункты помощи'},
        ),
    ]