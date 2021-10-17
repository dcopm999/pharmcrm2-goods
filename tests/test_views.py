from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from goods import models

User = get_user_model()


class TradeNameCase(TestCase):
    fixtures = ["goods"]

    def setUp(self):
        user_admin = User.objects.create(
            username="admin", password="admin", is_superuser=True
        )
        self.client = Client()
        self.client.force_login(user=user_admin)

    def test_tradename_update(self):
        name = "name_update"
        query = models.TradeName.objects.last()
        response = self.client.post(
            reverse("goods:tradename-update", args=[query.slug]), {"name": name}
        )
        test_query = models.TradeName.objects.get(name=name)
        self.assertRedirects(
            response, reverse("goods:tradename-detail", args=[test_query.slug])
        )

    def test_maker_update(self):
        name = "name_update"
        query = models.Maker.objects.last()
        response = self.client.post(
            reverse("goods:maker-update", args=[query.slug]), {"name": name}
        )
        test_query = models.Maker.objects.get(name=name)
        self.assertRedirects(
            response, reverse("goods:maker-detail", args=[test_query.slug])
        )

    def test_packing_update(self):
        name = "name_update"
        query = models.Packing.objects.last()
        response = self.client.post(
            reverse("goods:packing-update", args=[query.slug]), {"name": name}
        )
        test_query = models.Packing.objects.get(name=name)
        self.assertRedirects(
            response, reverse("goods:packing-detail", args=[test_query.slug])
        )

    def test_unit_update(self):
        name = "name_update"
        query = models.Unit.objects.last()
        response = self.client.post(
            reverse("goods:unit-update", args=[query.slug]), {"name": name}
        )
        test_query = models.Unit.objects.get(name=name)
        self.assertRedirects(
            response, reverse("goods:unit-detail", args=[test_query.slug])
        )

    def test_catalog_update(self):
        name = "name_update"
        query = models.Catalog.objects.last()
        response = self.client.post(
            reverse("goods:catalog-update", args=[query.slug]), {"name": name}
        )
        test_query = models.Catalog.objects.get(name=name)
        self.assertRedirects(
            response, reverse("goods:catalog-detail", args=[test_query.slug])
        )

    def test_originalpacking_update(self):
        packing = models.Packing.objects.create(name="packing_test")
        unit = models.Unit.objects.create(name="unit_test")

        query = models.OriginalPacking.objects.last()
        response = self.client.post(
            reverse("goods:originalpacking-update", args=[query.slug]),
            {"packing": packing.pk, "quantity": 1, "unit": unit.pk},
        )
        test_query = models.OriginalPacking.objects.get(packing=packing, unit=unit)
        self.assertRedirects(
            response, reverse("goods:originalpacking-detail", args=[test_query.slug])
        )

    def test_dosagepacking_update(self):
        packing = models.Packing.objects.create(name="packing_test")
        unit = models.Unit.objects.create(name="unit_test")

        query = models.DosagePacking.objects.last()
        response = self.client.post(
            reverse("goods:dosagepacking-update", args=[query.slug]),
            {"packing": packing.pk, "quantity": 1, "unit": unit.pk},
        )
        test_query = models.DosagePacking.objects.get(packing=packing, unit=unit)
        self.assertRedirects(
            response, reverse("goods:dosagepacking-detail", args=[test_query.slug])
        )

    def test_pharmproduct_update(self):
        trade_name = models.TradeName.objects.create(name="product_trade_name2")
        maker = models.Maker.objects.last()
        original_packing = models.OriginalPacking.objects.last()
        dosage_packing = models.DosagePacking.objects.last()
        catalog = models.Catalog.objects.last()
        query = models.PharmProduct.objects.last()

        response = self.client.post(
            reverse("goods:pharmproduct-update", args=[query.slug]),
            {
                "trade_name": trade_name.pk,
                "maker": maker.pk,
                "original_packing": original_packing.pk,
                "dosage_packing": dosage_packing.pk,
                "catalog": catalog.pk,
            },
        )
        test_query = models.PharmProduct.objects.last()
        self.assertRedirects(
            response, reverse("goods:pharmproduct-detail", args=[test_query.slug])
        )
