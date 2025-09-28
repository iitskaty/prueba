from django.shortcuts import render, get_object_or_404, redirect
from .models import Registro
from .forms import RegistroForm

def lista_visitas(request):
    visitas = Registro.objects.all()
    return render(request, 'visitas/listado.html', {'visitas': visitas})

def detalle_visita(request, id):
    visita = get_object_or_404(Registro, id=id)
    return render(request, 'visitas/detalle.html', {'visita': visita})

def nueva_visita(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_visitas')
    else:
        form = RegistroForm()
    return render(request, 'visitas/nuevo.html', {'form': form})

def editar_visita(request, id):
    visita = get_object_or_404(Registro, id=id)
    if request.method == 'POST':
        form = RegistroForm(request.POST, instance=visita)
        if form.is_valid():
            form.save()
            return redirect('lista_visitas')
    else:
        form = RegistroForm(instance=visita)
    return render(request, 'visitas/editar.html', {'form': form})

def eliminar_visita(request, id):
    visita = get_object_or_404(Registro, id=id)
    if request.method == 'POST':
        visita.delete()
        return redirect('lista_visitas')
    return render(request, 'visitas/eliminar_registro.html', {'visita': visita})