from django.urls import path, include 
from django.contrib import admin
from django.views.generic.base import TemplateView
from . import views

app_name = 'quoting'
urlpatterns = [
    #path('', TemplateView.as_view(template_name='home.html'), name='home'), 
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='home'),
    path('requests/', views.requests_index, name='requests_index'),
    path('requestform/', views.request_form, name='requestform'),
    path('requests/<int:requestid>/', views.request_detail, name='request_detail'), #TODO replace requestid with generated unique id?
    path('requests/<int:requestid>/submitted=<slug:just_submitted>/', views.after_request, name='after_request'),
    path('quotes/', views.quotes_index, name='quotes_index'),
    path('quotes/<int:quoteid>/', views.quote_detail, name='quote_detail'),
    path('pdf/', views.quote_pdf, name='quote_pdf'),
    path('inputpdf/', views.input_pdf, name = 'input_pdf'),
    path('createuser/', views.create_user, name = 'create_user'),
]
