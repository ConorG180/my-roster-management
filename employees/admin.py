"""Admin panel for employees app"""
from django.contrib import admin
from .models import Employee

admin.site.site_header = "MyRosterManagement Dashboard"


class EmployeeAdmin(admin.ModelAdmin):
    """Class for customising employees admin view."""
    list_display = ("employee_id", "first_name",
                    "last_name", "role", "phone_number")
    list_filter = ("first_name", "last_name", "role",)
    search_fields = ("first_name", "last_name", "role",)


admin.site.register(Employee, EmployeeAdmin)
