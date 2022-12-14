"""Admin panel for workshifts app"""
from django.contrib import admin
from .models import Workshift


class WorkshiftAdmin(admin.ModelAdmin):
    """Class for customising workshifts admin view."""
    list_display = (
        "employee_id", "role_id",
        "start_time", "end_time"
    )
    list_filter = (
        "employee_id", "role_id",
        "start_time", "created_on"
    )
    search_fields = ("employee_id", "role_id",)


admin.site.register(Workshift, WorkshiftAdmin)
