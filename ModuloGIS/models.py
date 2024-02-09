from django.db import models

class Estructura(models.Model):
    ID = models.AutoField(primary_key=True)
    CODIGO = models.CharField(max_length=255, null=True, blank=True)
    CODIGO_VNR = models.CharField(max_length=255, null=True, blank=True)
    TIPO = models.CharField(max_length=255, null=True, blank=True)
    PROPIEDAD = models.CharField(max_length=255, null=True, blank=True)
    ESTADO = models.CharField(max_length=255, null=True, blank=True)
    LATITUD = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    LONGITUD = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    CLASIFICACI = models.CharField(max_length=255, null=True, blank=True)
    ALTURA = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    OPERATIVO = models.CharField(max_length=255, null=True, blank=True)
    TIPO_ARMADO = models.CharField(max_length=255, null=True, blank=True)
    PROPIETARIO = models.CharField(max_length=255, null=True, blank=True)
    ANGULO = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    OBSERVACION = models.TextField(null=True, blank=True)
    COMPARTE = models.CharField(max_length=255, null=True, blank=True)
    CODIGO_ARMA = models.CharField(max_length=255, null=True, blank=True)
    TERNAS = models.CharField(max_length=255, null=True, blank=True)
    DISPOSICION = models.CharField(max_length=255, null=True, blank=True)
    FUNCION_ARM = models.CharField(max_length=255, null=True, blank=True)
    ESFUERZO = models.CharField(max_length=255, null=True, blank=True)
    ETIQUETA = models.CharField(max_length=255, null=True, blank=True)
    AMT = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.ETIQUETA
    


class Tramo_MT(models.Model):
    ID = models.AutoField(primary_key=True)
    AMT = models.CharField(max_length=255, null=True, blank=True) 
    ID_SALIDA_M = models.CharField(max_length=255, null=True, blank=True)  # Este campo debe ser único
    TENSION_NOM = models.CharField(max_length=255, null=True, blank=True)
    ID_CONFIGUR = models.IntegerField(null=True, blank=True)
    PROPIEDAD = models.CharField(max_length=255, null=True, blank=True)
    ESTADO = models.CharField(max_length=255, null=True, blank=True)
    LONGITUD = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    LATITUD1 = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    LONGITUD1 = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    LATITUD2 = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    LONGITUD2 = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    OBSERVACION = models.TextField(null=True, blank=True)
    NOMBRE_PROP = models.CharField(max_length=255, null=True, blank=True)
    TIPO_CIRCUI = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.DESCRIPCION)


class Subestacion(models.Model):
    ID = models.AutoField(primary_key=True)
    CODIGO = models.CharField(max_length=255, null=True, blank=True)
    ID_SALIDAMT = models.CharField(max_length=255, null=True, blank=True)
    TENSION1 = models.CharField(max_length=255, null=True, blank=True)
    TENSION2 = models.CharField(max_length=255, null=True, blank=True)
    TENSION3 = models.CharField(max_length=255, null=True, blank=True)
    MAXIMA_DEMA = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    POTENCIA_IN = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    SUBCOMPONEN = models.CharField(max_length=255, null=True, blank=True)
    CODIGO_VNR = models.CharField(max_length=255, null=True, blank=True)
    PROPIEDAD = models.CharField(max_length=255, null=True, blank=True)
    ESTADO = models.CharField(max_length=255, null=True, blank=True)
    LATITUD = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    LONGITUD = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    ID_NODO = models.IntegerField(null=True, blank=True)
    TIPO_CONEXI = models.CharField(max_length=255, null=True, blank=True)
    TIPO_SUBEST = models.CharField(max_length=255, null=True, blank=True)
    OBSERVACION = models.TextField(null=True, blank=True)
    NOMBRE_PROP = models.CharField(max_length=255, null=True, blank=True)
    GRUPO_CONEX = models.CharField(max_length=255, null=True, blank=True)
    CANTIDAD_TR = models.IntegerField(null=True, blank=True)
    UBICACION = models.CharField(max_length=255, null=True, blank=True)
    TIPO_VIA = models.CharField(max_length=255, null=True, blank=True)
    NOMBRE_VIA = models.CharField(max_length=255, null=True, blank=True)
    MANZANA = models.CharField(max_length=255, null=True, blank=True)
    LOTE = models.CharField(max_length=255, null=True, blank=True)
    DISTRITO = models.CharField(max_length=255, null=True, blank=True)
    PROVINCIA = models.CharField(max_length=255, null=True, blank=True)
    DEPARTAMENT = models.CharField(max_length=255, null=True, blank=True)
    CODIGO_UBIG = models.CharField(max_length=255, null=True, blank=True)
    ALTURA = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    FACTOR_UTIL = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    OPERATIVO = models.CharField(max_length=255, null=True, blank=True)
    ELECTRIFICA = models.CharField(max_length=255, null=True, blank=True)
    SISTEMA_ELE = models.CharField(max_length=255, null=True, blank=True)
    SECTOR_TIPI = models.CharField(max_length=255, null=True, blank=True)


    class Meta:
        unique_together = ('CODIGO', 'ID_SALIDAMT')  # Esto garantizará que no se repitan registros
        
    def __str__(self):
        return str(self.CODIGO)

class Seccionador(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=255, blank=True, null=True)
    amt = models.CharField(max_length=255, blank=True, null=True)
    id_vano_mt = models.IntegerField(blank=True, null=True)
    id_subestacion = models.IntegerField(blank=True, null=True)
    tension_nominal = models.CharField(max_length=255, blank=True, null=True)
    codigo_vnr = models.CharField(max_length=255, blank=True, null=True)
    tipo_instalacion = models.CharField(max_length=255, blank=True, null=True)
    propiedad = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=255, blank=True, null=True)
    latitud = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitud = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    funcion = models.CharField(max_length=255, blank=True, null=True)
    abierto = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.CharField(max_length=255, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    operativo = models.CharField(max_length=255, blank=True, null=True)
    corriente_nominal = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    nombre_propietario = models.CharField(max_length=255, blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)
    altura = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    marca = models.CharField(max_length=255, blank=True, null=True)
    serie = models.CharField(max_length=255, blank=True, null=True)
    norma = models.CharField(max_length=255, blank=True, null=True)
    icc = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    bill = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    corriente = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    aislante = models.CharField(max_length=255, blank=True, null=True)
    maniobra = models.CharField(max_length=255, blank=True, null=True)
    id_nodo = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return str(self.codigo)
    
    
class KMLFile(models.Model):
    file = models.FileField(upload_to='kml/')
    upload_date = models.DateTimeField(auto_now_add=True)