from sistemaAislado.models import *
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages

# Create your views here.
def SistemaAislado(request):
    title = 'Listado del Sistema Aislado'
    # Recupera todas las instancias de Transmision desde la base de datos
    sistema_aislado = Sistema_Aislado.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'lista_aislado.html', {'sistema_aislado': sistema_aislado, 'title': title})

def crear_SistemaAislado(request):
    title = 'Creacion de planos del Sistema Aislado'
    if request.method == 'POST':
        form = Sistema_AisladoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Archivo creado satisfactoriamente!')
            return redirect('lista_aislado')  # Redirige a la vista de lista de registros
    else:
        form = Sistema_AisladoForm()

    return render(request, 'crear_sistema_aislado.html', {'form': form, 'title': title})

def borrar_SistemaAislado(request, id):
    sistema_aislado = Sistema_Aislado.objects.get(id=id)
    sistema_aislado.delete()
    messages.success(request, 'Archivo eliminado satisfactoriamente!')
    return redirect('lista_aislado')

def editar_SistemaAislado(request, id):
    title = 'Edición de planos del Sistema Aislado'    
    sistema_aislado = Sistema_Aislado.objects.get(id=id)
    if request.method == 'POST':
        form = Sistema_AisladoForm(request.POST, request.FILES, instance=sistema_aislado)
        if form.is_valid():
            form.save()
            messages.success(request, 'Archivo editado satisfactoriamente!')
            return redirect('lista_aislado')  # Redirige a la vista de lista de registros
    else:
        form = Sistema_AisladoForm(instance=sistema_aislado)

    return render(request, 'editar_sistema_aislado.html', {'form': form, 'title': title})
