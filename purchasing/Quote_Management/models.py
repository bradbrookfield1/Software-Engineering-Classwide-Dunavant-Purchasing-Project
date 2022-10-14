import datetime
from django.db import models
import random
from django.utils import timezone
from django.contrib.auth.models import User
from django.forms import ModelForm

REQUEST_STATES = (
    ('pending','Pending'),
    ('approved', 'Approved'),
    ('denied','Denied'),
)
class RequestForQuote(models.Model):
    request_name = models.CharField(max_length=32)
    request_date = models.DateField('date requested', default=timezone.now)
    request_time = models.TimeField('time requested', default=timezone.now)
    request_id = models.IntegerField(default=0)
    # request type?
    # request destination?
    # origin company?
    # origin company department?
    # name of requestee? - part of user object
    # requestee email? - part of user object
    # request quantity?
    purchase_order = models.IntegerField(default=0) # prob no purchase order number yet since this is only a request
    equipment_name = models.CharField(max_length=32)
    equipment_id = models.CharField(max_length=64)
    requestee = models.ForeignKey(User, default="", on_delete=models.CASCADE)
    status = models.CharField(max_length=8, choices=REQUEST_STATES, default='pending')
    def wasRequestedRecently(self):
        return self.request_date >= timezone.now() - datetime.timedelta(days=1) # returns a true if request is younger than one day
    def __str__(self):
        return self.request_name # returns select model info as a string

class Quote(models.Model):
    quote_id = models.IntegerField(default=0)
    creation_date = models.DateTimeField('Date created', default=timezone.now)
    modified_date = models.DateTimeField('Date modified', default=timezone.now)
    quote_name = models.CharField(default='', max_length=32)
    equipment_name = models.CharField(default='', max_length=32)
    quote_cost = models.IntegerField(default=0)
    quote_quantity = models.IntegerField(default=0)
    # quote number order?
    # quote name?
    # quote unit amount?
    # quote quantity?
    # quote total?
    request = models.ForeignKey(RequestForQuote, default="", on_delete=models.CASCADE)
    def __str__(self):
        return self.quote_name


class RequestApproval(models.Model):
    request = models.ForeignKey(RequestForQuote, default="", on_delete=models.CASCADE)
    user = models.ForeignKey(User, default="", on_delete=models.CASCADE)
    date_approved = models.DateTimeField('Date approved', default=timezone.now)
    def __str__(self):
        return self.date_approved

class QuoteToPurchaseOrder(models.Model):
    link = models.CharField(max_length=32) # PLACEHOLDER FOR POSSIBLE ATTRIBUTE (allows other team apps to pull quoting information)
    def __str__(self):
        return self.link

class CreateUserAccount(models.Model):
    user_name = models.CharField(default='', max_length=32)
    user_email = models.CharField(default='', max_length=32)
    user_password = models.CharField(default='', max_length=32)

class RequestUserInfo(models.Model):
    user_company = models.CharField(default='', max_length=64)
