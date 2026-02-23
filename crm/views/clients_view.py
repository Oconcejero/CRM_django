from django.shortcuts import render, get_object_or_404, redirect
from crm.models import Client, Commercial
from crm.views.decoratos import commercial_required


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


@commercial_required
def client_view(request):
    all_clients = Client.objects.all()
    return render(request, 'client/client.html', {"clients": all_clients})
