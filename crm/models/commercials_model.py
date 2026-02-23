
# VISTAS MODELOS
from django.db import models
from django.contrib.auth.models import User


class Commercial(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username
