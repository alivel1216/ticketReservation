from django.shortcuts import render
from vuelos.models import Vuelos 
# Create your views here.

def vuelos(request):
    vuelos=Vuelos.objects.all()
    return render(request, 'vuelos/vuelos.html',{"vuelos":vuelos})
