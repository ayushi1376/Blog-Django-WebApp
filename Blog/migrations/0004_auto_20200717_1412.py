# Generated by Django 3.0.8 on 2020-07-17 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200717_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(default='', max_length=130),
        ),
    ]
