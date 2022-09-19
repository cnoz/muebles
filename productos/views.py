from django.shortcuts import render
from django.http import HttpResponse
from productos.models import *

# Create your views here.


def inicio(request):
    return render(request, 'index.html')


def mesas(request):
    return render(request, 'mesas.html')

