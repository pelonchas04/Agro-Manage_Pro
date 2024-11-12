# Generated by Django 5.0.7 on 2024-10-24 20:52

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=15, verbose_name='Nombre de empresa')),
                ('hability', models.BooleanField(default=True, verbose_name='Habilitado')),
                ('usernameextension', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(5)], verbose_name='Extension de empresa')),
                ('address', models.CharField(max_length=25, validators=[django.core.validators.MinLengthValidator(6)], verbose_name='Direccion')),
                ('nit', models.CharField(max_length=12, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='NIT')),
                ('owner', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(8)], verbose_name='Propietario')),
                ('tel', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefono')),
                ('observations', models.CharField(blank=True, max_length=100, null=True, verbose_name='Observaciones')),
                ('department', models.CharField(blank=True, max_length=25, null=True, verbose_name='Departamento')),
                ('state', models.CharField(blank=True, max_length=25, null=True, verbose_name='Municipio')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='UserAsigned',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Asignacion',
                'verbose_name_plural': 'Asignaciones',
            },
        ),
    ]