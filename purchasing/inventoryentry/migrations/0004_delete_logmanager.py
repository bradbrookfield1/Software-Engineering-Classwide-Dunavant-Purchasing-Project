# Generated by Django 3.2.9 on 2021-11-15 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryentry', '0003_logmanager'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LogManager',
        ),
    ]