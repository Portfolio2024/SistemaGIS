from django.urls import path
from sistemaAislado.views import *

urlpatterns = [
    path('list/', SistemaAislado, name='lista_aislado'),
    path('add/', crear_SistemaAislado, name='crear_SistemaAislado'),
    path('list/delete/<id>', borrar_SistemaAislado, name='borrar_SistemaAislado'),
    path('list/edit/<id>', editar_SistemaAislado, name='editar_SistemaAislado'),
]