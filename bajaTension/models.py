from django.conf import settings
from django.db import models
from datetime import datetime

#Baja Tension - AL01
class BajaTension(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH001'
        db_table = 'BajaTension'
        ordering = ['id']

class BajaTension2(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH002'
        db_table = 'BajaTension2'
        ordering = ['id']

class BajaTension3(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH003'
        db_table = 'BajaTension3'
        ordering = ['id']

class BajaTension4(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH004'
        db_table = 'BajaTension4'
        ordering = ['id']

class BajaTension5(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH005'
        db_table = 'BajaTension5'
        ordering = ['id']

class BajaTension6(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH006'
        db_table = 'BajaTension6'
        ordering = ['id']

class BajaTension7(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH007'
        db_table = 'BajaTension7'
        ordering = ['id']

class BajaTension8(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH008'
        db_table = 'BajaTension8'
        ordering = ['id']

class BajaTension9(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH009'
        db_table = 'BajaTension9'
        ordering = ['id']

class BajaTension10(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH010'
        db_table = 'BajaTension10'
        ordering = ['id']

class BajaTension62(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH062'
        db_table = 'BajaTension62'
        ordering = ['id']

class BajaTension64(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH064'
        db_table = 'BajaTension64'
        ordering = ['id']

class BajaTension65(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH065'
        db_table = 'BajaTension65'
        ordering = ['id']

class BajaTension66(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH066'
        db_table = 'BajaTension66'
        ordering = ['id']

class BajaTension67(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH067'
        db_table = 'BajaTension67'
        ordering = ['id']

class BajaTension68(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH068'
        db_table = 'BajaTension68'
        ordering = ['id']

class BajaTension69(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH069'
        db_table = 'BajaTension69'
        ordering = ['id']

class BajaTension70(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH070'
        db_table = 'BajaTension70'
        ordering = ['id']

class BajaTension71(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH071'
        db_table = 'BajaTension71'
        ordering = ['id']

class BajaTension72(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH072'
        db_table = 'BajaTension72'
        ordering = ['id']

class BajaTension73(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH073'
        db_table = 'BajaTension73'
        ordering = ['id']

class BajaTension120(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH120'
        db_table = 'BajaTension120'
        ordering = ['id']

class BajaTension121(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH121'
        db_table = 'BajaTension121'
        ordering = ['id']

class BajaTension122(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH122'
        db_table = 'BajaTension122'
        ordering = ['id']

class BajaTension127(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH127'
        db_table = 'BajaTension127'
        ordering = ['id']

class BajaTension128(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH128'
        db_table = 'BajaTension128'
        ordering = ['id']

class BajaTension129(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH129'
        db_table = 'BajaTension129'
        ordering = ['id']

class BajaTension142(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH142'
        db_table = 'BajaTension142'
        ordering = ['id']

class BajaTension158(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH158'
        db_table = 'BajaTension158'
        ordering = ['id']

class BajaTension159(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH159'
        db_table = 'BajaTension159'
        ordering = ['id']

#Baja Tension - AL02

class BajaTension11(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH011'
        db_table = 'BajaTension11'
        ordering = ['id']

class BajaTension12(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH012'
        db_table = 'BajaTension12'
        ordering = ['id']

class BajaTension13(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH013'
        db_table = 'BajaTension13'
        ordering = ['id']

class BajaTension14(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH014'
        db_table = 'BajaTension14'
        ordering = ['id']

class BajaTension15(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH015'
        db_table = 'BajaTension15'
        ordering = ['id']

class BajaTension16(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH016'
        db_table = 'BajaTension16'
        ordering = ['id']

class BajaTension17(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH017'
        db_table = 'BajaTension17'
        ordering = ['id']

class BajaTension18(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH018'
        db_table = 'BajaTension18'
        ordering = ['id']

class BajaTension19(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH019'
        db_table = 'BajaTension19'
        ordering = ['id']

class BajaTension20(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH020'
        db_table = 'BajaTension20'
        ordering = ['id']

class BajaTension21(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH021'
        db_table = 'BajaTension21'
        ordering = ['id']

class BajaTension22(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH022'
        db_table = 'BajaTension22'
        ordering = ['id']

class BajaTension23(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH023'
        db_table = 'BajaTension23'
        ordering = ['id']

class BajaTension24(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH024'
        db_table = 'BajaTension24'
        ordering = ['id']

class BajaTension25(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH025'
        db_table = 'BajaTension25'
        ordering = ['id']

class BajaTension26(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH026'
        db_table = 'BajaTension26'
        ordering = ['id']

class BajaTension27(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH027'
        db_table = 'BajaTension27'
        ordering = ['id']

class BajaTension28(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH028'
        db_table = 'BajaTension28'
        ordering = ['id']

class BajaTension30(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH030'
        db_table = 'BajaTension30'
        ordering = ['id']

class BajaTension31(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH031'
        db_table = 'BajaTension31'
        ordering = ['id']

class BajaTension32(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH032'
        db_table = 'BajaTension32'
        ordering = ['id']

class BajaTension33(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH033'
        db_table = 'BajaTension33'
        ordering = ['id']

class BajaTension34(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH034'
        db_table = 'BajaTension34'
        ordering = ['id']

class BajaTension74(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH074'
        db_table = 'BajaTension74'
        ordering = ['id']

class BajaTension75(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH075'
        db_table = 'BajaTension75'
        ordering = ['id']

class BajaTension76(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH076'
        db_table = 'BajaTension76'
        ordering = ['id']

class BajaTension77(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH077'
        db_table = 'BajaTension77'
        ordering = ['id']

class BajaTension78(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH078'
        db_table = 'BajaTension78'
        ordering = ['id']

class BajaTension79(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH079'
        db_table = 'BajaTension79'
        ordering = ['id']

class BajaTension80(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH080'
        db_table = 'BajaTension80'
        ordering = ['id']

class BajaTension81(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH081'
        db_table = 'BajaTension81'
        ordering = ['id']

class BajaTension86(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH086'
        db_table = 'BajaTension86'
        ordering = ['id']

class BajaTension90(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH090'
        db_table = 'BajaTension90'
        ordering = ['id']

class BajaTension91(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH091'
        db_table = 'BajaTension91'
        ordering = ['id']

class BajaTension92(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH092'
        db_table = 'BajaTension92'
        ordering = ['id']

class BajaTension93(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH093'
        db_table = 'BajaTension93'
        ordering = ['id']

class BajaTension94(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH094'
        db_table = 'BajaTension94'
        ordering = ['id']

class BajaTension95(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH095'
        db_table = 'BajaTension95'
        ordering = ['id']

class BajaTension106(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH106'
        db_table = 'BajaTension106'
        ordering = ['id']

class BajaTension107(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH107'
        db_table = 'BajaTension107'
        ordering = ['id']

class BajaTension109(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH109'
        db_table = 'BajaTension109'
        ordering = ['id']

class BajaTension110(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH110'
        db_table = 'BajaTension110'
        ordering = ['id']

class BajaTension111(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH111'
        db_table = 'BajaTension111'
        ordering = ['id']

class BajaTension112(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH112'
        db_table = 'BajaTension112'
        ordering = ['id']

class BajaTension113(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH113'
        db_table = 'BajaTension113'
        ordering = ['id']

class BajaTension114(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH114'
        db_table = 'BajaTension114'
        ordering = ['id']

class BajaTension124(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH124'
        db_table = 'BajaTension124'
        ordering = ['id']

class BajaTension125(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH125'
        db_table = 'BajaTension125'
        ordering = ['id']

class BajaTension126(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH126'
        db_table = 'BajaTension126'
        ordering = ['id']

class BajaTension130(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH130'
        db_table = 'BajaTension130'
        ordering = ['id']

class BajaTension131(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH131'
        db_table = 'BajaTension131'
        ordering = ['id']

#Baja Tension - SSJ001

class BajaTension36(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH036'
        db_table = 'BajaTension36'
        ordering = ['id']

class BajaTension37(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH037'
        db_table = 'BajaTension37'
        ordering = ['id']

class BajaTension38(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH038'
        db_table = 'BajaTension38'
        ordering = ['id']

class BajaTension39(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH039'
        db_table = 'BajaTension39'
        ordering = ['id']

class BajaTension40(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH040'
        db_table = 'BajaTension40'
        ordering = ['id']

class BajaTension63(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH063'
        db_table = 'BajaTension63'
        ordering = ['id'] 

#Baja Tension - SPP001

class BajaTension41(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH041'
        db_table = 'BajaTension41'
        ordering = ['id']

class BajaTension42(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH042'
        db_table = 'BajaTension42'
        ordering = ['id']

class BajaTension43(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH043'
        db_table = 'BajaTension43'
        ordering = ['id']

class BajaTension46(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH046'
        db_table = 'BajaTension46'
        ordering = ['id']

class BajaTension47(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH047'
        db_table = 'BajaTension47'
        ordering = ['id']

class BajaTension48(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH048'
        db_table = 'BajaTension48'
        ordering = ['id']

class BajaTension50(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH050'
        db_table = 'BajaTension50'
        ordering = ['id']

class BajaTension51(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH051'
        db_table = 'BajaTension51'
        ordering = ['id']

class BajaTension52(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH052'
        db_table = 'BajaTension52'
        ordering = ['id']

class BajaTension53(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH053'
        db_table = 'BajaTension53'
        ordering = ['id']

class BajaTension54(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH054'
        db_table = 'BajaTension54'
        ordering = ['id']

class BajaTension55(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH055'
        db_table = 'BajaTension55'
        ordering = ['id']

class BajaTension56(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH056'
        db_table = 'BajaTension56'
        ordering = ['id']

class BajaTension57(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH057'
        db_table = 'BajaTension57'
        ordering = ['id']

class BajaTension58(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH058'
        db_table = 'BajaTension58'
        ordering = ['id']

class BajaTension59(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH059'
        db_table = 'BajaTension59'
        ordering = ['id']

class BajaTension60(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH060'
        db_table = 'BajaTension60'
        ordering = ['id']

class BajaTension61(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH061'
        db_table = 'BajaTension61'
        ordering = ['id']

class BajaTension89(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH089'
        db_table = 'BajaTension89'
        ordering = ['id']

class BajaTension96(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH096'
        db_table = 'BajaTension96'
        ordering = ['id']

class BajaTension97(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH097'
        db_table = 'BajaTension197'
        ordering = ['id']

class BajaTension98(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH098'
        db_table = 'BajaTension98'
        ordering = ['id']

class BajaTension99(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH099'
        db_table = 'BajaTension99'
        ordering = ['id']

class BajaTension100(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH100'
        db_table = 'BajaTension100'
        ordering = ['id']

class BajaTension101(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH101'
        db_table = 'BajaTension101'
        ordering = ['id']


class BajaTension102(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH102'
        db_table = 'BajaTension102'
        ordering = ['id']

class BajaTension153(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH153'
        db_table = 'BajaTension153'
        ordering = ['id']

class BajaTension157(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.FileField(upload_to='BajaTension/%d/%m/%Y')

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'BajaTension'
        verbose_name_plural = 'BajaTensions_PCH157'
        db_table = 'BajaTension157'
        ordering = ['id']
