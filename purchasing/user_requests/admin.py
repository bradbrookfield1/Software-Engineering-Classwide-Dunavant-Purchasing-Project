from django.contrib import admin
from .models import Request
from .models import EquipmentRequest
# Register your models here.
admin.site.register(Request)
admin.site.register(EquipmentRequest)