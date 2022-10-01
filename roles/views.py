from django.shortcuts import render
from .models import Role

def role(request):
    roles = Role.objects.all()
    context = {
        "roles": roles
    }
    return render(request, "role-table.html", context)