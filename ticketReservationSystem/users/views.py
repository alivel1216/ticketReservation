from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from reservas.urls import urlpatterns
from .forms import createdUserForm

# Create your views here.
def registro(request):
    if request.user.is_authenticated:
        return redirect('Home')
    else:
        form = UserCreationForm()
        if request.method == 'POST':
            form = createdUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Se creo una cuenta para '+user)
                return redirect('Login')

        context = {'form': form}
        return render(request, 'users/registro.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('Home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Home')
            else:
                messages.info(request, 'username Or password son incorrectas')
                
        context = {}
        return render(request, 'users/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('Login')