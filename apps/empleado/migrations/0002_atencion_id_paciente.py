# Generated by Django 2.2 on 2019-04-23 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empleado', '0001_initial'),
        ('paciente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='atencion',
            name='id_paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paciente.Paciente'),
        ),
    ]
