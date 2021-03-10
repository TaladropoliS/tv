from django.shortcuts import render, redirect
from .models import Programa
from django.contrib import messages
from django.db.models import Q, Max, Count, F

def inicio(request):
    return render(request, 'index.html')

def crear(request):
    Programa.objects.create(titulo=request.POST['titulo'],
                            canal=request.POST['canal'],
                            fecha=request.POST['fecha'],
                            desc=request.POST['desc'])
    return redirect(programa)

def programa(request):
    return render(request, 'programa.html', context)