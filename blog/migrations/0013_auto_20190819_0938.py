# Generated by Django 2.2.4 on 2019-08-19 09:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0012_auto_20190807_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content_min',
            field=models.TextField(blank=True,
                                   help_text='Как статья отображается в свернутом виде. Максимум 200 символов.',
                                   max_length=500, verbose_name='Миниверсия статьи'),
        ),
    ]
