from django import forms
from .models import Role

class Role_form(forms.ModelForm):
    class Meta:
        model = Role
        fields = ["role_id", "title", "hourly_wage"]