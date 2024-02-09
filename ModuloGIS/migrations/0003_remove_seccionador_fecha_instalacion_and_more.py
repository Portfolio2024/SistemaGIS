# Generated by Django 4.2.6 on 2023-10-18 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModuloGIS', '0002_seccionador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seccionador',
            name='fecha_instalacion',
        ),
        migrations.RemoveField(
            model_name='seccionador',
            name='fecha_retiro',
        ),
        migrations.RemoveField(
            model_name='seccionador',
            name='fecha_servicio',
        ),
        migrations.RemoveField(
            model_name='seccionador',
            name='systime',
        ),
        migrations.AlterField(
            model_name='seccionador',
            name='abierto',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='seccionador',
            name='aislante',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='seccionador',
            name='altura',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='seccionador',
            name='bill',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='seccionador',
            name='cantidad',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='seccionador',
            name='codigo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='seccionador',
            name='codigo_vnr',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='seccionador',
            name='corriente',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='seccionador',
            name='corriente_nominal',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='seccionador',
            name='estado',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='seccionador',
            name='funcion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='seccionador',
            name='icc',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='seccionador',
            name='id_nodo',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='seccionador',
            name='id_subestacion',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='seccionador',
            name='id_vano_mt',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='seccionador',
            name='latitud',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='seccionador',
            name='longitud',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='seccionador',
            name='maniobra',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='seccionador',
            name='marca',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='seccionador',
            name='nombre_propietario',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='seccionador',
            name='norma',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='seccionador',
            name='observacion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='seccionador',
            name='operativo',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='seccionador',
            name='propiedad',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='seccionador',
            name='serie',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='seccionador',
            name='tension_nominal',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='seccionador',
            name='tipo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='seccionador',
            name='tipo_instalacion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
