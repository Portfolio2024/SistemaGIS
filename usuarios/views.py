from typing import Any
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, User
from django.urls import reverse_lazy
from .forms import FormularioRegistroUsuario
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic.base import TemplateView
from django.views.generic import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import update_session_auth_hash

def login_user(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)      
      messages.success(request, 'Haz ingresado Correctamente...!')
      return redirect('dashboard')    
    else:
      messages.success(request, ('Ha ocurrido un error al intentar loguearte intentalo de nuevo!!!'))
      return redirect('login')
  else:
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')

def registrar_usuario(request):
    title = 'Registro de usuarios'
    if request.method == 'POST':
        formulario = FormularioRegistroUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.info(request, ("Te has registrado correctamente!!!"))
            return redirect('dashboard')
    else:
        formulario = FormularioRegistroUsuario()
        
    return render(request, 'registrar_usuario.html',{'formulario':formulario, 'title':title})
  
def listar_perfil(request):
  title = 'Perfil de Usuario'
  return render(request, 'perfil.html',{'title':title})

@method_decorator(login_required, name= 'dispatch')
class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = 'update_perfil.html'
    form_class = ProfileForm
    success_url = reverse_lazy('listar_perfil')

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['title'] = 'Actualiza tu Perfil'
       return context

    def get_object(self, queryset=None):
        # Obtén el perfil del usuario actual o crea uno nuevo si no existe
        listar_perfil, created = Profile.objects.get_or_create(user=self.request.user)
        return listar_perfil

    def form_valid(self, form):
        # Asigna el usuario actual al formulario antes de guardarlo
        form.instance.user = self.request.user
        return super().form_valid(form)

#Cambiar contraseña del usuario
class ProfilePasswordChangeView(PasswordChangeView):
    template_name = 'update_password.html'
    success_url = reverse_lazy('listar_perfil')
   
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['password_changed'] = self.request.session.get('password_changed', False)
       context['title'] = 'Cambia tu Contraseña'
       return context
    
    def form_valid(self, form):
       messages.success(self.request, 'Tu contraseña ha sido cambiada')
       update_session_auth_hash(self.request, form.user)
       self.request.session['password_changed'] = True
       return super().form_valid(form)
    
    def form_invalid(self, form):
       messages.error(self.request, 'Error al cambiar tu contraseña')       
       return super().form_invalid(form)


