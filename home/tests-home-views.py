from django.test import TestCase

class TestHomeView(TestCase):

    def test_get_todo_list(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")