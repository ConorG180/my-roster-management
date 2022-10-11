from django import forms
from .models import Employee


class Employee_form(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["employee_id", "first_name", "last_name", "date_of_birth", "gender", "role", "pps_number", "phone_number", "email", "start_date"]