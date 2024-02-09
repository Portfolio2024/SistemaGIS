from django.contrib import admin
from .models import *

class EstructuraAdmin(admin.ModelAdmin):
    list_display = ('ETIQUETA', 'LATITUD', 'LONGITUD')  # Define los campos a mostrar en la lista de registros
    list_filter = ('PROPIETARIO', 'ESTADO')  # Agrega filtros en el panel de administración
    search_fields = ('ETIQUETA', 'TIPO', 'PROPIETARIO')  # Habilita la búsqueda por estos campos
    list_per_page = 10  # Establece la cantidad de registros por página


admin.site.register(Estructura, EstructuraAdmin)


class Tramo_MTAdmin(admin.ModelAdmin):
    list_display = ('PROPIEDAD',)  # Define los campos a mostrar en la lista de registros
    list_per_page = 10 
    
    
admin.site.register(Tramo_MT, Tramo_MTAdmin)



