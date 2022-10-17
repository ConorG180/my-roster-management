from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import Employee

class DateInput(forms.DateInput):
    input_type = "date"

class Employee_form(forms.ModelForm):
    date_of_birth = forms.DateField(widget=DateInput)
    phone_number = PhoneNumberField(widget=forms.TextInput(attrs={"placeholder": "e.g. +353872703824"}))
    start_date = forms.DateField(widget=DateInput)
    email = forms.EmailField()
    class Meta:
        model = Employee
        fields = ["employee_id", "first_name", "last_name", "date_of_birth", "gender", "role", "pps_number", "phone_number", "email", "start_date"]