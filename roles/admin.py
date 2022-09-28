from django.contrib import admin
from .models import Role


class RoleAdmin(admin.ModelAdmin):
    list_display = ("title", "hourly_wage",)
    list_filter = ("title",)
    search_fields = ("title",)

admin.site.register(Role, RoleAdmin)