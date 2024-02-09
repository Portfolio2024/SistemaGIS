# Generated by Django 4.2.7 on 2023-11-15 20:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaTension4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('files', models.FileField(upload_to='MediaTension/%d/%m/%Y')),
                ('creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'MediaTension_PLANOS',
                'verbose_name_plural': 'MediaTensions_PLANOS',
                'db_table': 'MediaTension4',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='MediaTension3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('files', models.FileField(upload_to='MediaTension/%d/%m/%Y')),
                ('creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'MediaTension_METRADO',
                'verbose_name_plural': 'MediaTensions_METRADO',
                'db_table': 'MediaTension3',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='MediaTension2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('files', models.FileField(upload_to='MediaTension/%d/%m/%Y')),
                ('creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'MediaTension_FOTOS',
                'verbose_name_plural': 'MediaTensions_FOTOS',
                'db_table': 'MediaTension2',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='MediaTension1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('files', models.FileField(upload_to='MediaTension/%d/%m/%Y')),
                ('creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'MediaTension_DU',
                'verbose_name_plural': 'MediaTensions_DU',
                'db_table': 'MediaTension1',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='MediaTension',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('files', models.FileField(upload_to='MediaTension/%d/%m/%Y')),
                ('creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'MediaTension',
                'verbose_name_plural': 'MediaTensions',
                'db_table': 'MediaTension',
                'ordering': ['id'],
            },
        ),
    ]
