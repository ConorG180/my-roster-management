from django.shortcuts import render
from .models import Workshift

def workshift(request):
    workshifts = Workshift.objects.all()
    context = {
        "workshifts": workshifts
    }
    return render(request, "workshift.html", context)