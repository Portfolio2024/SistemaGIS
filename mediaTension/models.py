from django.conf import settings
from django.db import models

# Create your models here.
#Media Tensión
class MediaTension(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='MediaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Diagramas'
        verbose_name_plural = 'MediaTensions'
        db_table = 'MediaTension'
        ordering = ['id']

class MediaTension1(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='MediaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'MediaTension_DU'
        verbose_name_plural = 'MediaTensions_DU'
        db_table = 'MediaTension1'
        ordering = ['id']

class MediaTension2(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='MediaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'MediaTension_FOTOS'
        verbose_name_plural = 'MediaTensions_FOTOS'
        db_table = 'MediaTension2'
        ordering = ['id']

class MediaTension3(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='MediaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'MediaTension_METRADO'
        verbose_name_plural = 'MediaTensions_METRADO'
        db_table = 'MediaTension3'
        ordering = ['id']

class MediaTension4(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='MediaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'MediaTension_PLANOS'
        verbose_name_plural = 'MediaTensions_PLANOS'
        db_table = 'MediaTension4'
        ordering = ['id']
