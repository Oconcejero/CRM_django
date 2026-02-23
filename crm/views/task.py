from django.shortcuts import render, redirect
from crm.models import Task, ActivityLog, Commercial
from crm.forms.forms import TaskForm
from crm.views.decoratos import commercial_required

@commercial_required
def add_task_view(request):
    comercial = Commercial.objects.get(user=request.user)

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.comercial = comercial
            task.save()

            ActivityLog.objects.create(
                comercial=comercial,
                message=f"Tarea creada: {task.title}"
            )

            return redirect("home")

    else:
        form = TaskForm()

    return render(request, "general/add_task.html", {"form": form})


