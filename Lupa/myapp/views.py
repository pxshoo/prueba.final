# Create your views here.
from django.shortcuts import render


def login_view(request):
    return render(request, 'paginas/Login.html')

def prueba_view(request):
    return render(request, 'paginas/prueba.html')

def Nosotros_view(request):
    return render(request, 'paginas/Nosotros.html')

def Register_view(request):
    return render(request, 'paginas/Register.html')
