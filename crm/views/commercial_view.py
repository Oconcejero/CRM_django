from django.shortcuts import render
from crm.models import Commercial

# VISTAS MODELOS


def commercial_view(request):
    all_commercials = Commercial.objects.all()
    context = {
        'commercials': all_commercials
    }
    return render(request, 'commercial/commercial.html',context)
