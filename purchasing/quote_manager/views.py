from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Quote, QuoteRequest
from .forms import CreateQuote, CreateQuoteRequest, ChangeStatus, SearchAndSort

def home(request):
    return render(request, 'quote_manager/home.html', {})

def quote(request, id):
    cur_quote = Quote.objects.get(id=id)
    if request.method == "POST":
        form = ChangeStatus(request.POST)
        if form.is_valid():  
            cur_status = form.cleaned_data['status']
            if cur_status == "approved" and cur_quote.po_number == " ":
                cur_quote.po_number = Quote.generate_po_number(cur_quote)
            cur_quote.status = cur_status
            cur_quote.save()
            return HttpResponseRedirect("/quotes/%i" %cur_quote.id)
    else:
        form = ChangeStatus(initial={'status':cur_quote.status})

    in_dict = { "quote":cur_quote, "form":form }
    return render(request, 'quote_manager/quote.html', in_dict)

def list(request):
    if request.method == "POST":
        form = SearchAndSort(request.POST)
        if form.is_valid():
            if form.cleaned_data['type'] == 'quote_requests':
                list = QuoteRequest.objects.all()
            else:
                list = Quote.objects.all()
            attribute = form.cleaned_data['sort']
            if form.cleaned_data['order'] == 'descending':
                attribute = '-'+attribute
            list = list.filter(name__contains=form.cleaned_data['search_result'])
            list = list.order_by(attribute)
            
    else:
        form = SearchAndSort()
        list = Quote.objects.order_by('name')
    dict = { 'list':list, 'form': form }
    return render(request, 'quote_manager/list.html', dict)

def create(request):
    if request.method == "POST":
        form1 = CreateQuote(request.POST)
        form2 = CreateQuoteRequest(request.POST)
        if form1.is_valid():
            new_quote = form1.save()
            return HttpResponseRedirect("/quotes/%i" %new_quote.id)
        if form2.is_valid(): 
            new_quote_request = form2.save()
            return HttpResponseRedirect("/quotes/list")
    else:
        form1 = CreateQuote()
        form2 = CreateQuoteRequest()
    return render(request, 'quote_manager/create.html', {'form1': form1, 'form2': form2})