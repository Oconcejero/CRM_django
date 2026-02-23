from django.db import models
from .client_model import Client


class Interaction(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='interactions')
    date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Interaction with {self.client.first_name} on {self.date.strftime('%Y-%m-%d %H:%M')}"
