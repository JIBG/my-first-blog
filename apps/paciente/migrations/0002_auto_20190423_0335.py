# Generated by Django 2.2 on 2019-04-23 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservacion',
            name='id_servicio',
            field=models.CharField(max_length=100, verbose_name='Servicio :'),
        ),
    ]