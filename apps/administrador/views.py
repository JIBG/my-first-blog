from django.shortcuts import render, redirect
from .forms import ServicioForm, EmpleadoForm
from .models import Servicio, Empleado
from apps.paciente.models import Paciente
from django.core.exceptions import ObjectDoesNotExist

def Administrador(request):
    return render(request, 'administrador.html')  


def crearServicio(request):
    if request.method == 'POST':
        servicio_form = ServicioForm(request.POST)
        if servicio_form.is_valid():
            servicio_form.save()
            return redirect('administrador')
    else:
        servicio_form = ServicioForm()
    return render(request,'administrador/crear_servicio.html',{'servicio_form':servicio_form})  





def editarServicio(request, id):
    servicio_form = None
    error = None
    try:
        servicio = Servicio.objects.get(id = id)
        if request.method == 'GET':
            servicio_form = ServicioForm(instance = servicio)
        else:
            servicio_form = ServicioForm(request.POST, instance = servicio)

            if servicio_form.is_valid():
                servicio_form.save()
            return redirect('administrador')
              
    except ObjectDoesNotExist as e:
        error = e   

    return render(request,'administrador/crear_servicio.html',{'servicio_form':servicio_form,'error':error})  


def listarServicio(request):
    servicios = Servicio.objects.filter(estado = True)   
    return render(request,'administrador/listar_servicio.html',{'servicios':servicios})



def eliminarServicio(request, id):
    servicio = Servicio.objects.get(id = id)
    if request.method =='POST':
        servicio.estado = False
        servicio.save()
        return redirect('administrador:listar_servicio')
    return render (request, 'administrador/eliminar_servicio.html',{'servicio':servicio})


def listarPaciente(request):
    pacientes = Paciente.objects.filter(estado = True)   
    return render(request,'administrador/listar_paciente.html',{'pacientes':pacientes})



def eliminarPaciente(request, rut):
    paciente = Paciente.objects.get(rut = rut)
    if request.method =='POST':
        paciente.estado = False
        paciente.save()
        return redirect('administrador:listar_paciente')
    return render (request, 'administrador/eliminar_paciente.html',{'paciente':paciente})


def crearEmpleado(request):
    if request.method == 'POST':
        empleado_form = EmpleadoForm(request.POST)
        if empleado_form.is_valid():
            empleado_form.save()
            return redirect('administrador')
    else:
        empleado_form = EmpleadoForm()
    return render(request,'administrador/crear_empleado.html',{'empleado_form':empleado_form})      


    

def listarEmpleado(request):
    empleados = Empleado.objects.filter(estado = True)   
    return render(request,'administrador/listar_empleado.html',{'empleados':empleados})



def eliminarEmpleado(request, rut):
    empleado = Empleado.objects.get(rut = rut)
    if request.method =='POST':
        empleado.estado = False
        empleado.save()
        return redirect('administrador:listar_empleado')
    return render (request, 'administrador/eliminar_empleado.html',{'empleado':empleado})