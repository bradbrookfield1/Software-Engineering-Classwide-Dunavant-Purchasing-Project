from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, AdminRegisterForm
from .models import admin_Key


@login_required
def is_admin(self):
    if self.admin_Key == admin_Key:
        return True
    else:
        return False


@login_required
def profile(request):
    return render(request, 'users/profile.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account made for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def register_admin(request):
    if request.method == 'POST':
        form = AdminRegisterForm(request.POST)
        request_Admin_Key = form['admin_Key'].value()
        if form.is_valid() and (request_Admin_Key == admin_Key):
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Admin account made for {username}!')
            return redirect('login')
    else:
        form = AdminRegisterForm()
    return render(request, 'users/register_admin.html', {'form': form})
