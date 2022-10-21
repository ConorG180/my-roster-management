from django.test import TestCase
from .models import Workshift

class TestWorkshiftModel(TestCase):

    def test_created_on_is_automatic_in_employee_model(self):
        auto_now_add = Workshift._meta.get_field("created_on").auto_now_add
        self.assertTrue(auto_now_add)