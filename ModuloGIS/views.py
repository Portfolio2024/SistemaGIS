from django.conf import settings
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.template import loader
import os
from .forms import KMLFileForm
import json
from django.db.models import Sum
from django.contrib.auth.models import User
from django.db.models import Count

@staff_member_required
def cargar_excel(request):
    if request.method == 'POST':
        # Obtén el archivo Excel del formulario
        archivo_excel = request.FILES['archivo_excel']
        
        # Lee el archivo Excel usando pandas
        try:
            df = pd.read_excel(archivo_excel)
            df.fillna(0, inplace=True)
        except pd.errors.EmptyDataError:
            messages.error(request, 'El archivo Excel está vacío.')
            return redirect('cargar_excel')
        
        # Verifica duplicados en función del campo CODIGO
        etiquetas_existentes = Estructura.objects.values_list('ETIQUETA', flat=True)
        duplicados = df[df['ETIQUETA'].isin(etiquetas_existentes)]
        
        if not duplicados.empty:
            messages.error(request, 'Se encontraron códigos duplicados en el archivo Excel.')
        else:
            # Carga los datos desde el archivo Excel al modelo Estructura
            df_dict = df.to_dict(orient='records')
            for data in df_dict:
                estructura = Estructura(**data)
                estructura.save()
            messages.success(request, 'Los datos se han cargado exitosamente.')
        return redirect('cargar_excel')  # Redirige nuevamente al formulario después de la carga

    return render(request, 'cargar_excel.html')  # Renderiza el formulario de carga de Excel

@staff_member_required
def listar_estructuras(request):
    title = 'Listado de Estructuras'
    estructuras = Estructura.objects.all()
    return render(request, 'listar_estructuras.html', {'estructuras': estructuras,'title': title})


@staff_member_required
def cargar_excel_vanos(request):
    if request.method == 'POST' and request.FILES.get('archivo_excel'):
        archivo_excel = request.FILES['archivo_excel']

        if archivo_excel.name.endswith('.xlsx'):
            try:
                df = pd.read_excel(archivo_excel)

                registros_creados = 0
                registros_duplicados = 0

                for index, row in df.iterrows():
                    id = row.get('ID')
                    if not Tramo_MT.objects.filter(ID=id).exists():
                        Tramo_MT.objects.create(
                            ID=id,
                            AMT=row.get('AMT'),
                            ID_SALIDA_M=row.get('ID_SALIDA_M'),
                            TENSION_NOM=row.get('TENSION_NOM'),
                            ID_CONFIGUR=row.get('ID_CONFIGUR'),
                            PROPIEDAD=row.get('PROPIEDAD'),
                            ESTADO=row.get('ESTADO'),
                            LONGITUD=row.get('LONGITUD'),
                            LATITUD1=row.get('LATITUD1'),
                            LONGITUD1=row.get('LONGITUD1'),
                            LATITUD2=row.get('LATITUD2'),
                            LONGITUD2=row.get('LONGITUD2'),
                            OBSERVACION=row.get('OBSERVACION'),
                            NOMBRE_PROP=row.get('NOMBRE_PROP'),
                            TIPO_CIRCUI=row.get('TIPO_CIRCUI'),
                        )
                        registros_creados += 1
                    else:
                        registros_duplicados += 1

                messages.success(request, f'Se cargaron {registros_creados} registros exitosamente.')
                messages.info(request, f'{registros_duplicados} registros ya existían y se omitieron.')
            except Exception as e:
                messages.error(request, f'Ocurrió un error al cargar el archivo: {str(e)}')
        else:
            messages.error(request, 'El archivo debe ser un archivo Excel (.xlsx).')

        return redirect('cargar_excel_vanos')

    return render(request, 'cargar_excel_vanos.html')

@staff_member_required
def listar_vanos(request):
    title = 'Listado de Vanos'
    tramo = Tramo_MT.objects.all()
    return render(request, 'listar_vanos.html', {'tramo': tramo,'title': title})

@staff_member_required
def cargar_excel_SED(request):
    if request.method == 'POST':
        # Obtén el archivo Excel del formulario
        archivo_excel = request.FILES['archivo_excel']
        
        # Lee el archivo Excel usando pandas
        try:
            df = pd.read_excel(archivo_excel)
            df.fillna(0, inplace=True)
        except pd.errors.EmptyDataError:
            messages.error(request, 'El archivo Excel está vacío.')
            return redirect('cargar_excel')
        
        # Verifica duplicados en función del campo CODIGO
        codigos_existentes = Subestacion.objects.values_list('CODIGO', flat=True)
        duplicados = df[df['CODIGO'].isin(codigos_existentes)]
        
        if not duplicados.empty:
            messages.error(request, 'Se encontraron códigos duplicados en el archivo Excel.')
        else:
            # Carga los datos desde el archivo Excel al modelo Estructura
            df_dict = df.to_dict(orient='records')
            for data in df_dict:
                subestacion = Subestacion(**data)
                subestacion.save()
            messages.success(request, 'Los datos se han cargado exitosamente.')
        return redirect('cargar_excel_SED')  # Redirige nuevamente al formulario después de la carga

    return render(request, 'cargar_excel_SED.html')  # Renderiza el formulario de carga de Excel

