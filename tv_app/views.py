from django.shortcuts import render, redirect
from .models import Programa
# from django.contrib import messages
# from django.db.models import Q, Max, Count, F

def inicio(request):
    return render(request, 'index.html')

def crear(request):
    Programa.objects.create(titulo=request.POST['titulo'],
                            canal=request.POST['canal'],
                            fecha=request.POST['fecha'],
                            desc=request.POST['desc'])
    return redirect(programa)

def programa(request):
    prog_last = Programa.objects.last()
    context = {
        'prog_last': prog_last,
    }
    return render(request, 'programa.html', context)

def editar(request, id):
    prog = Programa.objects.get(id=id)
    context = {
        'prog': prog,
    }
    if request.method == "POST":
        prog.titulo = request.POST['titulo']
        prog.canal = request.POST['canal']
        prog.fecha = request.POST['fecha']
        prog.desc = request.POST['desc']
        prog.save()
        return redirect(f'/ver/{id}')
    return render(request, 'editar.html', context)

def ver(request, id):
    prog = Programa.objects.get(id=id)
    context = {
        'prog': prog,
    }
    return render(request, 'ver_programa.html', context)

def programas(request):
    programas = Programa.objects.all()
    context = {
        'programas': programas,
    }
    return render(request, 'programas.html', context)

def borrar(request, id):
    eliminar = Programa.objects.get(id=id)
    eliminar.delete()
    return redirect(programas)