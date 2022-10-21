"""Tests for views in workshift app."""
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Role


class TestRoleView(TestCase):
    """Tests for views in roles app."""

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

    def test_get_role_table(self):
        """Test if role_table can be accessed"""

        login = self.client.login(
            username='AuthorizedTestUserName',
            password='password'
        )

        response = self.client.get("/role/")
        self.assertTrue(login)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "role-table.html")

    def test_get_add_role(self):
        """Test if add_role can be accessed"""

        login = self.client.login(
            username='AuthorizedTestUserName',
            password='password'
        )

        response = self.client.get("/add-role/add")
        self.assertTrue(login)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "add-role.html")

    def test_get_edit_role(self):
        """Test if edit_role can be accessed"""

        role = Role.objects.create(
            role_id="10",
            title="TesterRole",
            hourly_wage="10"
        )

        login = self.client.login(
            username='AuthorizedTestUserName',
            password='password'
        )

        response = self.client.get(
            f"/edit-role/{role.role_id}"
        )

        self.assertTrue(login)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "edit-role.html")

    def test_can_add_role(self):
        """Test if role can be added"""

        login = self.client.login(
            username='AuthorizedTestUserName',
            password='password'
        )

        response = self.client.post(
            "/add-role/add",
            {
                "role_id": "10",
                "title": "TesterRole",
                "hourly_wage": "10"
            }
        )

        self.assertTrue(login)
        self.assertRedirects(response, "/role/")

    def test_can_delete_role(self):
        """Test if workshift can be deleted"""

        role = Role.objects.create(
            role_id="10",
            title="TesterRole",
            hourly_wage="10"
        )

        login = self.client.login(
            username='AuthorizedTestUserName',
            password='password'
        )

        response = self.client.get(
            f"/delete-role/{role.role_id}"
        )

        existing_roles = Role.objects.filter(
            role_id=role.role_id
            )

        self.assertEqual(len(existing_roles), 0)
        self.assertTrue(login)
        self.assertRedirects(response, "/role/")

    # TESTS FOR UNAUTHORIZED USERS
    def test_unauthorized_user_can_get_role_table(self):
        """Test if workshift_table can be accessed"""

        login = self.client.login(
            username='UnauthorizedTestUserName',
            password='password'
        )

        response = self.client.get("/role/")
        self.assertTrue(login)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "role-table.html")

    def test_cannot_get_add_role(self):
        """Test if add_workshift page cannot be accessed"""

        login = self.client.login(
            username='UnauthorizedTestUserName',
            password='password'
        )

        response = self.client.get("/add-role/add")
        self.assertTrue(login)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "unauthorized.html")

    def test_cannot_get_edit_role(self):
        """Test if add_workshift page cannot be accessed"""

        role = Role.objects.create(
            role_id="10",
            title="TesterRole",
            hourly_wage="10"
        )

        login = self.client.login(
            username='UnauthorizedTestUserName',
            password='password'
        )

        response = self.client.get(f"/edit-role/{role.role_id}")
        self.assertTrue(login)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "unauthorized.html")

    def test_cannot_add_role(self):
        """Test if role cannot be added"""

        login = self.client.login(
            username='UnauthorizedTestUserName',
            password='password'
        )

        response = self.client.post(
            "/add-role/add",
            {
                "role_id": "10",
                "title": "TesterRole",
                "hourly_wage": "10"
            }
        )
        existing_roles = Role.objects.all()
        self.assertTrue(login)
        self.assertTemplateUsed(response, "unauthorized.html")
        # Proved unsuccessful in adding role if unauthorized
        # by checking length of existing roles
        self.assertEqual(len(existing_roles), 0)

    def test_cannot_delete_role(self):
        """Test if workshift cannot be deleted"""

        role = Role.objects.create(
            role_id="10",
            title="TesterRole",
            hourly_wage="10"
        )

        login = self.client.login(
            username='UnauthorizedTestUserName',
            password='password'
        )

        response = self.client.get(
            f"/delete-role/{role.role_id}"
        )

        existing_roles = Role.objects.all()
        self.assertTrue(login)
        self.assertTemplateUsed(response, "unauthorized.html")
        # Proved unsuccessful in deleting role if unauthorized
        # by checking length of existing roles
        self.assertEqual(len(existing_roles), 1)
