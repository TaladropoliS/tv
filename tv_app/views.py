from django.shortcuts import render, redirect
# from .models import Usuario, Amigo
from django.contrib import messages
from django.db.models import Q, Max, Count, F

def inicio(request):

    return render(request, 'index.html')