# Generated by Django 3.2.8 on 2021-10-20 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_requests', '0002_auto_20211020_1057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='ER',
        ),
    ]
