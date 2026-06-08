from django.urls import path
from .views.clients_view import (
    client_view, assign_client_view, unassign_client_view, 
    reassign_client_view, client_edit_view, client_delete_view
)
from .views.company_view import company_view
from .views.commercial_view import commercial_view
from .views.interactions_view import (
    interactions_view, interaction_add_view, 
    interaction_edit_view, interaction_delete_view
)
from .views.logout import commercial_logout
from .views.login import commercial_login
from a_crm_django.views import add_opportunity_view, home_view, pipeline_view, update_opportunity_state, add_client
from crm.views.task import add_task_view


urlpatterns = [
    # --- RUTAS DE CLIENTES ---
    path('client/', client_view, name='client'),
    path('clientes/nuevo/', add_client, name='add_client'),
    path('client/edit/<int:client_id>/', client_edit_view, name='client_edit'),
    path('client/delete/<int:client_id>/', client_delete_view, name='client_delete'),
    path('client/assign/<int:client_id>/', assign_client_view, name='assign_client'),
    path('client/unassign/<int:client_id>/', unassign_client_view, name='unassign_client'),
    path('client/reassign/<int:client_id>/', reassign_client_view, name='reassign_client'),

    # --- RUTAS DE INTERACCIONES ---
    path('interactions/', interactions_view, name='interactions'),
    path('interactions/add/', interaction_add_view, name='interaction_add'),
    path('interactions/edit/<int:pk>/', interaction_edit_view, name='interaction_edit'),
    path('interactions/delete/<int:pk>/', interaction_delete_view, name='interaction_delete'),

    # --- OTRAS RUTAS ---
    path('company/', company_view, name='company'),
    path('commercial/', commercial_view, name='commercial'),
    path('logout/', commercial_logout, name='commercial_logout'),
    path('oportunidad/nueva/', add_opportunity_view, name='add_opportunity'),
    path('', home_view, name='home'),
    path('task/add/', add_task_view, name='add_task'),
    path('pipeline/', pipeline_view, name='pipeline'),
    path('update-opportunity-state/<int:pk>/', update_opportunity_state, name='update_opportunity_state'),
]
