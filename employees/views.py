from django.shortcuts import render
from .models import Employee

def employee(request):
    employees = Employee.objects.all()
    context = {
        "employees": employees
    }
    return render(request, "employee.html", context)