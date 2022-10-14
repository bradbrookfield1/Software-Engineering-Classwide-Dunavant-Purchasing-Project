# Generated by Django 3.2.8 on 2021-10-23 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_requests', '0005_request_er'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipmentrequest',
            name='user_request',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_requests.request'),
        ),
        migrations.AlterField(
            model_name='equipmentrequest',
            name='status',
            field=models.CharField(choices=[('unreviewed', 'Unreviewed'), ('quote pending', 'Quote Pending'), ('purchase pending', 'Purchase Pending'), ('complete', 'Complete')], default='unreviewed', max_length=30),
        ),
        migrations.AlterField(
            model_name='request',
            name='ER',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_requests.equipmentrequest'),
        ),
    ]