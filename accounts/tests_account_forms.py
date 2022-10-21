"""Tests for forms in accounts app."""
from django.test import TestCase
from .forms import SignupForm


class TestSignupForm(TestCase):
    """We are testing the 3 custom fields here which we have
    input into our signup form.
    The other 2 fields (username and password) are handled
    by django-allauth """

    def test_first_name_is_required(self):
        """Test if employee_id is required."""

        form = SignupForm(
            {
                "first_name": "",
                "last_name": "TestName",
                "is_staff": True
            }
        )

        self.assertFalse(form.is_valid())
        self.assertIn("first_name", form.errors.keys())
        self.assertEqual(
                form.errors["first_name"][0],
                "This field is required."
            )

    def test_last_name_is_required(self):
        """Test last name is required."""

        form = SignupForm(
            {
                "first_name": "TestName",
                "last_name": "",
                "is_staff": True
            }
        )

        self.assertFalse(form.is_valid())
        self.assertIn("last_name", form.errors.keys())
        self.assertEqual(
            form.errors["last_name"][0],
            "This field is required."
        )

    def test_is_staff_is_not_required(self):
        """Test is_staff is not required."""

        form = SignupForm(
            {
                "first_name": "TestName",
                "last_name": "TestName",
                "is_staff": False
            }
        )
        self.assertTrue(form.is_valid())
