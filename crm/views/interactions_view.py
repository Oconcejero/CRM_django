from django.shortcuts import render, redirect, get_object_or_404
from crm.models.interaction_model import Interaction
from crm.forms.forms import InteractionForm

def interactions_view(request):
    interactions = Interaction.objects.all().order_by('-date')
    return render(request, 'interactions/list.html', {'interactions': interactions})

def interaction_add_view(request):
    if request.method == 'POST':
        form = InteractionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('interactions')
    else:
        form = InteractionForm()
    return render(request, 'interactions/form.html', {'form': form})

def interaction_edit_view(request, pk):
    interaction = get_object_or_404(Interaction, pk=pk)
    if request.method == 'POST':
        form = InteractionForm(request.POST, instance=interaction)
        if form.is_valid():
            form.save()
            return redirect('interactions')
    else:
        form = InteractionForm(instance=interaction)
    return render(request, 'interactions/form.html', {'form': form})

def interaction_delete_view(request, pk):
    interaction = get_object_or_404(Interaction, pk=pk)
    if request.method == 'POST':
        interaction.delete()
        return redirect('interactions')
    return render(request, "general/delete_confirm.html", {"obj": interaction, "cancel_url": "interactions"})