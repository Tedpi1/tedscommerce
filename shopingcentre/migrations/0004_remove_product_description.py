# Generated by Django 5.0.6 on 2024-09-26 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopingcentre', '0003_alter_category_options_remove_category_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
    ]
