from django.db import models
from django.contrib.auth.models import User

class Opportunity(models.Model):
    nombre = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_cierre = models.DateTimeField(null=True, blank=True)
    comercial = models.ForeignKey(User, on_delete=models.CASCADE)

    ESTADOS_OPORTUNIDAD = [
        ('Abierta', 'Abierta'),
        ('En curso','En curso'),
        ('Propuesta','Propuesta'),
        ('Ganada','Ganada'),
        ('Perdida', 'Perdida'),
    ]

    estado = models.CharField(
        max_length=50,
        choices=ESTADOS_OPORTUNIDAD,
        default='Abierta'
    )

    def __str__(self):
        return self.nombre
