from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Employee
from .forms import Employeeform


def employee(request):

    employees = Employee.objects.all().order_by("employee_id")
    fields = [field for field in Employee._meta.fields]
    employee_list = employees.values_list()
    employee_value_indexes = range(len(fields))
    hidden_fields = ["date_of_birth", "gender", "pps_number", "phone_number", "email"]

    def employee_value_finder():
        all_employee_values = []
        for employee in employee_list:
            for index in employee_value_indexes:
                all_employee_values.append(employee[index])
        return all_employee_values
    
    def get_hidden_values():
        hidden_columns = hidden_fields
        hidden_values_list = []
        for hidden_column in hidden_columns:
            hidden_values = Employee.objects.values(hidden_column)
            for hidden_value in hidden_values:
                hidden_values_list.append(hidden_value[hidden_column])                
        return hidden_values_list

    context = {
        "fields": fields,
        "all_employee_values": employee_value_finder(),
        "num_of_employees": list(range(employees.count())),
        "col_num": len(fields),
        "table_name": "Employees",
        "table_item_name": "Employee",
        "hidden_fields": hidden_fields,
        "hidden_values_list": get_hidden_values()
    }
    return render(request, "employee.html", context)


def add_employee(request):

    # Make sure user is authorised to add records
    if request.user.is_staff is False:
        context = {
            "action": "add new employees"
        }
        return render(request, "account/signup_closed.html", context)
        
    if request.method == "POST":
        form = Employeeform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("employee")

            # Rerender page if information not correct and display errors
        else:
            context = {
                "form": form,
                "table_item_name": "Employee",
                }
            return render(request, "add-employee.html", context)

    form = Employeeform()
    context = {
        "form": form,
        "table_item_name": "Employee"
    }
    return render(request, "add-employee.html", context)


def edit_employee(request, employee_id):

    # Make sure user is authorised to edit records
    if request.user.is_staff is False:
        context = {
            "action": "edit employees"
        }
        return render(request, "account/signup_closed.html", context)

    employee = get_object_or_404(Employee, employee_id=employee_id)
    if request.method == "POST":
        form = Employeeform(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect("employee")

        # Rerender page if information not correct and display errors
        else:
            context = {
                "form": form,
                "table_item_name": "Employee",
                }
            return render(request, "edit-employee.html", context)

    form = Employeeform(instance=employee)
    context = {
        "form": form,
        "table_item_name": "Employee"
    }
    return render(request, "edit-employee.html", context)


def delete_employee(request, employee_id):
    if request.user.is_staff is False:
        context = {
            "action": "delete employees"
        }
        return render(request, "account/signup_closed.html", context)
        
    employee = get_object_or_404(Employee, employee_id=employee_id)
    employee.delete()
    return redirect("employee")