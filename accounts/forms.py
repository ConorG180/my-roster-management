"""Forms in accounts app."""
from django import forms


class SignupForm(forms.Form):
    """Customize fields for the signup/registration form"""
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    is_staff = forms.BooleanField(
        required=False,
        label="Give this user permission to create/edit/delete"
        "company records and create new users?"
        )

    def signup(self, request, user):
        """Add fields to the signup/registration form"""
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.is_staff = self.cleaned_data["is_staff"]
        user.save()
