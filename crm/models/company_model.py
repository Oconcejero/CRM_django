from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(
        'Name',
        max_length=100
    )
    address = models.CharField(
        'Direction',
        max_length=200, blank=True
    )
    phone = models.CharField(
        'Phone',
        max_length=20, blank=True
    )

    def __str__(self):
        return self.name