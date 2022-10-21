"""Forms in roles app."""
from django import forms
from .models import Role


class DecimalInput(forms.NumberInput):
    """Controls input style of Decimal fields"""

    input_type = "number"


class RoleForm(forms.ModelForm):
    """Customize fields for the workshift form"""

    hourly_wage = forms.DecimalField(widget=DecimalInput)

    class Meta:
        """Set fields to appear in employee form"""
        model = Role
        fields = ["role_id", "title", "hourly_wage"]
