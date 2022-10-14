from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime


class Request(models.Model):
    author = models.ForeignKey(
        User, default=None, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    user_id = models.IntegerField(blank=False)
    date_created = models.DateTimeField(default=datetime.datetime.now)
    equipment_name = models.CharField(max_length=30, blank=False)
    equipment_number = models.IntegerField(blank=False)

    def __str__(self):
        list = [self.equipment_name, self.equipment_number, self.author]
        list_as_string = ', '.join(str(x) for x in list)
        return list_as_string


class EquipmentRequest(models.Model):
    STATUS = (
        # new/ After Request but before Request for Quote
        ('unreviewed', 'Unreviewed'),
        # After Request for quote but before Purchase Order
        ('quote pending', 'Quote Pending'),
        # After Purchase Order but before Asset Recieved
        ('purchase pending', 'Purchase Pending'),
        ('complete', 'Complete'),  # Asset Recieved
    )
    user_request = models.ForeignKey(
        'Request', on_delete=models.CASCADE, null=True)
    status = models.CharField(
        max_length=30, choices=STATUS, default='unreviewed')
    # Foreign Keys to models from other teams' apps
    # After Review of other teams work:
    # request_for_quote=models.ForeignKey(RequestForQuote,on_delete=models.SET_NULL,null=True)
    # quote=models.ForeignKey(Quote,on_delete=models.SET_NULL,null=True)
    # request_approval=models.ForeignKey(RequestApproval,on_delete=models.SET_NULL,null=True)
    #asset=models.ForeignKey(Asset, on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return str(self.user_request)


def create_EquipmentRequest(sender, **kwargs):
    if kwargs['created']:
        er = EquipmentRequest.objects.create(user_request=kwargs['instance'])


post_save.connect(create_EquipmentRequest, sender=Request)
