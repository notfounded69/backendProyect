from django.shortcuts import render
from .models import Agentes

def valorant(request):
    agentes=Agentes.objects.all
    return render(request,'valorant/agentes.html',{'agentes':agentes})
