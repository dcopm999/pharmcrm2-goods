from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from goods import factories

User = get_user_model()


class ApiCase(APITestCase):
    def setUp(self):
        # self.factory = factories.GoodFactory()
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
        factory = factories.OriginalPackingFactory()
        url = reverse("goods-api:originalpacking-list")
        response = self.client.post(
            url,
            {"packing": factory.packing_id, "unit": factory.unit_id, "quantity": 0.1},
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_dosage_packing(self):
        factory = factories.DosagePackingFactory()
        url = reverse("goods-api:dosagepacking-list")
        response = self.client.post(
            url,
            {"packing": factory.packing_id, "unit": factory.unit_id, "quantity": 1.0},
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    """
    def test_good(self):
        factory = factories.GoodFactory.create()
        url = reverse("goods-api:good-list")
        response = self.client.post(
            url,
            {
                "catalog": factory.catalog_id,
                "trade_name": factory.trade_name_id,
                "maker": factory.maker_id,
                "original_packing": factory.original_packing_id,
                "dosage_packing": factory.dosage_packing_id,
            },
        )
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    """

    def test_good_image(self):
        url = reverse("goods-api:goodimage-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
