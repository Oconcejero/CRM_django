from django.db import models
from django.contrib.auth.models import User
from .commercials_model import Commercial
from crm.models.company_model import Company





class Client(models.Model):
    first_name = models.CharField(
        'Name',
        max_length=100
    )
    last_name = models.CharField(
        'Last Name',
        max_length=100
    )
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    company = models.ForeignKey(Company,on_delete=models.SET_NULL, null=True, blank=True)
    comercial = models.ForeignKey(Commercial, on_delete=models.SET_NULL, null=True, blank=True)

    origen = models.CharField(
        max_length=50,
        choices=[
            ('organico', 'Orgánico'),
            ('adds','Adds'),
            ('contacto','Contacto'),
        ],
            blank=False,
            null=False,
    )

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
