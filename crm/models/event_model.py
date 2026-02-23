from django.db import models
from .commercials_model import Commercial

class Event(models.Model):
    comercial = models.ForeignKey(Commercial, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.title
