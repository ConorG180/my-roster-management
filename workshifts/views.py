from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Workshift
from .forms import Workshift_form

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
    if request.user.is_staff is False:
        return HttpResponse('Unauthorized', status=401)
    if request.method == "POST":
        form = Workshift_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("workshift")
    form = Workshift_form()
    context = {
        "form": form,
        "table_item_name": "Workshift"
    }
    return render(request, "add-workshift.html", context)


def edit_workshift(request, workshift_id):
    if request.user.is_staff is False:
        return HttpResponse('Unauthorized', status=401)
    workshift = get_object_or_404(Workshift, workshift_id=workshift_id )
    if request.method == "POST":
        form = Workshift_form(request.POST, instance=workshift)
        if form.is_valid():
            form.save()
            return redirect("workshift")
    form = Workshift_form(instance=workshift)
    context = {
    "form": form,
    "table_item_name": "workshift"
    }
    return render(request, "edit-workshift.html", context)


def delete_workshift(request, workshift_id):
    if request.user.is_staff is False:
        return HttpResponse('Unauthorized', status=401)
    workshift = get_object_or_404(Workshift, workshift_id=workshift_id)
    workshift.delete()
    return redirect("workshift")