@staff_member_required
def listar_SED(request):
    title = 'Listado de Subestaciones'
    subestacion = Subestacion.objects.all()
    return render(request, 'listar_SED.html', {'subestacion': subestacion,'title': title})

@staff_member_required
def upload_kml(request):
    if request.method == 'POST':
        form = KMLFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = KMLFileForm()
    
    kml_files = KMLFile.objects.all()
    
    return render(request, 'cargar_KML.html', {'form': form, 'kml_files': kml_files})

def infraestructura(request):
    title = "Infraestructura Electrica del PECH"
    return render(request, 'infraestructura.html', {'title': title})

@staff_member_required
def cargar_excel_seccionadores(request):
    if request.method == 'POST':
        # Obtén el archivo Excel del formulario
        archivo_excel = request.FILES['archivo_excel']
        
        # Lee el archivo Excel usando pandas
        try:
            df = pd.read_excel(archivo_excel)
            df.fillna(0, inplace=True)
        except pd.errors.EmptyDataError:
            messages.error(request, 'El archivo Excel está vacío.')
            return redirect('cargar_excel')
        
        # Verifica duplicados en función del campo CODIGO
        codigos_existentes = Seccionador.objects.values_list('codigo', flat=True)
        duplicados = df[df['codigo'].isin(codigos_existentes)]
        
        if not duplicados.empty:
            messages.error(request, 'Se encontraron códigos duplicados en el archivo Excel.')
        else:
            # Carga los datos desde el archivo Excel al modelo Estructura
            df_dict = df.to_dict(orient='records')
            for data in df_dict:
                seccionador = Seccionador(**data)
                seccionador.save()
            messages.success(request, 'Los datos se han cargado exitosamente.')
        return redirect('cargar_excel_seccionadores')  # Redirige nuevamente al formulario después de la carga

    return render(request, 'cargar_excel_seccionadores.html')  # Renderiza el formulario de carga de Excel

def listar_seccionadores(request):
    title = 'Listado de Seccionadores'
    seccionador = Seccionador.objects.all()
    return render(request, 'listar_seccionadores.html', {'seccionador': seccionador,'title': title})

def dashboard(request):
    title = "Dashboard"
    subestaciones = Subestacion.objects.all()
    subestacion_count = Subestacion.objects.count()
    
    estructuras_no_bt = Estructura.objects.exclude(CLASIFICACI="BT")
    count_no_bt = estructuras_no_bt.count()
    #estructura_count = Estructura.objects.count()
    
    total_longitud_tramo_mt = Tramo_MT.objects.aggregate(total_longitud=Sum('LONGITUD'))
    total_longitud_km = total_longitud_tramo_mt['total_longitud'] / 1000
    total_longitud_km_redondeado = round(total_longitud_km, 2)
    
    propiedades = Subestacion.objects.values('PROPIEDAD').annotate(count=models.Count('PROPIEDAD')) 
    data = [{'name': propiedad['PROPIEDAD'], 'y': propiedad['count']} for propiedad in propiedades]
    data_json = json.dumps(data)  
    
    subestaciones = Subestacion.objects.values('ID_SALIDAMT').annotate(count=models.Count('ID_SALIDAMT'))
    data1 = [{'name': subestacion['ID_SALIDAMT'], 'y': subestacion['count']} for subestacion in subestaciones]
    data_json1 = json.dumps(data1)
    
    estructuras_por_amt = Estructura.objects.values('AMT').annotate(count=Count('AMT'))
    data2 = [{'name': estructura['AMT'], 'y': estructura['count']} for estructura in estructuras_por_amt]
    data_json2 = json.dumps(data2)
    
    seccionadores_por_amt = Seccionador.objects.values('amt').annotate(count=Count('amt'))
    data3 = [{'name': seccionador['amt'], 'y': seccionador['count']} for seccionador in seccionadores_por_amt]
    data_json3 = json.dumps(data3)

    total_usuarios = User.objects.count()
    
    return render(request, 'dashboard.html',{'data': data_json, 'title': title, 'subestacion_count': subestacion_count,
    'count_no_bt': count_no_bt, 'total_longitud_km': total_longitud_km_redondeado, 'data1': data_json1,
    'subestaciones': subestaciones, 'total_usuarios': total_usuarios, 'data2': data_json2, 'data3': data_json3})
    
