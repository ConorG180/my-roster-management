"""Tests for models in employee app."""
from django.test import TestCase
from .models import Employee


class TestEmployeeModel(TestCase):
    """Class for testing employee models."""

    def test_pps_number_is_unique_in_employee_model(self):
        """Test if pps_number is unique."""

        unique_constraint = Employee._meta.get_field("pps_number").unique
        self.assertTrue(unique_constraint)

    def test_email_is_unique_in_employee_model(self):
        """Test if email is unique."""

        unique_constraint = Employee._meta.get_field("email").unique
        self.assertTrue(unique_constraint)
