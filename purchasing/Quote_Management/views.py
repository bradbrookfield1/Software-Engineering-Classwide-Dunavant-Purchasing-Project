from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.template import loader
from django.urls import reverse
from django.utils import timezone
import reportlab
from reportlab.pdfgen import canvas
from django.contrib import messages

from .models import CreateUserAccount, RequestForQuote, Quote
from .forms import CreateUserForm, PdfInput, RequestForm

#TODO make registration form that requires admin approval and, afterwards, user confirmation
#TODO add bootstrap css to auth system
#TODO add bootstrap to index and detail pages
#TODO decide whether user is allowed to edit their requests
@login_required
def index(request):
    return render(request, 'quoting_app/index.html') #TODO design better app page


@login_required
def requests_index(request):
    latest_request_list = RequestForQuote.objects.order_by('-request_date')[:25] #TODO make sure requestee may only view and delete their own requests while manager can view all
    context = {
        'latest_request_list': latest_request_list,
    }
    return render(request, 'requests/index.html', context) #TODO generate table of requests with sort and search function


@login_required
@user_passes_test(lambda u: u.groups.filter(name='IT Staff').exists() or u.groups.filter(name='IT Manager').exists()) #TODO add more relevant groups to access filter
def request_form(request):
    requestee = request.user
    obj_id = ''
    if request.method == "POST":
        request_form = RequestForm(request.POST, request.FILES) #TODO add an image upload option or product image lookup or generic icons
        if "cancel" in request.POST:
            return redirect("quoting:home")
        else:
            if request_form.is_valid():
                obj = request_form.save(commit=False) # Return an object without saving to the DB
                obj.requestee = requestee
                obj.save()
                obj_id = obj.id
                messages.success(request, ('Your request was successfully submitted!')) #TODO send confirmation email upon submission (include text and PDF)
            else:
                messages.error(request, 'Error saving form')
            return redirect("quoting:after_request", obj_id, True)
    request_form = RequestForm()
    requests = RequestForQuote.objects.all()
    return render(request=request, template_name="quoting_app/requestform.html", context={'request_form':request_form, 'requests':requests, 'requestee':requestee})

@login_required
def input_pdf(request):
    if request.method == "POST":
        pdf_input = PdfInput(request.POST, request.FILES)
        if pdf_input.is_valid():
            pdf_input.save()
            messages.success(request, 'Quote info input successfully')
        else:
            messages.error(request, 'Error inputting Quote information')
        return redirect("quoting:quotes_index")
    pdf_input = PdfInput()
    quote = Quote.objects.all()
    return render(request, "quoting_app/PDFInput.html", context = {'pdf_input': pdf_input, 'quote': quote})

def create_user(request):
    if request.method == "POST":
        user_create = CreateUserForm(request.POST, request.FILES)
        if user_create.is_valid():
            user_create.save()
            messages.success(request, 'User information input successfully')
        else:
            messages.error(request, 'Error inputting User information')
        return redirect("quoting:home")
    user_create = CreateUserForm()
    user = CreateUserAccount.objects.all()
    return render(request, "quoting_app/userform.html", context = {'user_create': user_create, 'user': user})

@login_required
def request_detail(request, requestid):
    request_data = get_object_or_404(RequestForQuote, pk=requestid)
    return render(request, 'requests/detail.html', {'request_data': request_data, 'just_submitted': False})


@login_required
def after_request(request, requestid, just_submitted):
    request_data = get_object_or_404(RequestForQuote, pk=requestid)
    return render(request, 'requests/detail.html', {'request_data': request_data, 'just_submitted': True})


@login_required
def quotes_index(request): #TODO add indicators to indicate missing fields and an ignore warnings option
    latest_quote_list = Quote.objects.order_by('-creation_date')[:25] #TODO add selection option to change number of viewable quotes (do same for requests)
    context = {
        'latest_quote_list': latest_quote_list,
    }
    return render(request, 'quotes/index.html', context)


@login_required
def quote_detail(request, quoteid):
    quote_data = get_object_or_404(Quote, pk=quoteid)
    return render(request, 'quotes/detail.html', {'quote_data': quote_data}) #TODO make sure each request and quote has a one-to-one relation


@login_required
def quote_pdf(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="quote.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    
    # coordinates are (612,792) 1 inch = 72?
    p.drawString(72, 720, "Ye ye")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response

