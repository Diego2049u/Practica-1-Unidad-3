

# Create your views here.
from modelApp.models import Empleado
from django.shortcuts import render, redirect
from . import forms

def index(request):
    form = forms.EmpleadoForm()
    if request.method == 'POST':
        form = forms.EmpleadoForm(request.POST)
        if form.is_valid():
            print("Formulario OK")
            print("Nombre: ", form.cleaned_data['nombre'])
            form.save()
            return listar_empleados(request)
    data = {'form': form}
    return render(request, 'modelApp/index.html', data)

def listar_empleados(request):
    empleados = Empleado.objects.all()
    data = {'empleados': empleados}
    return render(request, 'modelApp/empleados.html', data)

def editar_empleado(request, id):
    empleado = Empleado.objects.get(id=id)
    form = forms.EmpleadoForm(instance=empleado)
    if request.method == 'POST':
        form = forms.EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return listar_empleados(request)
    data = {'form': form}
    return render(request, 'modelApp/index.html', data)

def eliminar_empleado(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()
    return redirect('trabajadores:empleados')
