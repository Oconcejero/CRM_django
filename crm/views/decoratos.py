from django.shortcuts import redirect
from crm.models import Commercial


def commercial_required(view_func):

    def wrapper(request, *args, **kwargs):
        
        if not request.user.is_authenticated:
            return redirect("commercial_login")
        try:
            request.commercial = Commercial.objects.get(user=request.user)
        except Commercial.DoesNotExist:
            return redirect("commercial_login")

        return view_func(request, *args, **kwargs)
    
    return wrapper

