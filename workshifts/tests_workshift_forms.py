"""Tests for forms in workshift apps.
Role object and employee objects needed for
testing accurately with foreign keys.
"workshift_id" and "created_on" fields are
not tested as "workshift_id" is of type
"BigAutoField" and "created_on" is
automatically added depending on date.
"""
from django.test import TestCase
from roles.models import Role
from employees.models import Employee
from .forms import WorkshiftForm


class TestWorkshiftForm(TestCase):
    """Class for testing workshift forms."""

    def test_employee_id_is_required(self):
        """Test if employee_id is required."""

        role = Role.objects.create(
            role_id="10",
            title="TesterRole",
            hourly_wage="10"
        )

        form = WorkshiftForm(
            {
                "workshift_id": "123456789",
                "employee_id": "",
                "start_date": "2022-03-11",
                "start_time": "09:00",
                "end_date": "2022-03-12",
                "end_time": "17:00",
                "role_id": str(role.role_id),
                "created_on": "2022-03-10"
            }
        )

        self.assertFalse(form.is_valid())
        self.assertIn("employee_id", form.errors.keys())
        self.assertEqual(
            form.errors["employee_id"][0],
            "This field is required."
        )

    def test_start_date_is_required(self):
        """Test if start_date is required."""

        role = Role.objects.create(
            role_id="10",
            title="TesterRole",
            hourly_wage="10"
        )

        employee = Employee.objects.create(
            employee_id="1",
            first_name="test_title",
            last_name="test_title",
            date_of_birth="1995-01-02",
            gender="M",
            role=role,
            pps_number="8374928R",
            phone_number="+353872839059",
            email="test@testing.com",
            start_date="2022-03-11"
        )

        form = WorkshiftForm(
            {
                "workshift_id": "123456789",
                "employee_id": str(employee.role_id),
                "start_date": "",
                "start_time": "09:00",
                "end_date": "2022-03-12",
                "end_time": "17:00",
                "role_id": str(role.role_id),
                "created_on": "2022-03-10"
            }
        )

        self.assertFalse(form.is_valid())
        self.assertIn("start_date", form.errors.keys())
        self.assertEqual(
            form.errors["start_date"][0],
            "This field is required."
        )

    def test_start_time_is_required(self):
        """Test if start_time is required."""

        role = Role.objects.create(
            role_id="10",
            title="TesterRole",
            hourly_wage="10"
        )

        employee = Employee.objects.create(
            employee_id="1",
            first_name="test_title",
            last_name="test_title",
            date_of_birth="1995-01-02",
            gender="M",
            role=role,
            pps_number="8374928R",
            phone_number="+353872839059",
            email="test@testing.com",
            start_date="2022-03-11"
        )

        form = WorkshiftForm(
            {
                "workshift_id": "123456789",
                "employee_id": str(employee.role_id),
                "start_date": "2022-03-11",
                "start_time": "",
                "end_date": "2022-03-12",
                "end_time": "17:00",
                "role_id": str(role.role_id),
                "created_on": "2022-03-10"
            }
        )

        self.assertFalse(form.is_valid())
        self.assertIn("start_time", form.errors.keys())
        self.assertEqual(
            form.errors["start_time"][0],
            "This field is required."
        )

    def test_end_date_is_required(self):
        """Test if end_date is required."""

        role = Role.objects.create(
            role_id="10",
            title="TesterRole",
            hourly_wage="10"
        )

        employee = Employee.objects.create(
            employee_id="1",
            first_name="test_title",
            last_name="test_title",
            date_of_birth="1995-01-02",
            gender="M",
            role=role,
            pps_number="8374928R",
            phone_number="+353872839059",
            email="test@testing.com",
            start_date="2022-03-11"
        )

        form = WorkshiftForm(
            {
                "workshift_id": "123456789",
                "employee_id": str(employee.role_id),
                "start_date": "2022-03-11",
                "start_time": "09:00",
                "end_date": "",
                "end_time": "17:00",
                "role_id": str(role.role_id),
                "created_on": "2022-03-10"
            }
        )

        self.assertFalse(form.is_valid())
        self.assertIn("end_date", form.errors.keys())
        self.assertEqual(
            form.errors["end_date"][0],
            "This field is required."
        )

    def test_end_time_is_required(self):
        """Test if end_time is required."""

        role = Role.objects.create(
            role_id="10",
            title="TesterRole",
            hourly_wage="10"
        )

        employee = Employee.objects.create(
            employee_id="1",
            first_name="test_title",
            last_name="test_title",
            date_of_birth="1995-01-02",
            gender="M",
            role=role,
            pps_number="8374928R",
            phone_number="+353872839059",
            email="test@testing.com",
            start_date="2022-03-11"
        )

        form = WorkshiftForm(
            {
                "workshift_id": "123456789",
                "employee_id": str(employee.role_id),
                "start_date": "2022-03-11",
                "start_time": "09:00",
                "end_date": "2022-03-12",
                "end_time": "",
                "role_id": str(role.role_id),
                "created_on": "2022-03-10"
            }
        )

        self.assertFalse(form.is_valid())
        self.assertIn("end_time", form.errors.keys())
        self.assertEqual(
            form.errors["end_time"][0],
            "This field is required."
        )

    def test_role_id_is_required(self):
        """Test if role_id is required."""

        role = Role.objects.create(
            role_id="10",
            title="TesterRole",
            hourly_wage="10"
        )

        employee = Employee.objects.create(
            employee_id="1",
            first_name="test_title",
            last_name="test_title",
            date_of_birth="1995-01-02",
            gender="M",
            role=role,
            pps_number="8374928R",
            phone_number="+353872839059",
            email="test@testing.com",
            start_date="2022-03-11"
        )

        form = WorkshiftForm(
            {
                "workshift_id": "123456789",
                "employee_id": str(employee.role_id),
                "start_date": "2022-03-11",
                "start_time": "09:00",
                "end_date": "2022-03-12",
                "end_time": "17:00",
                "role_id": "",
                "created_on": "2022-03-10"
            }
        )

        self.assertFalse(form.is_valid())
        self.assertIn("role_id", form.errors.keys())
        self.assertEqual(
            form.errors["role_id"][0],
            "This field is required."
        )

    def test_fields_are_explicit_in_form_metaclass(self):
        """Test if correct fields are present."""

        form = WorkshiftForm()
        self.assertEqual(
            form.Meta.fields,
            [
                "workshift_id",
                "employee_id",
                "start_time",
                "start_date",
                "end_time",
                "end_date",
                "role_id"
            ]
        )
