from django.db import models
from django.conf import settings

#Transmisión
class Transmision(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='Transmision/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'DiagramasUnifilares'
        verbose_name_plural = 'Transmisions'
        db_table = 'transmision'
        ordering = ['id']

class Transmision1(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='Transmision/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Varios'
        verbose_name_plural = 'Transmisions1'
        db_table = 'transmision_varios'
        ordering = ['id']
