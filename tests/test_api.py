from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


class ApiCase(APITestCase):
    def setUp(self):
        credentials = {"username": "admin", "password": "admin"}
        user = User.objects.create_user(**credentials)
        self.client.force_authenticate(user=user)

    def test_catalog(self):
        url = reverse("goods-api:catalog-list")
        response = self.client.post(url, {"name": "catalog_test"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_trade_name(self):
        url = reverse("goods-api:tradename-list")
        response = self.client.post(url, {"name": "trade_name_test"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_maker(self):
        url = reverse("goods-api:maker-list")
        response = self.client.post(url, {"name": "maker_test"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_packing(self):
        url = reverse("goods-api:packing-list")
        response = self.client.post(url, {"name": "packing_test"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unit(self):
        url = reverse("goods-api:unit-list")
        response = self.client.post(url, {"name": "unit_test"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_original_packing(self):
        self.test_packing()
        self.test_unit()
        url = reverse("goods-api:originalpacking-list")
        response = self.client.post(url, {"packing": 1, "unit": 1, "quantity": 0.1})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_dosage_packing(self):
        self.test_packing()
        self.test_unit()
        url = reverse("goods-api:dosagepacking-list")
        response = self.client.post(url, {"packing": 1, "unit": 1, "quantity": 1.0})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_pharm_product(self):
        self.test_trade_name()
        self.test_maker()
        self.test_catalog()
        self.test_original_packing()
        self.test_dosage_packing()
        url = reverse("goods-api:pharmproduct-list")
        response = self.client.post(
            url,
            {
                "catalog": 1,
                "trade_name": 1,
                "maker": 1,
                "original_packing": 1,
                "dosage_packing": 1,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_pharm_product_image(self):
        url = reverse("goods-api:pharmproductimage-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
