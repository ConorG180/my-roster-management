from django import forms
from .models import Role


class DecimalInput(forms.NumberInput):
    input_type = "number"


class RoleForm(forms.ModelForm):
    hourly_wage = forms.DecimalField(widget=DecimalInput)

    class Meta:
        model = Role
        fields = ["role_id", "title", "hourly_wage"]