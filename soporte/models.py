from django.db import models


class Reparacion(models.Model):

    ESTADOS = [
        ('ESPERA', 'En espera'),
        ('REPARANDO', 'En reparación'),
        ('FINALIZADO', 'Finalizado'),
        ('ENTREGADO', 'Entregado'),
    ]

    tecnico = models.CharField(max_length=100)
    diagnostico = models.TextField(blank=True)
    fecha_entrega = models.DateField(null=True, blank=True)
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='ESPERA'
    )
    solucion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.tecnico} - {self.estado}"