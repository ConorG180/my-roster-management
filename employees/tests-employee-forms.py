from django.test import TestCase
from .forms import Employeeform
from roles.models import Role


# role object needed for testing accurately with foreign key
class TestEmployeeForm(TestCase):

    def test_employee_id_is_required(self):
        role = Role.objects.create(role_id="10", title="TesterRole", hourly_wage="10")
        form = Employeeform({"employee_id": "", "first_name": "test_title", "last_name": "test_title", "date_of_birth": "1995-01-02", "gender": "M", "role": str(role.role_id), "pps_number": "8374928R", "phone_number": "+353872839059", "email": "test@testing.com", "start_date": "2022-03-11"})
        self.assertFalse(form.is_valid())
        self.assertIn("employee_id", form.errors.keys())
        self.assertEqual(form.errors["employee_id"][0], "This field is required.")

    def test_first_name_is_required(self):
        role = Role.objects.create(role_id="10", title="TesterRole", hourly_wage="10")
        form = Employeeform({"employee_id": "1", "first_name": "", "last_name": "test_title", "date_of_birth": "1995-01-02", "gender": "M", "role": str(role.role_id), "pps_number": "8374928R", "phone_number": "+353872839059", "email": "test@testing.com", "start_date": "2022-03-11"})
        self.assertFalse(form.is_valid())
        self.assertIn("first_name", form.errors.keys())
        self.assertEqual(form.errors["first_name"][0], "This field is required.")

    def test_last_name_is_required(self):
        role = Role.objects.create(role_id="10", title="TesterRole", hourly_wage="10")
        form = Employeeform({"employee_id": "1", "first_name": "test_title", "last_name": "", "date_of_birth": "1995-01-02", "gender": "M", "role": str(role.role_id), "pps_number": "8374928R", "phone_number": "+353872839059", "email": "test@testing.com", "start_date": "2022-03-11"})
        self.assertFalse(form.is_valid())
        self.assertIn("last_name", form.errors.keys())
        self.assertEqual(form.errors["last_name"][0], "This field is required.")
    
    def test_date_of_birth_is_required(self):
        role = Role.objects.create(role_id="10", title="TesterRole", hourly_wage="10")
        form = Employeeform({"employee_id": "1", "first_name": "test_title", "last_name": "test_title", "date_of_birth": "", "gender": "M", "role": str(role.role_id), "pps_number": "8374928R", "phone_number": "+353872839059", "email": "test@testing.com", "start_date": "2022-03-11"})
        self.assertFalse(form.is_valid())
        self.assertIn("date_of_birth", form.errors.keys())
        self.assertEqual(form.errors["date_of_birth"][0], "This field is required.")

    def test_gender_is_required(self):
        role = Role.objects.create(role_id="10", title="TesterRole", hourly_wage="10")
        form = Employeeform({"employee_id": "1", "first_name": "test_title", "last_name": "test_title", "date_of_birth": "1995-01-02", "gender": "", "role": str(role.role_id), "pps_number": "8374928R", "phone_number": "+353872839059", "email": "test@testing.com", "start_date": "2022-03-11"})
        self.assertFalse(form.is_valid())
        self.assertIn("gender", form.errors.keys())
        self.assertEqual(form.errors["gender"][0], "This field is required.")

    def test_role_is_required(self):
        role = Role.objects.create(role_id="10", title="TesterRole", hourly_wage="10")
        form = Employeeform({"employee_id": "1", "first_name": "test_title", "last_name": "test_title", "date_of_birth": "1995-01-02", "gender": "M", "role": "", "pps_number": "8374928R", "phone_number": "+353872839059", "email": "test@testing.com", "start_date": "2022-03-11"})
        self.assertFalse(form.is_valid())
        self.assertIn("role", form.errors.keys())
        self.assertEqual(form.errors["role"][0], "This field is required.")
    
    def test_pps_number_is_required(self):
        role = Role.objects.create(role_id="10", title="TesterRole", hourly_wage="10")
        form = Employeeform({"employee_id": "1", "first_name": "test_title", "last_name": "test_title", "date_of_birth": "1995-01-02", "gender": "M", "role": str(role.role_id), "pps_number": "", "phone_number": "+353872839059", "email": "test@testing.com", "start_date": "2022-03-11"})
        self.assertFalse(form.is_valid())
        self.assertIn("pps_number", form.errors.keys())
        self.assertEqual(form.errors["pps_number"][0], "This field is required.")

    def test_phone_number_is_required(self):
        role = Role.objects.create(role_id="10", title="TesterRole", hourly_wage="10")
        form = Employeeform({"employee_id": "1", "first_name": "test_title", "last_name": "test_title", "date_of_birth": "1995-01-02", "gender": "M", "role": str(role.role_id), "pps_number": "8374928R", "phone_number": "", "email": "test@testing.com", "start_date": "2022-03-11"})
        self.assertFalse(form.is_valid())
        self.assertIn("phone_number", form.errors.keys())
        self.assertEqual(form.errors["phone_number"][0], "This field is required.")

    def test_email_is_required(self):
        role = Role.objects.create(role_id="10", title="TesterRole", hourly_wage="10")
        form = Employeeform({"employee_id": "1", "first_name": "test_title", "last_name": "test_title", "date_of_birth": "1995-01-02", "gender": "M", "role": str(role.role_id), "pps_number": "8374928R", "phone_number": "+353872839059", "email": "", "start_date": "2022-03-11"})
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors.keys())
        self.assertEqual(form.errors["email"][0], "This field is required.")
    
    def test_start_date_is_required(self):
        role = Role.objects.create(role_id="10", title="TesterRole", hourly_wage="10")
        form = Employeeform({"employee_id": "1", "first_name": "test_title", "last_name": "test_title", "date_of_birth": "1995-01-02", "gender": "M", "role": str(role.role_id), "pps_number": "8374928R", "phone_number": "+353872839059", "email": "test@testing.com", "start_date": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("start_date", form.errors.keys())
        self.assertEqual(form.errors["start_date"][0], "This field is required.")

    def test_fields_are_explicit_in_form_metaclass(self):
        form = Employeeform()
        self.assertEqual(form.Meta.fields, ["employee_id", "first_name", "last_name", "date_of_birth", "gender", "role", "pps_number", "phone_number", "email", "start_date"])