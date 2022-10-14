from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import FieldSelectionList

# Create your views here.
#def generate_report_login(request):
#    if request.method == 'POST':
#        username = request.POST.get('username')
#        password = request.POST.get('password')
#        user = authenticate(request,username=username,password=password)
#        if user is not None:
#            login(request,user)
#            return redirect()
#
#        else:
#            messages.info(request,'Username or password is incorrect')
#            return render()

#    context = {}
#    return render()


#def logout_user(request):
#    logout(request)
#    return redirect(generate_report_login)

#@login_required(login_url=generate_report_login)
#def generate_report(request):
#    if request.method == 'POST':
#        messages.success(request)
#        form = FieldSelectionList(request.POST)
#        if form.is_valid():

