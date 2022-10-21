"""Tests for views in workshift app."""
from django.test import TestCase
from django.contrib.auth import get_user_model
from roles.models import Role
from employees.models import Employee
from .models import Workshift


class TestworkshiftView(TestCase):
    """Tests for views in workshift app."""

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

    def test_get_workshift_table(self):
        """Test if workshift_table can be accessed"""

        login = self.client.login(
            username='AuthorizedTestUserName',
            password='password'
        )

        response = self.client.get("/workshift/")
        self.assertTrue(login)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "workshift.html")

    def test_get_add_workshift(self):
        """Test if add_workshift can be accessed"""

        login = self.client.login(
            username='AuthorizedTestUserName',
            password='password'
        )

        response = self.client.get("/add-workshift/add")
        self.assertTrue(login)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "add-workshift.html")

    def test_get_edit_workshift(self):
        """Test if edit_workshift can be accessed"""

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

        workshift = Workshift.objects.create(
            workshift_id="1",
            employee_id=employee,
            start_date="2022-10-11",
            start_time="09:00",
            end_date="2022-03-12",
            end_time="17:00",
            role_id=role
        )

        login = self.client.login(
            username='AuthorizedTestUserName',
            password='password'
        )

        response = self.client.get(f"/edit-workshift/{workshift.workshift_id}")
        self.assertTrue(login)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "edit-workshift.html")

    def test_can_add_workshift(self):
        """Test if workshift can be added"""

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
            gender="M", role=role,
            pps_number="8374928R",
            phone_number="+353872839059",
            email="test@testing.com",
            start_date="2022-03-11"
        )

        login = self.client.login(
            username='AuthorizedTestUserName',
            password='password'
        )

        response = self.client.post(
            "/add-workshift/add",
            {
                "workshift_id": "123456789",
                "employee_id": str(employee.employee_id),
                "start_date": "2022-03-11",
                "start_time": "09:00",
                "end_date": "2022-03-12",
                "end_time": "17:00",
                "role_id": str(role.role_id),
                "created_on": "2022-03-10"
            }
        )
        self.assertTrue(login)
        self.assertRedirects(response, "/workshift/")

    def test_can_delete_workshift(self):
        """Test if workshift can be deleted"""

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

        workshift = Workshift.objects.create(
            workshift_id="1",
            employee_id=employee,
            start_date="2022-10-11",
            start_time="09:00",
            end_date="2022-03-12",
            end_time="17:00",
            role_id=role
        )

        login = self.client.login(
            username='AuthorizedTestUserName',
            password='password'
        )

        response = self.client.get(
            f"/delete-workshift/{workshift.workshift_id}"
        )

        existing_workshifts = Workshift.objects.filter(
            workshift_id=workshift.workshift_id
        )

        self.assertEqual(len(existing_workshifts), 0)
        self.assertTrue(login)
        self.assertRedirects(response, "/workshift/")

    # TESTS FOR UNAUTHORIZED USERS
    def test_unauthorized_user_can_get_workshift_table(self):
        """Test if workshift_table can be accessed"""

        login = self.client.login(
            username='UnauthorizedTestUserName',
            password='password'
        )

        response = self.client.get("/workshift/")
        self.assertTrue(login)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "workshift.html")

    def test_cannot_get_add_workshift(self):
        """Test if add_workshift page cannot be accessed"""

        login = self.client.login(
            username='UnauthorizedTestUserName',
            password='password'
        )

        response = self.client.get("/add-workshift/add")
        self.assertTrue(login)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "unauthorized.html")

    def test_cannot_get_edit_workshift(self):
        """Test if edit_workshift page cannot be accessed"""

        login = self.client.login(
            username='UnauthorizedTestUserName',
            password='password'
        )

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

        workshift = Workshift.objects.create(
            workshift_id="1",
            employee_id=employee,
            start_date="2022-10-11",
            start_time="09:00",
            end_date="2022-03-12",
            end_time="17:00",
            role_id=role
        )

        response = self.client.get(f"/edit-workshift/{workshift.workshift_id}")
        self.assertTrue(login)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "unauthorized.html")

    def test_cannot_add_workshift(self):
        """Test if workshift cannot be added"""

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
            "/add-workshift/add",
            {
                "workshift_id": "10",
                "first_name": "test_title",
                "last_name": "test_title",
                "date_of_birth": "1995-01-02",
                "gender": "M", "role": str(role.role_id),
                "pps_number": "8374948R",
                "phone_number": "+353872539059",
                "email": "test@testing.com",
                "start_date": "2022-03-11"
            }
        )

        existing_workshifts = Workshift.objects.all()
        self.assertTrue(login)
        self.assertTemplateUsed(response, "unauthorized.html")
        # Proved unsuccessful in adding workshift if unauthorized
        # by checking length of existing workshifts
        self.assertEqual(len(existing_workshifts), 0)

    def test_cannot_delete_workshift(self):
        """Test if workshift cannot be deleted"""

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

        workshift = Workshift.objects.create(
            workshift_id="1",
            employee_id=employee,
            start_date="2022-10-11",
            start_time="09:00",
            end_date="2022-03-12",
            end_time="17:00",
            role_id=role
        )

        login = self.client.login(
            username='UnauthorizedTestUserName',
            password='password'
        )

        response = self.client.get(
            f"/delete-workshift/{workshift.workshift_id}"
            )

        existing_workshifts = Workshift.objects.all()
        self.assertTrue(login)
        self.assertTemplateUsed(response, "unauthorized.html")
        # Proved unsuccessful in deleting workshift if unauthorized
        # by checking length of existing workshifts
        self.assertEqual(len(existing_workshifts), 1)
