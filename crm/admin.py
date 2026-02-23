from django.contrib import admin
from .models.client_model import Client
from .models.company_model import Company
from .models.commercials_model import Commercial
from .models.task_model import Task
from .models.activity_log_model import ActivityLog
from .models.event_model import Event
from .models.interaction_model import Interaction
from .models import Opportunity

# Register your models here.
admin.site.register(Commercial)
admin.site.register(ActivityLog)
admin.site.register(Event)
admin.site.register(Interaction)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'address',
        'phone',
    )

@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'valor',
        'fecha_creacion',
        'fecha_cierre',
        'comercial',
        'estado',
    )

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
	list_display = (
        'comercial',
        'title',
        'due_date',
        'due_time',
        'completed'
    )


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'email',
        'phone',
        'company'
    )

@admin.register(Interaction)
class InteracionAdmin(admin.ModelAdmin):
    pass
