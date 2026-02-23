from django.shortcuts import render

# VISTAS MODELOS


def interactions_view(request):
    return render(request, 'interactions/interactions.html')