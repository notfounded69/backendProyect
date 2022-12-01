from django.shortcuts import render

def home(request):
    return render(request,'core/home.html')

def tienda(request):
    return render(request,'core/tienda.html')

def skins(request):
    return render(request,'core/skins.html')





