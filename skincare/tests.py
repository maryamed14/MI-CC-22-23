from django.test import TestCase
import unittest
# Create your tests here.
from django.test import Client
from django.urls import reverse

from .models import Issue
from .models import Person

from rest_framework.test import APITestCase
from rest_framework.test import APIClient

from rest_framework import status


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


class personAPITestCase(APITestCase):
    def test_create_person(self):

        data = {'name': 'DabApps', 'age': '33'}
        response = self.client.post('/api/people/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read_person(self):

        data = {'name': 'DabApps', 'age': '33'}
        response = self.client.get('/api/people/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

   # def test_read_person(self):

    #    data = {'name': 'DabApps', 'age': '33'}
    #    response = self.client.put('/api/people/', data, format='json')
    #    self.assertEqual(response.status_code, status.HTTP_200_OK)
    #    self.assertEqual(Person.objects.count(), 1)
    #    self.assertEqual(person.objects.get().name, 'DabApps')

  #  @classmethod
   # def setUp(self):
    #    self.client = APIClient()
    #    self.person_data = {'name': 'John', 'age': 30}
   #     self.response = self.client.post(
     #       '/people/', self.person_data, format='json')

   # def test_api_create(self):
        # Test creating a new object
      #  self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
      #  self.assertEqual(Person.objects.count(), 1)
      #  self.assertEqual(Person.objects.get().name, 'ane')
