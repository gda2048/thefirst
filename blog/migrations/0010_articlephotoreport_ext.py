# Generated by Django 2.2.3 on 2019-07-26 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_articlephotoreport_binary_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlephotoreport',
            name='ext',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]