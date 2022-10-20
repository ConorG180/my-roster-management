from django.test import TestCase
from .models import Employee

class TestEmployeeModel(TestCase):

    def test_pps_number_is_unique_in_employee_model(self):
        unique_constraint = Employee._meta.get_field("pps_number").unique
        self.assertTrue(unique_constraint)
    
    def test_email_is_unique_in_employee_model(self):
        unique_constraint = Employee._meta.get_field("email").unique
        self.assertTrue(unique_constraint)