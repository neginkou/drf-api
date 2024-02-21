from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Snack


class SnackTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_snack = Snack.objects.create(
            name="Protein bar",
            owner=testuser1,  
            description="nut free and delicious!",
        )
        test_snack.save()

    def test_snacks_model(self):
        snack = Snack.objects.get(id=1)
        actual_owner = str(snack.owner) 
        actual_name = str(snack.name)
        actual_description = str(snack.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "Protein bar")
        self.assertEqual(
            actual_description, "nut free and delicious!"
        )

    def test_get_snack_list(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        snacks = response.data
        self.assertEqual(len(snacks), 1)
        self.assertEqual(snacks[0]["name"], "Protein bar")

    def test_get_snack_by_id(self):
        url = reverse("snack_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        snack = response.data
        self.assertEqual(snack["name"], "Protein bar")

    def test_create_snack(self):
        self.client.login(username="testuser1", password="pass")
        url = reverse("snack_list")
        data = {"owner": 1, "name": "chips", "description": "Crunchy and delicious potato chips."}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        snacks = Snack.objects.all()
        self.assertEqual(len(snacks), 2)
        self.assertEqual(Snack.objects.get(id=2).name, "chips")

    def test_update_snack(self):
        self.client.login(username="testuser1", password="pass")
        url = reverse("snack_detail", args=(1,))
        testuser1_id = get_user_model().objects.get(username="testuser1").id
        data = {
            "owner": testuser1_id,
            "name": "Updated Protein Bar",
            "description": "Updated description",
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        snack = Snack.objects.get(id=1)
        self.assertEqual(snack.name, "Updated Protein Bar")
        self.assertEqual(snack.description, "Updated description")


    def test_delete_snack(self):
        self.client.login(username="testuser1", password="pass")
        url = reverse("snack_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        snacks = Snack.objects.all()
        self.assertEqual(len(snacks), 0)
