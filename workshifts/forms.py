from django import forms
from .models import Workshift


class DateInput(forms.DateInput):
    input_type = "date"


class TimeInput(forms.TimeInput):
    input_type = "time"


class WorkshiftForm(forms.ModelForm):
    start_date = forms.DateField(widget=DateInput)
    start_time = forms.TimeField(widget=TimeInput)
    end_date = forms.DateField(widget=DateInput)
    end_time = forms.TimeField(widget=TimeInput)

    class Meta:
        model = Workshift
        fields = ["workshift_id", "employee_id", "start_time", "start_date", "end_time", "end_date", "role_id"]