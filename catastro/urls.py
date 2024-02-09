from django.urls import path
from catastro.views import *

urlpatterns = [
    path('list/', ListaCatastro, name='catastro_list'),
    path('add/', crear_catastro, name='crear_catastro'),
    path('list/delete/<id>', borrar_catastro, name='borrar_catastro'),
    path('list/edit/<id>', editar_catastro, name='editar_catastro'),
]
