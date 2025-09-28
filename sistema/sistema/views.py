from django.shortcuts import render, get_object_or_404, redirect
from .models import sistema
from .forms import sistemaForm

def lista_visitas(request):
    visitas = sistema.objects.all()
    return render(request, 'visitas/base.html', {'visitas': visitas})

def detalle_visitas(request, id):
    visita = get_object_or_404(sistema, id=id)
    return render(request, 'visitas/detalle_visitas.html', {'visita': visita})

def nueva_visita(request):
    if request.method == 'POST':
        form = sistemaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_visitas')
    else:
        form = sistemaForm()
    return render(request, 'visitas/nueva_visitas.html', {'form': form})

def editar_visitas(request, id):
    visita = get_object_or_404(sistema, id=id)
    if request.method == 'POST':
        form = sistemaForm(request.POST, instance=visita)
        if form.is_valid():
            form.save()
            return redirect('lista_visitas')
    else:
        form = sistemaForm(instance=visita)
    return render(request, 'visitas/editar_visitas.html', {'form': form})

def eliminar_visitas(request, id):
    visita = get_object_or_404(sistema, id=id)
    if request.method == 'POST':
        visita.delete()
        return redirect('lista_visitas')
    return render(request, 'visitas/eliminar_visitas.html', {'visita': visita})