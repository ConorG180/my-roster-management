from django.test import TestCase
from .forms import RoleForm

class TestRoleForm(TestCase):

    def test_role_id_is_required(self):
        form = RoleForm({"role_id": "", "title": "test_title", "hourly_wage": "10.00"})
        self.assertFalse(form.is_valid())
        self.assertIn("role_id", form.errors.keys())
        self.assertEqual(form.errors["role_id"][0], "This field is required.")

    def test_title_is_required(self):
        form = RoleForm({"role_id": "10", "title": "", "hourly_wage": "10.00"})
        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors.keys())
        self.assertEqual(form.errors["title"][0], "This field is required.")

    def test_hourly_wage_is_required(self):
        form = RoleForm({"role_id": "10", "title": "test_title", "hourly_wage": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("hourly_wage", form.errors.keys())
        self.assertEqual(form.errors["hourly_wage"][0], "This field is required.")

    def test_fields_are_explicit_in_form_metaclass(self):
        form = RoleForm()
        self.assertEqual(form.Meta.fields, ["role_id", "title", "hourly_wage"])