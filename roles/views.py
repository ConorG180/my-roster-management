"""Workshift view"""
from django.shortcuts import render, redirect, get_object_or_404
from .models import Role
from .forms import RoleForm


def role_table(request):
    """Function for employee table view"""

    roles = Role.objects.all().order_by("role_id")
    fields = [field for field in Role._meta.fields]
    role_list = roles.values_list()
    role_value_indexes = range(len(fields))
    hidden_fields = ['hourly_wage']

    def role_value_finder():

        """Loops through list of roles and then grabs each value from
        role by looping again (A nested loop) through the role.
        The nested loop will always be equal to the number of values of
        the role, as the nested loop is defined as the length of the
        fields.
        """

        all_role_values = []
        for role in role_list:
            for index in role_value_indexes:
                all_role_values.append(role[index])
        return all_role_values

    def get_hidden_values():
        hidden_columns = ["hourly_wage"]
        hidden_values_list = []
        for hidden_column in hidden_columns:
            hidden_values = Role.objects.values(hidden_column)
            for hidden_value in hidden_values:
                hidden_values_list.append(
                    hidden_value[hidden_column]
                )

        return hidden_values_list

    context = {
        "fields": fields,
        "all_role_values": role_value_finder(),
        "num_of_roles": list(range(roles.count())),
        "col_num": len(fields),
        "table_name": "Roles",
        "table_item_name": "Role",
        "hidden_fields": hidden_fields,
        "hidden_values_list": get_hidden_values()
    }
    return render(request, "role-table.html", context)


def add_role(request):
    """Add record to table """

    # Make sure user is authorised to add records
    if request.user.is_staff is False:
        context = {
            "action": "add new roles"
        }
        return render(request, "account/signup_closed.html", context)

    if request.method == "POST":
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("role_table")

        # Rerender page if information not correct and display errors
        else:
            context = {
                "form": form,
                "table_item_name": "Employee",
                }
            return render(request, "add-employee.html", context)

    form = RoleForm()
    context = {
        "table_item_name": "Role",
        "form": form
    }
    return render(request, "add-role.html", context)


def edit_role(request, role_id):
    """Edit record in table """

    # Make sure user is authorised to edit records
    if request.user.is_staff is False:
        context = {
            "action": "edit roles"
        }
        return render(request, "account/signup_closed.html", context)

    role = get_object_or_404(Role, role_id=role_id)
    if request.method == "POST":
        form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            return redirect("role_table")

        # Rerender page if information not correct and display errors
        else:
            context = {
                    "form": form,
                    "table_item_name": "Role",
                }
            return render(request, "edit-role.html", context)

    form = RoleForm(instance=role)
    context = {
        "form": form,
        "table_item_name": "Role"
    }
    return render(request, "edit-role.html", context)


def delete_role(request, role_id):
    """Delete record in table """

    if request.user.is_staff is False:
        context = {
            "action": "delete roles"
        }
        return render(request, "account/signup_closed.html", context)

    role = get_object_or_404(Role, role_id=role_id)
    role.delete()
    return redirect("role_table")
