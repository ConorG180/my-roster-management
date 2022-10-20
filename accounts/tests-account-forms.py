from django.test import TestCase

from django.test import TestCase
from .forms import SignupForm

# class SignupForm(forms.Form):
#     first_name = forms.CharField(max_length=30)
#     last_name = forms.CharField(max_length=30)
#     is_staff = forms.BooleanField(required=False, label="Give this user permission to create/edit/delete company records and create new users?")

class TestSignupForm(TestCase):
    """We are testing the 3 custom fields here which we have input into our signup form. The other 2 fields (username and password) are handled by django-allauth """

    def test_first_name_is_required(self):

        form = SignupForm({"first_name": "", "last_name": "TestName", "is_staff": True})

        self.assertFalse(form.is_valid())
        self.assertIn("first_name", form.errors.keys())
        self.assertEqual(form.errors["first_name"][0], "This field is required.")

    def test_last_name_is_required(self):

        form = SignupForm({"first_name": "TestName", "last_name": "", "is_staff": True})

        self.assertFalse(form.is_valid())
        self.assertIn("last_name", form.errors.keys())
        self.assertEqual(form.errors["last_name"][0], "This field is required.")

    def test_is_staff_is_not_required(self):

        form = SignupForm({"first_name": "TestName", "last_name": "TestName", "is_staff": False})
        self.assertTrue(form.is_valid())