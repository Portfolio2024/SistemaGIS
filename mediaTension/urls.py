from django.urls import path
from mediaTension.views import *

    #mediatension
urlpatterns = [
    path('list/DU', MediaTensionListView, name='mediatension_list_DU'),
    path('add/DU',crear_lista_diagramas, name='crear_lista_diagramas'),
    path('list/edit/<id>', editar_lista_diagramas, name='editar_lista_diagramas'),
    path('list/delete/DU/<id>', borrar_lista_diagramas, name='borrar_lista_diagramas'),
    path('list/Fotos', MediaTensionListView2, name='mediatension_list_Fotos'),
    path('add/Fotos',crear_lista_fotos, name='crear_lista_fotos'),
    path('list/fotos/edit/<id>', editar_lista_fotos, name='editar_lista_fotos'),
    path('list/delete/Fotos/<id>', borrar_lista_fotos, name='borrar_lista_fotos'),
    path('list/Metrado', MediaTensionListView3, name='mediatension_list_Metrados'),
    path('add/Metrado',crear_metrados, name='crear_metrados'),
    path('list/metrado/edit/<id>', editar_metrados, name='editar_metrados'),
    path('list/delete/Metrado/<id>', borrar_metrados, name='borrar_metrados'),
    path('list/Planos', MediaTensionListView4, name='mediatension_list_Planos'),
    path('add/Planos',crear_planos, name='crear_planos'),
    path('list/planos/edit/<id>', editar_planos, name='editar_planos'),
    path('list/delete/Planos/<id>', borrar_planos, name='borrar_planos'),
  ]