# Generated by Django 3.2.8 on 2021-10-16 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_siteuser_admin_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteuser',
            name='admin_Key',
            field=models.CharField(default='', max_length=100),
        ),
    ]
