from django.db import models
from django.conf import settings

# Create your models here.

class Catastro(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='Catastro/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Catastro'
        verbose_name_plural = 'Catastros'
        db_table = 'Catastro'
        ordering = ['id']