"""Handles all urls in project"""

from django.contrib import admin
from django.urls import path, include
from roles import views as role_views
from home.views import home
from employees import views as employee_views
from workshifts import views as workshift_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("role/", role_views.role_table, name="role_table"),
    path("add-role/", role_views.add_role, name="add_role"),
    path("add-role/add", role_views.add_role, name="add_role"),
    path("edit-role/<role_id>", role_views.edit_role, name="edit_role"),
    path("delete-role/<role_id>", role_views.delete_role, name="delete_role"),
    path("employee/", employee_views.employee_table, name="employee"),
    path("add-employee/add", employee_views.add_employee, name="add_employee"),
    path(
        "edit-employee/<employee_id>",
        employee_views.edit_employee,
        name="edit_employee"
    ),
    path(
        "delete-employee/<employee_id>",
        employee_views.delete_employee,
        name="delete_employee"
    ),
    path("workshift/", workshift_views.workshift_table, name="workshift"),
    path(
        "add-workshift/",
        workshift_views.add_workshift,
        name="add_workshift"
    ),
    path(
        "add-workshift/add",
        workshift_views.add_workshift,
        name="add_workshift"
    ),
    path(
        "edit-workshift/<workshift_id>",
        workshift_views.edit_workshift,
        name="edit_workshift"
    ),
    path(
        "delete-workshift/<workshift_id>",
        workshift_views.delete_workshift,
        name="delete_workshift"
    ),
    path("accounts/", include("allauth.urls"))
    # url - function - namespace: used in hrefs
]
