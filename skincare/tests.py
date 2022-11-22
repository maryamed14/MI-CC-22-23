from django.test import TestCase

# Create your tests here.

from .models import Issue


class IssuesTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.issue = Issue.objects.create(
            name="blackHeads", skin_type='OILY SKIN', solution='issue solution')

    def test_model_content(self):
        self.assertEqual(self.issue.name, "blackHeads")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
