from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from crm.models import Commercial

def commercial_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(request, "general/commercial_login.html", {
                "error": "Credenciales incorrectas"
            })

        user = authenticate(request, username=user_obj.username, password=password)

        if user is None:
            return render(request, "general/commercial_login.html", {
                "error": "Credenciales incorrectas"
            })

        try:
            commercial = Commercial.objects.get(user=user)
        except Commercial.DoesNotExist:
            return render(request, "general/commercial_login.html", {
                "error": "Este usuario no está registrado como comercial"
            })

        login(request, user)
        request.session["commercial_id"] = commercial.id

        return redirect("home")

    return render(request, "general/commercial_login.html")
