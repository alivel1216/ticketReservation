from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import PagarForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='Login')
def pagos(request):
    form = PagarForm()
    if request.method == 'POST':
        form = PagarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'pagos/pagos.html', context)