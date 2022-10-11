from django.shortcuts import render
from .models import Workshift

def workshift(request):

    workshifts = Workshift.objects.all().order_by("workshift_id")
    fields = [field for field in Workshift._meta.fields]
    workshift_list = workshifts.values_list()
    workshift_value_indexes = range(len(fields))

    def workshift_value_finder():
        all_workshift_values = []
        for workshift in workshift_list:
            for index in workshift_value_indexes:
                all_workshift_values.append(workshift[index])
        return all_workshift_values

    context = {
        "fields": fields,
        "all_workshift_values": workshift_value_finder(),
        "num_of_workshifts": list(range(workshifts.count())),
        "col_num": len(fields),
        "table_name": "Workshifts",
        "table_item_name": "Workshift"
    }
    return render(request, "workshift.html", context)


def add_workshift(request):
    return render(request, "add-workshift.html", context)


def edit_workshift(request, employee_id):
    return render(request, "edit-workshift.html", context)


def delete_workshift(request, workshift_id):
    return redirect("workshift")