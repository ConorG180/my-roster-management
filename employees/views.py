from django.shortcuts import render, redirect
from .models import Employee
from .forms import Employee_form


def employee(request):

    employees = Employee.objects.all().order_by("employee_id")
    fields = [field for field in Employee._meta.fields]
    employee_list = employees.values_list()
    employee_value_indexes = range(len(fields))

    def employee_value_finder():
        all_employee_values = []
        for employee in employee_list:
            for index in employee_value_indexes:
                all_employee_values.append(employee[index])
        return all_employee_values

    context = {
        "fields": fields,
        "all_employee_values": employee_value_finder(),
        "num_of_employees": list(range(employees.count())),
        "col_num": len(fields),
        "table_name": "Employees",
        "table_item_name": "Employee"
    }
    return render(request, "employee.html", context)


def add_employee(request):
    if request.method == "POST":
        form = Employee_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("employee")
    form = Employee_form()
    context = {
        "form": form,
        "table_item_name": "Employee"
    }
    return render(request, "add-employee.html", context)


def edit_employee(request, employee_id):
    return redirect("index")


def delete_employee(request, employee_id):
    return redirect("index")