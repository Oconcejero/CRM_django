from django.db import models
from.commercials_model import Commercial

class Task(models.Model):
    comercial = models.ForeignKey(Commercial, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    due_date = models.DateField()
    due_time = models.TimeField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
