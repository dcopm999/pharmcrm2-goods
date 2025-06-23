from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase
from django.urls import reverse

from goods import models

small_gif = (
    b"\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04"
    b"\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02"
    b"\x02\x4c\x01\x00\x3b"
)

User = get_user_model()


class HomeCase(TestCase):
    def setUp(self):
        user_admin = User.objects.create(
            username="admin", password="admin", is_superuser=True
        )
        self.client = Client()
        self.client.force_login(user=user_admin)

    def test_goods_home_accessible(self):
        response = self.client.get(reverse("home"))  # укажите нужный URL страницы
        self.assertEqual(response.status_code, 200)  # проверяем, что страница доступна


class MakerCase(TestCase):
    def setUp(self):
        user_admin = User.objects.create(
            username="admin", password="admin", is_superuser=True
        )
        self.client = Client()
        self.client.force_login(user=user_admin)
        self.maker = models.Maker.objects.create(name="Sanofi")

    def test_goods_maker_list_accessible(self):
        response = self.client.get(
            reverse("goods:maker-list")
        )  # укажите нужный URL страницы
        self.assertEqual(response.status_code, 200)  # проверяем, что страница доступна

    def test_goods_maker_detail_accessible(self):
        query = models.Maker.objects.last()
        response = self.client.get(
            reverse("goods:maker-detail", args=[query.slug])
        )  # укажите нужный URL страницы
        self.assertEqual(response.status_code, 200)  # проверяем, что страница доступна

    def test_goods_maker_create_accessible(self):
        response = self.client.get(
            reverse("goods:maker-create")
        )  # укажите нужный URL страницы
        self.assertEqual(response.status_code, 200)  # проверяем, что страница доступна

    def test_goods_maker_update(self):
        name = "name_update"
        query = models.Maker.objects.last()
        response = self.client.post(
            reverse("goods:maker-update", args=[query.slug]), {"name": name}
        )
        test_query = models.Maker.objects.get(name=name)
        self.assertRedirects(
            response, reverse("goods:maker-detail", args=[test_query.slug])
        )

    def test_goods_maker_delete_accessible(self):
        query = models.Maker.objects.create(name="PG")
        response = self.client.get(
            reverse("goods:maker-delete", args=[query.slug])
        )  # укажите нужный URL страницы
        self.assertEqual(response.status_code, 200)  # проверяем, что страница доступна


class TradeNameCase(TestCase):
    def setUp(self):
        user_admin = User.objects.create(
            username="admin", password="admin", is_superuser=True
        )
        self.client = Client()
        self.client.force_login(user=user_admin)
        catalog = models.Catalog.objects.create(name="обезболивающие")
        self.trade_name = models.TradeName.objects.create(name="Анальгин")
        maker = models.Maker.objects.create(name="Sanofi")
        unit = models.Unit.objects.create(name="шт.")
        packing = models.Packing.objects.create(name="табл.")
        original = models.OriginalPacking.objects.create(
            packing=packing, quantity=10, unit=unit
        )
        dosage = models.DosagePacking.objects.create(
            packing=packing, quantity=10, unit=unit
        )

        good = models.Good.objects.create(
            catalog=catalog,
            trade_name=self.trade_name,
            maker=maker,
            original_packing=original,
            dosage_packing=dosage,
        )
        self.query = models.GoodImage.objects.create(
            good=good,
            image=SimpleUploadedFile("small.gif", small_gif, content_type="image/gif"),
        )

    def test_goods_tradename_list_accessible(self):
        response = self.client.get(
            reverse("goods:tradename-list")
        )  # укажите нужный URL страницы
        self.assertEqual(response.status_code, 200)  # проверяем, что страница доступна

    def test_goods_tradename_detail_accessible(self):
        response = self.client.get(
            reverse("goods:tradename-detail", args=[self.trade_name.slug])
        )  # укажите нужный URL страницы
        self.assertEqual(response.status_code, 200)  # проверяем, что страница доступна

    def test_goods_tradename_create_accessible(self):
        response = self.client.get(
            reverse("goods:tradename-create")
        )  # укажите нужный URL страницы
        self.assertEqual(response.status_code, 200)  # проверяем, что страница доступна

    def test_goods_tradename_delete_accessible(self):
        response = self.client.get(
            reverse("goods:tradename-delete", args=[self.trade_name.slug])
        )  # укажите нужный URL страницы
        self.assertEqual(response.status_code, 200)  # проверяем, что страница доступна

    def test_goods_tradename_update(self):
        name = "name_update"
        query = models.TradeName.objects.last()
        response = self.client.post(
            reverse("goods:tradename-update", args=[query.slug]), {"name": name}
        )
        test_query = models.TradeName.objects.get(name=name)
        self.assertRedirects(
            response, reverse("goods:tradename-detail", args=[test_query.slug])
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

    def test_goods_update(self):
        trade_name = models.TradeName.objects.create(name="product_trade_name2")
        maker = models.Maker.objects.last()
        original_packing = models.OriginalPacking.objects.last()
        dosage_packing = models.DosagePacking.objects.last()
        catalog = models.Catalog.objects.last()
        query = models.Good.objects.last()

        response = self.client.post(
            reverse("goods:goods-update", args=[query.slug]),
            {
                "trade_name": trade_name.pk,
                "maker": maker.pk,
                "original_packing": original_packing.pk,
                "dosage_packing": dosage_packing.pk,
                "catalog": catalog.pk,
            },
        )
        test_query = models.Good.objects.last()
        self.assertRedirects(
            response, reverse("goods:goods-detail", args=[test_query.slug])
        )
