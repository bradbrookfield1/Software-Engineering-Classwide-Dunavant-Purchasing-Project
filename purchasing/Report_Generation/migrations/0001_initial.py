# Generated by Django 2.2.12 on 2021-10-25 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Database_Fields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_tag', models.CharField(blank=True, max_length=100)),
                ('last_audit_date', models.DateField()),
                ('company', models.CharField(blank=True, max_length=100)),
                ('department', models.CharField(blank=True, max_length=100)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('equipment_type', models.CharField(blank=True, max_length=100)),
                ('vendor', models.CharField(blank=True, max_length=100)),
                ('purchase_price', models.CharField(blank=True, max_length=100)),
                ('purchase_date', models.DateField()),
                ('equipment_model', models.CharField(blank=True, max_length=100)),
                ('assigned_to', models.CharField(blank=True, max_length=100)),
                ('equipment_status', models.CharField(blank=True, max_length=100)),
                ('serial_number', models.CharField(blank=True, max_length=100)),
                ('phone_number', models.CharField(max_length=12)),
                ('spare_location', models.CharField(blank=True, max_length=100)),
                ('verizon_cost_center', models.CharField(blank=True, max_length=100)),
                ('equipment_issue', models.TextField(blank=True)),
                ('date_modified', models.DateField()),
                ('modified_by', models.CharField(blank=True, max_length=100)),
                ('purchase_order_number', models.CharField(blank=True, max_length=100)),
                ('date_approved', models.CharField(blank=True, max_length=100)),
                ('approving_supervisor', models.CharField(blank=True, max_length=100)),
                ('carrier_tracking_number', models.CharField(blank=True, max_length=100)),
                ('equipment_name', models.CharField(blank=True, max_length=100)),
                ('ip_address', models.GenericIPAddressField()),
                ('konica_service_code', models.CharField(blank=True, max_length=100)),
                ('notes', models.TextField(blank=True)),
                ('item_type', models.CharField(blank=True, max_length=100)),
                ('path', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
