from django.urls import path
from . import views

urlpatterns = [
    path('cargar_excel/', views.cargar_excel, name='cargar_excel'),
    path('listar_estructuras/', views.listar_estructuras, name='listar_estructuras'),
    path('cargar_excel_vanos/', views.cargar_excel_vanos, name='cargar_excel_vanos'),
    path('listar_vanos/', views.listar_vanos, name='listar_vanos'),
    path('cargar_excel_SED/', views.cargar_excel_SED, name='cargar_excel_SED'),
    path('listar_SED/', views.listar_SED, name='listar_SED'),
    path('cargar_excel_seccionadores/', views.cargar_excel_seccionadores, name='cargar_excel_seccionadores'),
    path('listar_seccionadores/', views.listar_seccionadores, name='listar_seccionadores'),
    path('upload_kml/', views.upload_kml, name='upload_kml'),
    path('infraestructura/', views.infraestructura, name='infraestructura'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
