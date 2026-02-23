from django.shortcuts import redirect

def commercial_logout(request):
    request.session.pop("commercial_id", None)
    return redirect("commercial_login")
