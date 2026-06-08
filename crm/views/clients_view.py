from django.shortcuts import render, get_object_or_404, redirect
from crm.models import Client, Commercial
from crm.views.decoratos import commercial_required
from crm.forms.forms import ClientForm


def assign_client_view(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    comercial = Commercial.objects.get(user=request.user)
    client.comercial = comercial
    client.save()
    return redirect("client")


def unassign_client_view(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    client.comercial = None
    client.save()
    return redirect("client")


def reassign_client_view(request, client_id):
    client = get_object_or_404(Client, id=client_id)

    if request.method == "POST":
        new_commercial_id = request.POST.get("comercial")
        
        client.comercial = Commercial.objects.get(id=new_commercial_id)
        client.save()
        return redirect("client")

    comerciales = Commercial.objects.all()

    return render(request, "general/reassign_client.html", {
        "client": client,
        "comerciales": comerciales
    })

def client_edit_view(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client')
    else:
        # Inicializamos el form con el nombre de la empresa para que no salga vacío
        initial_data = {'company_name': client.company.name if client.company else ''}
        form = ClientForm(instance=client, initial=initial_data)
        
    return render(request, "client/add_client.html", {"form": form, "edit_mode": True})

def client_delete_view(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == "POST":
        client.delete()
        return redirect('client')
    # Usamos un template sencillo de confirmación
    return render(request, "general/delete_confirm.html", {"obj": client, "cancel_url": "client"})


@commercial_required
def client_view(request):
    all_clients = Client.objects.all()
    return render(request, 'client/client.html', {"clients": all_clients})
