from django.urls import path
from . import views

urlpatterns = [   
    path('', views.infraestructura, name='infraestructura'),
]