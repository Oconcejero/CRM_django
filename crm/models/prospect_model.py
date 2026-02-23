from django.db import models
from django.contrib.auth.models import User

class Prospect(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    origen = models.CharField(max_length=50)
    comercial = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
