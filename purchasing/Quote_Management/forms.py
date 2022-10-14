from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Button, ButtonHolder, MultiField, Div, HTML, Submit, Field, Fieldset
from crispy_forms.bootstrap import FormActions
from crispy_bootstrap5.bootstrap5 import FloatingField
from django.urls import reverse
from django.utils import timezone

from .models import Quote, RequestForQuote, CreateUserAccount

class RequestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-requestForm'
        self.helper.form_class = 'requestForms'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                Div(FloatingField('request_name'), css_class="col"),
                Div(FloatingField('request_date'), css_class="col"),
                css_id="asteriskField",
                css_class="row my-2"
            ),
            Div(
                FloatingField('equipment_name', css_class="my-2"),
                css_id="asteriskField"
            ),
            Div(
                FormActions(
                    Submit('submit', 'Submit', css_class='btn btn-primary my-4'),
                    Submit('cancel', 'Cancel', css_class='btn btn-danger my-4', formnovalidate='formnovalidate'),
                ),
                align="center"
            ),
        )
    class Meta:
        model = RequestForQuote
        fields = [
            'request_name',
            'request_date', # maybe not needed if date requested is auto-assigned
            'equipment_name',
        ]
    
    request_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), initial=timezone.now())
    
class PdfInput(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-quoteUpdate'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset("",
                'quote_name',
                'equipment_name',
                'quote_cost',
                'quote_quantity',
                'request',
            ),
            FormActions(
                Submit('submit', 'Submit', css_class='btn btn-primary my-4'),
                HTML("""<a href="{% url "quoting:home" %}" class="btn btn-danger">Cancel</a>"""),
            )
        )
    class Meta:
        model = Quote
        fields = [ 
            'quote_name',
            'equipment_name',
            'quote_cost',
            'quote_quantity',
            'request',
        ]

class CreateUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-createUser'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset("",
                'user_name',
                'user_email',
                'user_password',
            ),
            FormActions(
                Submit('submit', 'Submit', css_class='btn btn-primary my-4'),
                HTML("""<a href="{% url "quoting:home" %}" class="btn btn-danger">Cancel</a>"""),
            )
        )
    class Meta:
        model = CreateUserAccount
        fields = [ 
            'user_name',
            'user_email',
            'user_password',
        ]
