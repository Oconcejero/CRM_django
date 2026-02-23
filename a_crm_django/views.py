from django.shortcuts import render, redirect
from crm.views.decoratos import commercial_required
from crm.models import Client, Prospect, Opportunity, Commercial
from datetime import datetime
from django.db.models import Sum, Count
from django.db.models.functions import ExtractMonth
from crm.forms.forms import OpportunityForm,ClientForm
from crm.models.task_model import Task
from crm.models.event_model import Event
from crm.models.activity_log_model import ActivityLog
from django.http import JsonResponse
from django.utils import timezone


@commercial_required
def add_opportunity_view(request):
    if request.method == "POST":
        form = OpportunityForm(request.POST)
        if form.is_valid():
            oportunidad = form.save(commit=False)
            oportunidad.comercial = request.user  # asignar comercial automáticamente
            oportunidad.save()
            return redirect('home')  # vuelve al dashboard
    else:
        form = OpportunityForm()

    return render(request, "general/add_opportunity.html", {"form": form})

@commercial_required
def pipeline_view(request):
    comercial = request.user


    oportunidades = Opportunity.objects.filter(comercial=comercial)

    columnas = {
        "Abierta": oportunidades.filter(estado="Abierta"),
        "En curso": oportunidades.filter(estado="En curso"),
        "Propuesta": oportunidades.filter(estado="Propuesta"),
        "Ganada": oportunidades.filter(estado="Ganada"),
        "Perdida": oportunidades.filter(estado="Perdida"),
    }

    return render(request, "general/pipeline.html", {"columnas": columnas})

#ENDPOINT
@commercial_required
def update_opportunity_state(request, pk):

    if request.method == "POST":
        nuevo_estado = request.POST.get("estado")

        # Cargar la oportunidad del comercial actual
        oportunidad = Opportunity.objects.get(pk=pk, comercial=request.user)

        # Actualizar estado
        oportunidad.estado = nuevo_estado

        # Si pasa a GANADA, registrar fecha de cierre si no existe
        if nuevo_estado == "Ganada" and not oportunidad.fecha_cierre:
            oportunidad.fecha_cierre = timezone.now()

        # Si pasa a PERDIDA, también puedes registrar fecha de cierre si quieres
        if nuevo_estado == "Perdida" and not oportunidad.fecha_cierre:
            oportunidad.fecha_cierre = timezone.now()

        oportunidad.save()

        return JsonResponse({"ok": True})



#VISTAS GENERALES
@commercial_required
def home_view(request):
    ano_actual = datetime.now().year
    mes_actual = datetime.now().month

    comercial = request.commercial
    user = request.user

    abiertas = Opportunity.objects.filter(estado="Abierta", comercial=user).aggregate(total=Sum("valor"))["total"] or 0
    en_curso = Opportunity.objects.filter(estado="En curso", comercial=user).aggregate(total=Sum("valor"))["total"] or 0
    propuesta = Opportunity.objects.filter(estado="Propuesta", comercial=user).aggregate(total=Sum("valor"))["total"] or 0
    ganadas = Opportunity.objects.filter(estado="Ganada", comercial=user).aggregate(total=Sum("valor"))["total"] or 0
    perdidas = Opportunity.objects.filter(estado="Perdida", comercial=user).aggregate(total=Sum("valor"))["total"] or 0

    pipeline_total = abiertas + en_curso + propuesta



    origen_qs = (
        Client.objects
        .filter(comercial=comercial)
        .values("origen")
        .annotate(total=Count("id"))
    )

    ORIGEN_MAP = {
        "organico":"Orgánico",
        "adds":"Adds",
        "contacto":"Contacto",
    }

    origen_labels = []
    origen_data = []

    for item in origen_qs:
        clave = item["origen"]
        origen_labels.append(ORIGEN_MAP.get(clave,clave))
        origen_data.append(item["total"])

    

    ventas_mes = (
        Opportunity.objects.filter(
            estado='Ganada',
            fecha_cierre__year=ano_actual,
            comercial=request.user
        )
        .annotate(mes=ExtractMonth('fecha_cierre'))
        .values('mes')
        .annotate(total=Sum('valor'))
        .order_by('mes')
    )

    meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
    
    ventas = [0] * 12
    for venta in ventas_mes:
        ventas[venta['mes'] - 1] = float(venta['total'])

    ventas_mes_actual = ventas[mes_actual - 1]

    cartera_abierta = (
        Opportunity.objects.filter(
            estado='Abierta',
            comercial=request.user
        ).aggregate(total=Sum('valor'))['total'] or 0
    )

    tareas = Task.objects.filter(comercial=comercial, completed=False).order_by('due_date', 'due_time')[:5]
    agenda = Event.objects.filter(comercial=comercial).order_by('date', 'time')[:5]
    actividad = ActivityLog.objects.filter(comercial=comercial).order_by('-created_at')[:5]


    return render(request, "general/home.html", {
        "abiertas":abiertas,
        "en_curso": en_curso,
        "propuesta": propuesta,
        "ganadas":ganadas,
        "perdidas":perdidas,
        "pipeline_total":pipeline_total,
        "total_clientes": Client.objects.filter(comercial=comercial).count(),
        "total_prospectos": Prospect.objects.filter(comercial=request.user).count(),
        "total_oportunidades": Opportunity.objects.filter(comercial=request.user).count(),
        "ventas_mes": ventas_mes_actual,
        "cartera_abierta": cartera_abierta,
        "meses": meses,
        "ventas": ventas,
        "origen_labels": origen_labels,
        "origen_data": origen_data,
        "tareas": tareas,
        "agenda": agenda,
        "actividad": actividad
    })



@commercial_required
def contact_view(request):
    return render(request, 'general/contact.html')

@commercial_required
def add_client(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.comercial = request.commercial
            client.save()
            return redirect("home")
    else:
        form = ClientForm()

    return render(request, "client/add_client.html", {"form": form})
