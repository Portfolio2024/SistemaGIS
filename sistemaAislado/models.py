from django.conf import settings
from django.db import models

# Create your models here.
class Sistema_Aislado(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='Sistema_Aislado/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Sistema_Aislado'
        verbose_name_plural = 'Sistemas_Aislados'
        db_table = 'Sistema_Aislado'
        ordering = ['id'] 