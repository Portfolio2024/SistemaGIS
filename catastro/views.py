from catastro.models import *
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages


#@login_required

# Catastro
def ListaCatastro(request):
    title = 'Catastro del Proyecto Chavimochic'
    # Recupera todas las instancias de Transmision desde la base de datos
    catastro = Catastro.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'lista_catastro.html', {'catastro': catastro, 'title': title})

def crear_catastro(request):
    title = 'Creacion de nuevo Catastro del Proyecto Chavimochic'
    if request.method == 'POST':
        form = catastroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Archivo creado satisfactoriamente!')
            return redirect('catastro_list')  # Redirige a la vista de lista de registros
    else:
        form = catastroForm()

    return render(request, 'crear_catastro.html', {'form': form, 'title': title})

def borrar_catastro(request, id):
    Catastro.objects.get(id=id).delete()
    messages.success(request, 'Archivo eliminado satisfactoriamente!')
    return redirect('catastro_list')

def editar_catastro(request, id):
    title = 'Edición de Catastro del Proyecto Chavimochic'
    catastro = Catastro.objects.get(id=id)
    if request.method == 'POST':
        form = catastroForm(request.POST, request.FILES, instance=catastro)
        if form.is_valid():
            form.save()
            messages.success(request, 'Archivo editado satisfactoriamente!')
            return redirect('catastro_list')  # Redirige a la vista de lista de registros
    else:
        form = catastroForm(instance=catastro)

    return render(request, 'editar_catastro.html', {'form': form, 'title': title})


