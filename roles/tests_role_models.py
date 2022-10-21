"""Tests for models in roles app."""
from django.test import TestCase
from .models import Role


class TestRoleModel(TestCase):
    """Class for testing role models."""

    def test_title_is_less_than_50_characters_in_employee_model(self):
        """Test if title is less than 50 characters."""

        max_length = Role._meta.get_field("title").max_length
        self.assertTrue(max_length)

    def test_hourly_wage_has_2_decimal_places_in_employee_model(self):
        """Test if hourly_wage has 2 decimal places."""

        decimal_places = Role._meta.get_field("hourly_wage").decimal_places
        self.assertEqual(decimal_places, 2)

    def test_hourly_wage_is_less_than_5_digits_in_employee_model(self):
        """Test if hourly_wage has less than 5 digits."""

        max_digits = Role._meta.get_field("hourly_wage").max_digits
        self.assertEqual(max_digits, 5)
