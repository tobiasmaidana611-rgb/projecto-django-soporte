from django.shortcuts import render, redirect
from .models import Reparacion

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