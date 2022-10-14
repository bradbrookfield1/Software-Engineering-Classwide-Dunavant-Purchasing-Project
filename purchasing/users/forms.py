from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import SiteUser


class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = SiteUser
        fields = ["username", "email", "password1", "password2"]


class AdminRegisterForm(UserCreationForm):
    email = forms.EmailField()
    admin_Key = forms.CharField(max_length=100)

    class Meta:
        model = SiteUser
        fields = ["username", "email", "password1", "password2", "admin_Key"]
