from django.shortcuts import render, redirect
from .forms import PacienteForm, ReservacionForm
from .models import Paciente, Reservacion
from django.core.exceptions import ObjectDoesNotExist


def Paciente(request):
    return render(request, 'paciente.html')  

# Create your views here.
def crearPaciente(request):
    if request.method == 'POST':
        paciente_form = PacienteForm(request.POST)
        if paciente_form.is_valid():
            paciente_form.save()
            return redirect('paciente')
    else:
        paciente_form = PacienteForm()
    return render(request,'paciente/crear_paciente.html',{'paciente_form':paciente_form}) 

def editarPaciente(request, rut):
    paciente_form = None
    error = None
    try:
        paciente = Paciente.objects.get(rut = rut)
        if request.method == 'GET':
            paciente_form = PacienteForm(instance = paciente)
        else:
            paciente_form = PacienteForm(request.POST, instance = paciente)

            if paciente_form.is_valid():
                paciente_form.save()
            return redirect('paciente')
              
    except ObjectDoesNotExist as e:
        error = e   

    return render(request,'paciente/crear_paciente.html',{'paciente_form':paciente_form,'error':error})      


def crearReservacion(request):
    if request.method == 'POST':
        reservacion_form = ReservacionForm(request.POST)
        if reservacion_form.is_valid():
            reservacion_form.save()
            return redirect('paciente')
    else:
        reservacion_form = ReservacionForm()
    return render(request,'paciente/crear_reservacion.html',{'reservacion_form':reservacion_form})  





def editarReservacion(request, id):
    reservacion_form = None
    error = None
    try:
        reservacion = Reservacion.objects.get(id = id)
        if request.method == 'GET':
            reservacion_form = ReservacionForm(instance = reservacion)
        else:
            reservacion_form = ReservacionForm(request.POST, instance = reservacion)

            if reservacion_form.is_valid():
                reservacion_form.save()
            return redirect('paciente')
              
    except ObjectDoesNotExist as e:
        error = e   

    return render(request,'paciente/crear_reservacion.html',{'reservacion_form':reservacion_form,'error':error})  


def listarReservacion(request):
    reservaciones = Reservacion.objects.filter(estado = True)   
    return render(request,'paciente/listar_reservacion.html',{'reservaciones':reservaciones})



def eliminarReservacion(request, id):
    reservacion = Reservacion.objects.get(id = id)
    if request.method =='POST':
        reservacion.estado = False
        reservacion.save()
        return redirect('paciente:listar_reservacion')
    return render (request, 'paciente/eliminar_reservacion.html',{'reservacion':reservacion})