from django.contrib import admin
from .models import Quote,QuoteRequest

# Register your models here.
admin.site.register(QuoteRequest)
admin.site.register(Quote)

