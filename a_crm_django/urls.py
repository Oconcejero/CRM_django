from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from crm.views.login import commercial_login

from a_crm_django.views import home_view, contact_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', commercial_login, name='commercial_login'),
    path('home/', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('',include('crm.urls')),



    # path('contact/', contact_view, name='contact'),
    # path('client/', client_view, name='client'),
    # path('company/', company_view, name='company'),
    # path('users/', users_view, name='users'),
]
