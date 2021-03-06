# Generated by Django 2.2 on 2019-04-23 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('rut', models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='Rut :')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre :')),
                ('appaterno', models.CharField(max_length=50, verbose_name='Apellido Paterno :')),
                ('apmaterno', models.CharField(max_length=50, verbose_name='Apellido Materno :')),
                ('fono', models.IntegerField(verbose_name='Telefono :')),
                ('email', models.EmailField(max_length=254, verbose_name='Email :')),
                ('direccion', models.CharField(max_length=100, verbose_name='Dirección :')),
                ('f_contrato', models.DateField(verbose_name='Fecha de Contrato :')),
                ('salario', models.IntegerField(verbose_name='Salario :')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
            },
        ),
        migrations.CreateModel(
            name='TipoCargo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre :')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado :')),
            ],
            options={
                'verbose_name': 'TipoCargo',
                'verbose_name_plural': 'TipoCargos',
            },
        ),
        migrations.CreateModel(
            name='TipoServicio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre :')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado :')),
            ],
            options={
                'verbose_name': 'TipoServicio',
                'verbose_name_plural': 'TipoServicios',
            },
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre :')),
                ('descripcion', models.CharField(max_length=200, verbose_name='Descripción :')),
                ('costo', models.IntegerField(verbose_name='Costo :')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('id_empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrador.Empleado')),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
            },
        ),
    ]
