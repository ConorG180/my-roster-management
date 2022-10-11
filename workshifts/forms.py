from django import forms
from .models import Workshift


class Workshift_form(forms.ModelForm):
    class Meta:
        model = Workshift
        fields = ["workshift_id", "employee_id", "start_time", "end_time", "role_id"]