from django import forms
from crm.models import Opportunity,Client, Company
from crm.models.task_model import Task
from crm.models.event_model import Event
from django.forms import DateInput, TimeInput, DateTimeInput


class OpportunityForm(forms.ModelForm):
    fecha_cierre = forms.DateTimeField(
        widget=DateTimeInput(attrs={"type": "datetime-local"}),

        required=False
    )

    class Meta:
        model = Opportunity
        fields = ['nombre', 'valor', 'estado', 'fecha_cierre']

    def clean(self):
        cleaned_data = super().clean()
        estado = cleaned_data.get("estado")
        fecha = cleaned_data.get("fecha_cierre")

        if estado == "Ganada" and not fecha:
            raise forms.ValidationError("Debes indicar una fecha de cierre para una oportunidad ganada.")

        return cleaned_data


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'due_date', 'due_time', 'completed']
        labels = {
            "title": "Tarea",
            "due_date": "Fecha límite",
            "due_time": "Hora límite",
            "completed": "Completada"
        }
        widgets = {
            "due_date": DateInput(attrs={"type": "date"}),

            "due_time": TimeInput(attrs={"type": "time"}),
        }


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['title', 'date', 'time']
        widgets = {
            "date": DateInput(attrs={"type": "date"}),
            "time": TimeInput(attrs={"type": "time"}),
        }

class ClientForm(forms.ModelForm):
    company_name = forms.CharField(label="Compañía", required=True)

    class Meta:
        model = Client
        fields = ["first_name", "last_name", "email", "phone", "company_name", "origen", "comercial"]

    def save(self, commit=True):
        from crm.models import Company 

        #NOMBRE DEL USUARIO
        company_name = self.cleaned_data["company_name"].strip()

        #COMPAÑÍA
        company, created = Company.objects.get_or_create(name=company_name)

    
        client = super().save(commit=False)
        client.company = company

        if commit:
            client.save()

        return client
