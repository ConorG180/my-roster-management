from django.contrib import admin
from .models import Workshift
# Register your models here.


class WorkshiftAdmin(admin.ModelAdmin):
    list_display = ("employee_id", "role_id", "start_time", "end_time")
    list_filter = ("employee_id", "role_id", "start_time", "created_on")
    search_fields = ("employee_id", "role_id",)

admin.site.register(Workshift, WorkshiftAdmin)