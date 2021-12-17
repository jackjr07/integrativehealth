from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password2')
            messages.success(request, f'You account has been created!')
            return redirect('login')
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg} : {form.error_messages[msg]}")
            return render(request, 'users/register.html', {'form':form})
    form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

def login(request):
    return render(request, 'users/login.html')

