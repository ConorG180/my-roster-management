"""Forms in workshifts app."""
from django import forms
from .models import Workshift


class DateInput(forms.DateInput):
    """Controls input style of date fields"""
    input_type = "date"


class TimeInput(forms.TimeInput):
    """Controls input style of time fields"""
    input_type = "time"


class WorkshiftForm(forms.ModelForm):
    """Customize fields for the workshift form"""

    start_date = forms.DateField(widget=DateInput)
    start_time = forms.TimeField(widget=TimeInput)
    end_date = forms.DateField(widget=DateInput)
    end_time = forms.TimeField(widget=TimeInput)

    class Meta:
        """Set fields to appear in employee form"""

        model = Workshift
        fields = [
            "workshift_id",
            "employee_id",
            "start_time",
            "start_date",
            "end_time",
            "end_date",
            "role_id"
        ]
