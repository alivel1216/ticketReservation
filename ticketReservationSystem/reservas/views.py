  
from django.shortcuts import render, redirect
from django.http import HttpResponse
from reservas.models import ReservarForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'reservas/index.html')

@login_required(login_url='Login')
def reservaciones(request):
    form = ReservarForm()
    if request.method == 'POST':
        form = ReservarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form':form}
    return render(request, 'reservas/reservas.html', context)