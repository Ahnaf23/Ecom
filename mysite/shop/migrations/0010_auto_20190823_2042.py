# Generated by Django 2.2.3 on 2019-08-23 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_orders_phone'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
    ]
