from django import forms
from django.forms import TextInput
from . import models

class RequestForm(forms.ModelForm):
    class Meta:
        model = models.Request
        fields = [
            'first_name',
            'last_name',
            'user_id',
            'equipment_name',
            'equipment_number'
            ]
        widgets = {
            'first_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'First Name',
                'label': 'First Name'
            }),
            'last_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Last Name'
            }),
            'user_id': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'User ID'
            }),
            'equipment_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Equipment Name'
            }),
            'equipment_number': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Equipment Number'
            })
        }