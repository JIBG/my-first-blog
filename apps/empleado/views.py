from django.shortcuts import render, redirect
from .forms import ProductoForm, AtencionForm
from .models import Producto, Atencion
from apps.paciente.models import Paciente
from apps.odontologia.models import Dentista
from apps.administrador.models import Empleado
from django.core.exceptions import ObjectDoesNotExist

def Empleado(request):
    return render(request, 'empleado.html')  

# Create your views here.


def editarEmpleado(request, rut):
    empleado_form = None
    error = None
    try:
        empleado = Empleado.objects.get(rut = rut)
        if request.method == 'GET':
            empleado_form = EmpleadoForm(instance = empleado)
        else:
            empleado_form = EmpleadoForm(request.POST, instance = empleado)

            if empleado_form.is_valid():
                empleado_form.save()
            return redirect('empleado')
              
    except ObjectDoesNotExist as e:
        error = e   

    return render(request,'administrador/crear_empleado.html',{'empleado_form':empleado_form,'error':error})


def crearProducto(request):
    if request.method == 'POST':
        producto_form = ProductoForm(request.POST)
        if producto_form.is_valid():
            producto_form.save()
            return redirect('empleado')
    else:
        producto_form = ProductoForm()
    return render(request,'empleado/crear_producto.html',{'producto_form':producto_form})  





def editarProducto(request, id):
    producto_form = None
    error = None
    try:
        producto = Producto.objects.get(id = id)
        if request.method == 'GET':
            producto_form = ProductoForm(instance = producto)
        else:
            producto_form = ProductoForm(request.POST, instance = producto)

            if producto_form.is_valid():
                producto_form.save()
            return redirect('empleado')
              
    except ObjectDoesNotExist as e:
        error = e   

    return render(request,'empleado/crear_producto.html',{'producto_form':producto_form,'error':error})  


def listarProducto(request):
    productos = Producto.objects.filter(estado = True)   
    return render(request,'empleado/listar_producto.html',{'productos':productos})



def eliminarProducto(request, id):
    producto = Producto.objects.get(id = id)
    if request.method =='POST':
        producto.estado = False
        producto.save()
        return redirect('empleado:listar_producto')
    return render (request, 'empleado/eliminar_producto.html',{'producto':producto})


def crearAtencion(request):
    if request.method == 'POST':
        atencion_form = AtencionForm(request.POST)
        if atencion_form.is_valid():
            atencion_form.save()
            return redirect('empleado')
    else:
        atencion_form = AtencionForm()
    return render(request,'empleado/crear_atencion.html',{'atencion_form':atencion_form})  


def listarAtencion(request):
    atenciones = Atencion.objects.filter(estado = True)   
    return render(request,'empleado/listar_atencion.html',{'atenciones':atenciones})



def eliminarAtencion(request, id):
    atencion = Atencion.objects.get(id = id)
    if request.method =='POST':
        atencion.estado = False
        atencion.save()
        return redirect('empleado:listar_atencion')
    return render (request, 'empleado/eliminar_atencion.html',{'atencion':atencion})
