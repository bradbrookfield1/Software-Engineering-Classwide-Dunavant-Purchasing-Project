from django import forms
from .models import QuoteRequest, Quote

class CreateQuoteRequest(forms.ModelForm):
    class Meta:
        model = QuoteRequest
        fields = ['name', 'details', 'vendor']
        widgets = {
            'details': forms.Textarea(attrs={"rows":"5", "cols":"40"}),
        }
    
class CreateQuote(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['name', 'details', 'product_id', 'vendor', 'price', 'quote_request']
        widgets = {
            'details': forms.Textarea(attrs={"rows":"5", "cols":"40"}),
        }

class ChangeStatus(forms.Form):
    status = forms.ChoiceField(choices=Quote.STATUS, required=False)  

class SearchAndSort(forms.Form):
    sort_options = (
        ('name', 'Name'),
        ('status', 'Status'),
        ('date_created', 'Date Created'), 
        ('last_updated', 'Date Updated'),
    )
    order_options = (
        ('ascending', 'Ascending'),
        ('descending', 'Descending'),
    )
    object_type = (
        ('quotes', 'Quotes'),
        ('quote_requests', 'Quote Requests')
    )
    search_result = forms.CharField(max_length=100, required=False, label = 'Search')
    sort = forms.ChoiceField(choices=sort_options, required=False, label='Sort By')
    order = forms.ChoiceField(choices=order_options, required=False, label='Order')
    type = forms.ChoiceField(choices=object_type, required=False, label='Type')
    