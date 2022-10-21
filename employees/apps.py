"""app module for employees app"""
from django.apps import AppConfig


class EmployeesConfig(AppConfig):
    """EmployeesConfig class"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'employees'
