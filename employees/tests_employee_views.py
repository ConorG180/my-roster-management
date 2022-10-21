"""Tests for views in employee app."""
from django.test import TestCase
from django.contrib.auth import get_user_model
from roles.models import Role
from .models import Employee


class TestEmployeeView(TestCase):
    """Tests for views in employee app."""

    def setUp(self):
        """Set up authorized and unauthorized users."""

        user = get_user_model()

        # Authorized user
        self.authorized_user = user.objects.create_user(
            username='AuthorizedTestUserName',
            first_name='test name',
            email='test@test.test',
            password='password',
            is_staff=True,
        )

        # Unauthorized user
        self.unauthorized_user = user.objects.create_user(
            username='UnauthorizedTestUserName',
            first_name='test name',
            email='test@test.test',
            password='password',
            is_staff=False,
        )

    # TESTS FOR AUTHORIZED USERS

    def test_get_employee_table(self):
        """Test if employee_table can be accessed"""

        login = self.client.login(
            username='AuthorizedTestUserName',
            password='password'
        )

        response = self.client.get("/employee/")
        self.assertTrue(login)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "employee.html")

    def test_get_add_employee(self):
        """Test if add_employee can be accessed"""

        login = self.client.login(
            username='AuthorizedTestUserName',
            password='password'
        )

        response = self.client.get("/add-employee/add")
        self.assertTrue(login)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "add-employee.html")

    def test_get_edit_employee(self):
        """Test if edit_employee page can be accessed"""

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

        login = self.client.login(
            username='AuthorizedTestUserName',
            password='password'
        )

        response = self.client.get(f"/edit-employee/{employee.employee_id}")
        self.assertTrue(login)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "edit-employee.html")

    def test_can_add_employee(self):
        """Test if employee can be added"""

        role = Role.objects.create(
            role_id="10",
            title="TesterRole",
            hourly_wage="10"
        )

        login = self.client.login(
            username='AuthorizedTestUserName',
            password='password'
        )

        response = self.client.post(
            "/add-employee/add",
            {
                "employee_id": "10",
                "first_name": "test_title",
                "last_name": "test_title",
                "date_of_birth": "1995-01-02",
                "gender": "M",
                "role": str(role.role_id),
                "pps_number": "8374928R",
                "phone_number": "+353872839059",
                "email": "test@testing.com",
                "start_date": "2022-03-11"
            }
        )
        self.assertTrue(login)
        self.assertRedirects(response, "/employee/")

    def test_can_delete_employee(self):
        """Test if employee can be deleted"""

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

        login = self.client.login(
            username='AuthorizedTestUserName',
            password='password'
        )

        response = self.client.get(f"/delete-employee/{employee.employee_id}")
        existing_employees = Employee.objects.filter(
            employee_id=employee.employee_id
        )

        self.assertEqual(len(existing_employees), 0)
        self.assertTrue(login)
        self.assertRedirects(response, "/employee/")

    # TESTS FOR UNAUTHORIZED USERS
    def test_unauthorized_user_can_get_employee_table(self):
        """Test if employee_table can be accessed"""

        login = self.client.login(
            username='UnauthorizedTestUserName',
            password='password'
        )

        response = self.client.get("/employee/")
        self.assertTrue(login)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "employee.html")

    def test_cannot_get_add_employee(self):
        """Test if add_employee page cannot be accessed"""

        login = self.client.login(
            username='UnauthorizedTestUserName',
            password='password'
        )

        response = self.client.get("/add-employee/add")
        self.assertTrue(login)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "unauthorized.html")

    def test_cannot_get_edit_employee(self):
        """Test if edit_employee page cannot be accessed"""

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

        login = self.client.login(
            username='UnauthorizedTestUserName',
            password='password'
        )

        response = self.client.get(f"/edit-employee/{employee.employee_id}")
        self.assertTrue(login)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "unauthorized.html")

    def test_cannot_add_employee(self):
        """Test if employee cannot be added"""

        role = Role.objects.create(
            role_id="10",
            title="TesterRole",
            hourly_wage="10"
        )

        login = self.client.login(
            username='UnauthorizedTestUserName',
            password='password'
        )

        response = self.client.post(
            "/add-employee/add",
            {
                "employee_id": "10",
                "first_name": "test_title",
                "last_name": "test_title",
                "date_of_birth": "1995-01-02",
                "gender": "M",
                "role": str(role.role_id),
                "pps_number": "8374928R",
                "phone_number": "+353872839059",
                "email": "test@testing.com",
                "start_date": "2022-03-11"
            }
        )

        existing_employees = Employee.objects.all()
        self.assertTrue(login)
        self.assertTemplateUsed(response, "unauthorized.html")
        # Proved unsuccessful in adding employee if unauthorized
        # by checking length of existing employees
        self.assertEqual(len(existing_employees), 0)

    def test_cannot_delete_employee(self):
        """Test if employee cannot be deleted"""

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

        login = self.client.login(
            username='UnauthorizedTestUserName',
            password='password'
        )

        response = self.client.get(f"/delete-employee/{employee.employee_id}")
        existing_employees = Employee.objects.all()
        self.assertTrue(login)
        self.assertTemplateUsed(response, "unauthorized.html")
        # Proved unsuccessful in deleting employee if unauthorized
        # by checking length of existing employees
        self.assertEqual(len(existing_employees), 1)
