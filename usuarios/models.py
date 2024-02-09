from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario')
  imagen = models.ImageField(default='empty.png', upload_to='perfil/', verbose_name='Imagen del perfil')
  telephone = models.CharField(max_length=50, blank=True, null=True, verbose_name='Teléfono')
  
  class Meta:
    verbose_name = 'perfil'
    verbose_name_plural = 'perfiles'
    ordering = ['-id']
    
  def __str__(self):
    return self.user.username
  


