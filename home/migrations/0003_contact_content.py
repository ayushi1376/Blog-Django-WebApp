# Generated by Django 3.0.8 on 2020-07-16 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='content',
            field=models.TextField(default=None),
        ),
    ]
