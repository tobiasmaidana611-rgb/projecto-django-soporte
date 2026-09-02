from django.shortcuts import render, redirect, get_object_or_404
from .models import Reparacion

def inicio(request):
    return render(request, 'soporte/inicio.html') 

def lista_reparaciones(request):
    reparaciones = Reparacion.objects.all().order_by('-id')
    return render(request, 'soporte/lista.html', {
        'reparaciones': reparaciones
    })

def nueva_reparacion(request):
    if request.method == 'POST':
        tecnico = request.POST.get('tecnico')
        diagnostico = request.POST.get('diagnostico')
        estado = request.POST.get('estado')
        fecha_entrega = request.POST.get('fecha_entrega') or None
        solucion = request.POST.get('solucion')

        Reparacion.objects.create(
            tecnico=tecnico,
            diagnostico=diagnostico,
            estado=estado,
            fecha_entrega=fecha_entrega,
            solucion=solucion
        )
        return redirect('lista_reparaciones')

    return render(request, 'soporte/nueva.html')

def editar_reparacion(request, id):
    reparacion = get_object_or_404(Reparacion, id=id)

    if request.method == 'POST':
        reparacion.tecnico = request.POST.get('tecnico')
        reparacion.diagnostico = request.POST.get('diagnostico')
        reparacion.estado = request.POST.get('estado')
        reparacion.fecha_entrega = request.POST.get('fecha_entrega') or None
        reparacion.solucion = request.POST.get('solucion')
        reparacion.save()
        return redirect('lista_reparaciones')

    return render(request, 'soporte/editar.html', {
        'reparacion': reparacion
    })

def eliminar_reparacion(request, id):
    reparacion = get_object_or_404(Reparacion, id=id)

    if request.method == 'POST':
        reparacion.delete()
        return redirect('lista_reparaciones')

    return render(request, 'soporte/eliminar.html', {
        'reparacion': reparacion
    })