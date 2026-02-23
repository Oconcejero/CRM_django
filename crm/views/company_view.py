from django.shortcuts import render
from crm.models import Company
from crm.views.decoratos import commercial_required

# VISTAS MODELOS

@commercial_required
def company_view(request):
    all_companys = Company.objects.all()
    context = {
        'companys': all_companys
    }
    return render(request, 'company/company.html', context)

