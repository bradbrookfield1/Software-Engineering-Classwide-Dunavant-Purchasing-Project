# Generated by Django 3.2.8 on 2021-10-16 16:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_alter_siteuser_admin_key'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SiteUser',
            new_name='User',
        ),
    ]
