from django.db import models
from django.contrib.auth.models import User

admin_Key = 'lookachu'


class SiteUser(User):
    admin_Key = models.CharField(max_length=100, default='')
