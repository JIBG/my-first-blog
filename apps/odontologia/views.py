from django.shortcuts import render, redirect
from .forms import DentistaForm, ReservaForm
from .models import Dentista, Reserva
from django.core.exceptions import ObjectDoesNotExist



# Create your views here.
def Home(request):
    return render(request, 'index.html')

def Admin(request):
    return render(request, 'odontologia/administrador.html')    

def crearDentista(request):
    if request.method == 'POST':
        dentista_form = DentistaForm(request.POST)
        if dentista_form.is_valid():
            dentista_form.save()
            return redirect('index')
    else:
        dentista_form = DentistaForm()
    return render(request,'odontologia/crear_dentista.html',{'dentista_form':dentista_form}) 


def crearReserva(request):
    if request.method == 'POST':
        reserva_form = ReservaForm(request.POST)
        if reserva_form.is_valid():
            reserva_form.save()
            return redirect('index')
    else:
        reserva_form = ReservaForm()
    return render(request,'odontologia/crear_reserva.html',{'reserva_form':reserva_form}) 



def listarDentista(request):
    dentistas = Dentista.objects.filter(estado = True)
    return render(request,'odontologia/listar_dentista.html',{'dentistas':dentistas})
        

def editarDentista(request, rut):
    dentista_form = None
    error = None
    try:
        dentista = Dentista.objects.get(rut = rut)
        if request.method == 'GET':
            dentista_form = DentistaForm(instance = dentista)
        else:
            dentista_form = DentistaForm(request.POST, instance = dentista)

            if dentista_form.is_valid():
                dentista_form.save()
            return redirect('index')
              
    except ObjectDoesNotExist as e:
        error = e   

    return render(request,'odontologia/crear_dentista.html',{'dentista_form':dentista_form,'error':error})   

def eliminarDentista(request, rut):
    dentista = Dentista.objects.get(rut = rut)
    if request.method =='POST':
        dentista.estado = False
        dentista.save()
        return redirect('odontologia:listar_dentista')
    return render (request, 'odontologia/eliminar_dentista.html',{'dentista':dentista})    
    