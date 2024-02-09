from django.urls import path
from transmision.views import *

urlpatterns = [
    path('list/', lista_transmisiones, name='lista_transmisiones'),
    path('varios/', lista_varios, name='lista_varios'),
    path('add/lista', crear_lista_transmisiones, name='crear_lista_transmisiones'),
    path('add/varios', crear_lista_varios, name='crear_lista_varios'),
    path('list/delete/<id>', borrar_lista_transmisiones, name='borrar_lista_transmisiones'),
    path('varios/delete/<id>', borrar_lista_varios, name='borrar_lista_varios'),
    path('list/edit/<id>', editar_lista_transmisiones, name='editar_transmisiones'),
    path('varios/edit/<id>', editar_lista_varios, name='editar_varios'),
]

