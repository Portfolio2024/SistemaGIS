from django.shortcuts import render, redirect
from django.views.generic import ListView
from mediaTension.models import *
from .forms import *
from django.contrib import messages

# listado en Media Tensión
def MediaTensionListView(request):
    title = 'Listado de Diagramas Unifilares'
    # Recupera todas las instancias de Transmision desde la base de datos
    mediaTension = MediaTension1.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'list_DU.html', {'mediaTension': mediaTension, 'title': title})

#@login_required
def MediaTensionListView2(request):
    title = 'Fotos por AMT de Media Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    mediaTension1 = MediaTension2.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'list_Fotos.html', {'mediaTension1': mediaTension1, 'title': title})

#@login_required
def MediaTensionListView3(request):
    title = 'Listado de Metrados de AMT de Media Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    mediaTension2 = MediaTension3.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'list_Metrado.html', {'mediaTension2': mediaTension2, 'title': title})

#@login_required
def MediaTensionListView4(request):
    title = 'Listado de planos de AMT de Media Tensión'
    # Recupera todas las instancias de Transmision desde la base de datos
    mediaTension3 = MediaTension4.objects.all()    
    # Pasa las transmisiones a la plantilla HTML
    return render(request, 'list_Planos.html', {'mediaTension3': mediaTension3, 'title': title})

# Creación en Media Tensión

def crear_lista_diagramas(request):
    title = 'Creacion de Diagramas Unifilares'
    if request.method == 'POST':
        form = MediaTension1Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Archivo creado satisfactoriamente!')
            return redirect('mediatension_list_DU')  # Redirige a la vista de lista de registros
    else:
        form = MediaTension1Form()

    return render(request, 'crear_DU.html', {'form': form, 'title': title})

def crear_lista_fotos(request):
    title = 'Creacion de Fotos por AMT de Media Tensión'
    if request.method == 'POST':
        form1 = MediaTension2Form(request.POST, request.FILES)
        if form1.is_valid():
            form1.save()
            messages.success(request, 'Archivo creado satisfactoriamente!')
            return redirect('mediatension_list_Fotos')  # Redirige a la vista de lista de registros
    else:
        form = MediaTension2Form()

    return render(request, 'crear_fotos.html', {'form1': form, 'title': title})

def crear_metrados(request):
    title = 'Creacion de Listado de Metrados de AMT de Media Tensión'
    if request.method == 'POST':
        form2 = MediaTension3Form(request.POST, request.FILES)
        if form2.is_valid():
            form2.save()
            messages.success(request, 'Archivo creado satisfactoriamente!')
            return redirect('mediatension_list_Metrados')  # Redirige a la vista de lista de registros
    else:
        form = MediaTension3Form()

    return render(request, 'crear_metrado.html', {'form2': form, 'title': title})

def crear_planos(request):
    title = 'Creacion de planos de AMT de Media Tensión'
    if request.method == 'POST':
        form3 = MediaTension4Form(request.POST, request.FILES)
        if form3.is_valid():
            form3.save()
            messages.success(request, 'Archivo creado satisfactoriamente!')
            return redirect('mediatension_list_Planos')  # Redirige a la vista de lista de registros
    else:
        form = MediaTension4Form()

    return render(request, 'crear_planos.html', {'form3': form, 'title': title})

def editar_lista_diagramas(request, id):
    title = 'Edición de archivos de Diagramas Unifilares'
    Mediatension_DU = MediaTension1.objects.get(id=id)
    if request.method == 'POST':
        form = MediaTension1Form(request.POST, request.FILES, instance=Mediatension_DU)
        if form.is_valid():
            form.save()
            messages.success(request, 'Archivo editado satisfactoriamente!')
            return redirect('mediatension_list_DU')  # Redirige a la vista de lista de registros
    else:
        form = MediaTension1Form(instance=Mediatension_DU)

    return render(request, 'editar_DU.html', {'form': form, 'title': title})

def editar_lista_fotos(request, id):
    title = 'Edición de archivos de Fotos por AMT de Media Tensión'
    Mediatension_Fotos = MediaTension2.objects.get(id=id)
    if request.method == 'POST':
        form1 = MediaTension2Form(request.POST, request.FILES, instance=Mediatension_Fotos)
        if form1.is_valid():
            form1.save()
            messages.success(request, 'Archivo editado satisfactoriamente!')
            return redirect('mediatension_list_Fotos')  # Redirige a la vista de lista de registros
    else:
        form1 = MediaTension2Form(instance=Mediatension_Fotos)

    return render(request, 'editar_fotos.html', {'form1': form1, 'title': title})

def editar_metrados(request, id):
    title = 'Edición de archivos de Metrados de AMT de Media Tensión'
    Mediatension_Metrados = MediaTension3.objects.get(id=id)
    if request.method == 'POST':
        form2 = MediaTension3Form(request.POST, request.FILES, instance=Mediatension_Metrados)
        if form2.is_valid():
            form2.save()
            messages.success(request, 'Archivo editado satisfactoriamente!')
            return redirect('mediatension_list_Metrados')  # Redirige a la vista de lista de registros
    else:
        form2 = MediaTension3Form(instance=Mediatension_Metrados)

    return render(request, 'editar_metrado.html', {'form2': form2, 'title': title})

def editar_planos(request, id):
    title = 'Edición de planos de AMT de Media Tensión'
    Mediatension_Planos = MediaTension4.objects.get(id=id)
    if request.method == 'POST':
        form3 = MediaTension4Form(request.POST, request.FILES, instance=Mediatension_Planos)
        if form3.is_valid():
            form3.save()
            messages.success(request, 'Archivo editado satisfactoriamente!')
            return redirect('mediatension_list_Planos')  # Redirige a la vista de lista de registros
    else:
        form3 = MediaTension4Form(instance=Mediatension_Planos)

    return render(request, 'editar_planos.html', {'form3': form3, 'title': title})

def borrar_lista_diagramas(request, id):
    Mediatension_DU = MediaTension1.objects.get(id=id)
    Mediatension_DU.delete()
    messages.success(request, 'Archivo eliminado satisfactoriamente!')

    return redirect('mediatension_list_DU')


def borrar_lista_fotos(request, id):
    Mediatension_Fotos = MediaTension2.objects.get(id=id)
    Mediatension_Fotos.delete()
    messages.success(request, 'Archivo eliminado satisfactoriamente!')

    return redirect('mediatension_list_Fotos')

def borrar_metrados(request, id):
    Mediatension_Metrados = MediaTension3.objects.get(id=id)
    Mediatension_Metrados.delete()
    messages.success(request, 'Archivo eliminado satisfactoriamente!')

    return redirect('mediatension_list_Metrados')

def borrar_planos(request, id):
    Mediatension_Planos = MediaTension4.objects.get(id=id)
    Mediatension_Planos.delete()
    messages.success(request, 'Archivo eliminado satisfactoriamente!')

    return redirect('mediatension_list_Planos')