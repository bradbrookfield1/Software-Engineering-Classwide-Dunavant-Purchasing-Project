from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from . import forms
from .models import EquipmentRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def landing(request):
    return render(request, 'landing.html')

@login_required()
def form_view(request):
    if request.method == 'POST':
        form = forms.RequestForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.author= request.user
            instance.save()
            return redirect('user_requests:ty')
    else:
        form = forms.RequestForm()
    return render(request, 'form.html', {'form': form} )

@login_required()
def thank_you(request):
    return render(request, 'thank_you.html')

@login_required()
def ER_list(request):
    ER= EquipmentRequest.objects.filter(user_request__author=request.user).order_by('user_request__date_created')
    return render(request,'ER_list.html', {'ER':ER})

@login_required()
def profile(request):
    return render(request,'profile.html')
