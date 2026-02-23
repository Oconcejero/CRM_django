from django.db import models
from .commercials_model import Commercial

class ActivityLog(models.Model):
    comercial = models.ForeignKey(Commercial, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
