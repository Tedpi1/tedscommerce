# Generated by Django 5.0.6 on 2024-09-26 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopingcentre', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
    ]
