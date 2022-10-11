from django.shortcuts import render, redirect
from .models import Employee

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
    return request(request, "workshifts.html")


def edit_employee(request, employee_id):
    return redirect("index")


def delete_employee(request, employee_id):
    return redirect("index")