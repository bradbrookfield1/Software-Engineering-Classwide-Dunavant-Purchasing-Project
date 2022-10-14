from django.contrib import admin
from .models import CreateUserAccount, RequestForQuote, Quote, RequestApproval

admin.site.register(RequestForQuote)
admin.site.register(Quote)
admin.site.register(RequestApproval)
admin.site.register(CreateUserAccount)