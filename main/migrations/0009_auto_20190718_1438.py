# Generated by Django 2.2.3 on 2019-07-18 14:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0008_remove_person_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=20, unique=True, verbose_name='Логин'),
        ),
    ]
