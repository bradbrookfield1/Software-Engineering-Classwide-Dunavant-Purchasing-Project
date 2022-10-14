from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Log(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=100)
    asset = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('inventory:log-confirm-delete', kwargs={'pk': self.pk})


class Asset(models.Model):

    # Asset ID and Location Details
    asset_Tag = models.CharField(max_length=100, blank=True, default='No Tag')
    purchase_Order_Number = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    iP_Address = models.CharField(max_length=100, blank=True)
    spare_Inventory_Location = models.CharField(max_length=100, blank=True)
    RMA = models.CharField(max_length=100, blank=True, default='No')

    # Asset Specification Details
    equipment_Name = models.CharField(max_length=100, blank=True)
    equipment_Manufacturer = models.CharField(max_length=100, blank=True)
    vendor = models.CharField(max_length=100, blank=True)
    equipment_Type = models.CharField(max_length=100, blank=True)
    tracking_Number = models.CharField(max_length=100, blank=True)
    equipment_Model = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(
        max_digits=13, decimal_places=2, blank=True, null=True)
    serial_Number = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    verizon_Cost_Center = models.CharField(max_length=100, blank=True)
    attachments = models.FileField(blank=True)
    additional_Specs = models.TextField(blank=True)

    # Asset Date Details
    approval_Date = models.DateField(blank=True, null=True)
    last_Audit_Date = models.DateField(default=timezone.now)
    purchase_Date = models.DateField(blank=True, null=True)

    # Asset Incident Details
    incident_Status = models.CharField(max_length=100, blank=True)
    equipment_Issues = models.TextField(blank=True)
    special_Notes = models.TextField(blank=True)
    last_Modified = models.DateField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('inventory:asset-detail', kwargs={'pk': self.pk})
