"""Forms in employee app."""
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import Employee


class DateInput(forms.DateInput):
    """Controls input style of date fields"""
    input_type = "date"


class Employeeform(forms.ModelForm):
    """Customize fields for the employee form"""

    date_of_birth = forms.DateField(widget=DateInput)
    phone_number = PhoneNumberField(widget=forms.TextInput(
        attrs={"placeholder": "e.g. +353872703824"}))
    start_date = forms.DateField(widget=DateInput)
    email = forms.EmailField()

    class Meta:
        """Set fields to appear in employee form"""

        model = Employee
        fields = [
                "employee_id", "first_name", "last_name", "date_of_birth",
                "gender", "role", "pps_number", "phone_number", "email",
                "start_date"
                ]
