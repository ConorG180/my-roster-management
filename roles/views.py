from django.shortcuts import render, redirect
from .models import Role
from .forms import Role_form


def role(request):
    roles = Role.objects.all()
    fields = [field for field in Role._meta.fields]
    role_list = roles.values_list()
    role_value_indexes = range(len(fields))

    def role_value_finder():
        all_role_values = []
        for role in role_list:
            for index in role_value_indexes:
                print(role[index])
                all_role_values.append(role[index])
        return all_role_values

    context = {
        "fields": fields,
        "all_role_values": role_value_finder(),
        "num_of_roles": list(range(roles.count())),
        "col_num": len(fields),
        "table_name": "Roles",
        "table_item_name": "Role"
    }
    return render(request, "role-table.html", context)


def add_role(request):
    if request.method == "POST":
        form = Role_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("role_table")
    form = Role_form()
    context = {
        "form": form
    }
    return render(request, "add-role.html", context)