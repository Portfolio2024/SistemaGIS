from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages

def index(request):
    return render(request, 'home.html')

def lista_transmisiones(request):
    title = 'Listado de Diagramas Unifilares'
    # Recupera todas las instancias de Transmision desde la base de datos
    transmisiones = Transmision.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'lista_transmisiones.html', {'transmisiones': transmisiones, 'title': title})

def lista_varios(request):
    title = 'Listado de archivos de Transmision'
    # Recupera todas las instancias de Transmision desde la base de datos
    transmisiones = Transmision1.objects.all()
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'lista_varios.html', {'transmisiones': transmisiones, 'title': title})

# @staff_member_required(login_url='login') 
def crear_lista_transmisiones(request):
    title = 'Creacion de listado de Diagramas Unifilares'
    if request.method == 'POST':
        form = TransmisionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Archivo creado satisfactoriamente!')
            return redirect('lista_transmisiones')  # Redirige a la vista de lista de registros
    else:
        form = TransmisionForm()

    return render(request, 'crear_transmision.html', {'form': form, 'title': title})

def crear_lista_varios(request):
    title = 'Creacion de archivos'
    if request.method == 'POST':
        form1 = Transmision1Form(request.POST, request.FILES)
        if form1.is_valid():
            form1.save()
            messages.success(request, 'Archivo creado satisfactoriamente!')
            return redirect('lista_varios')  # Redirige a la vista de lista de registros
    else:
        form = Transmision1Form()

    return render(request, 'crear_varios.html', {'form1': form, 'title': title})

def borrar_lista_transmisiones(request, id):
    transmision_DU = Transmision.objects.get(id=id)
    transmision_DU.delete()
    messages.success(request, 'Archivo eliminado satisfactoriamente!')

    return redirect('lista_transmisiones')

def borrar_lista_varios(request, id):
    transmision_varios = Transmision1.objects.get(id=id)
    transmision_varios.delete()
    messages.success(request, 'Archivo eliminado satisfactoriamente!')

    return redirect('lista_varios')

def editar_lista_transmisiones(request, id):
    title = 'Edición de archivos de Diagramas Unifilares'
    transmision_DU = Transmision.objects.get(id=id)
    if request.method == 'POST':
        form = TransmisionForm(request.POST, request.FILES, instance=transmision_DU)
        if form.is_valid():
            form.save()
            messages.success(request, 'Archivo editado satisfactoriamente!')
            return redirect('lista_transmisiones')  # Redirige a la vista de lista de registros
    else:
        form = TransmisionForm(instance=transmision_DU)

    return render(request, 'editar_transmision.html', {'form': form, 'title': title})

def editar_lista_varios(request, id):
    title = 'Edición de archivos de Transmision'
    transmision_varios = Transmision1.objects.get(id=id)
    if request.method == 'POST':
        form1 = Transmision1Form(request.POST, request.FILES, instance=transmision_varios)
        if form1.is_valid():
            form1.save()
            messages.success(request, 'Archivo editado satisfactoriamente!')
            return redirect('lista_varios')  # Redirige a la vista de lista de registros
    else:
        form1 = Transmision1Form(instance=transmision_varios)

    return render(request, 'editar_varios.html', {'form1': form1, 'title': title})



    

