from django.db import models
from user_requests.models import EquipmentRequest
import datetime
# Create your models here.


class QuoteRequest(models.Model):
    name = models.CharField(max_length=50)
    details = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=datetime.datetime.now)
    # Maybe add vendor email for easier emailing, Should vendor be its own model for easier access
    vendor = models.CharField(max_length=50, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    # Might not need, depends if ER has the Key to QR or vice versa
    equipment_request = models.ForeignKey(
        EquipmentRequest, on_delete=models.CASCADE, null=True)
    # A product number option if I know which product I want to request exactaly

    # Want a function that will allow easier ways to email the quote to a vendor
    # Want a function that can duplicate this and allows the changing of desired values to create a new one
    def __str__(self):
        return self.name


class Quote(models.Model):

    STATUS = (
        ('unreviewed', 'unreviewed'),
        ('approved', 'approved'),
        ('rejected', 'rejected'),
    )
    # Should quote name and product name be different fields
    name = models.CharField(max_length=50)
    details = models.CharField(max_length=200)
    # May be better to create a model for po_num so it can be a foreign key for more models
    po_number = models.CharField(max_length=10, default=" ")
    product_id = models.CharField(max_length=50)
    price = models.FloatField(blank=True)
    vendor = models.CharField(max_length=50)
    quote_request = models.ForeignKey(
        QuoteRequest, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(default=datetime.datetime.now)
    status = models.CharField(
        max_length=20, choices=STATUS, default='unreviewed')
    last_updated = models.DateTimeField(auto_now=True)

    # Want a function that can look through an email and create a new Quote with options to change fields if they are incorret
    def generate_po_number(self):
        # Need a better way to generate PO numbers that ensures no repeats occur and they are all in a defined form
        po_number = str(self.id)
        return po_number

    def __str__(self):
        return self.name
