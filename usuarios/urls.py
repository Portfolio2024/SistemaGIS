from django.urls import path
from . import views
from .views import ProfileUpdateView, ProfilePasswordChangeView

urlpatterns = [
    path('', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('registrar_usuario/', views.registrar_usuario, name='registrar_usuario'),
    path('listar_perfil/', views.listar_perfil, name='listar_perfil'),
    path('update_perfil/', ProfileUpdateView.as_view(), name='update_perfil'),
    path('update_password/', views.ProfilePasswordChangeView.as_view(), name='update_password'),
]