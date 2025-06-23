#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pharmcrm2-goods
------------

Tests for `pharmcrm2-goods` models module.
"""
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from slugify import slugify

from goods import models

small_gif = (
    b"\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04"
    b"\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02"
    b"\x02\x4c\x01\x00\x3b"
)


class TradeNameModelCase(TestCase):
    def setUp(self):
        self.query = models.TradeName.objects.create(name="Анальгин")

    def test_tradename_absolute_url(self):
        self.assertEqual(
            self.query.get_absolute_url(),
            reverse("goods:tradename-detail", args=[str(self.query.slug)]),
        )

    def test_tradename_str(self):
        self.assertEqual(self.query.__str__(), self.query.name)

    def test_tradename_slug(self):
        self.assertEqual(self.query.slug, slugify(self.query.name))

    def tearDown(self):
        pass


class MakerModelCase(TestCase):
    def setUp(self):
        self.query = models.Maker.objects.create(name="Sanofi")

    def test_maker_absolute_url(self):
        self.assertEqual(
            self.query.get_absolute_url(),
            reverse("goods:maker-detail", args=[str(self.query.slug)]),
        )

    def test_maker_str(self):
        self.assertEqual(self.query.__str__(), self.query.name)

    def test_maker_slug(self):
        self.assertEqual(self.query.slug, slugify(self.query.name))

    def tearDown(self):
        pass


class PackingModelCase(TestCase):
    def setUp(self):
        self.query = models.Packing.objects.create(name="табл.")

    def test_packing_absolute_url(self):
        self.assertEqual(
            self.query.get_absolute_url(),
            reverse("goods:packing-detail", args=[str(self.query.slug)]),
        )

    def test_packing_str(self):
        self.assertEqual(self.query.__str__(), self.query.name)

    def test_packing_slug(self):
        self.assertEqual(self.query.slug, slugify(self.query.name))

    def tearDown(self):
        pass


class UnitModelCase(TestCase):
    def setUp(self):
        self.query = models.Unit.objects.create(name="шт.")

    def test_unit_absolute_url(self):
        self.assertEqual(
            self.query.get_absolute_url(),
            reverse("goods:unit-detail", args=[str(self.query.slug)]),
        )

    def test_unit_str(self):
        self.assertEqual(self.query.__str__(), self.query.name)

    def test_unit_slug(self):
        self.assertEqual(self.query.slug, slugify(self.query.name))

    def tearDown(self):
        pass


class CatalogModelCase(TestCase):
    def setUp(self):
        self.query = models.Catalog.objects.create(name="обезболивающие")

    def test_catalog_absolute_url(self):
        self.assertEqual(
            self.query.get_absolute_url(),
            reverse("goods:catalog-detail", args=[str(self.query.slug)]),
        )

    def test_catalog_str(self):
        self.assertEqual(self.query.__str__(), self.query.name)

    def test_catalog_slug(self):
        self.assertEqual(self.query.slug, slugify(self.query.name))

    def tearDown(self):
        pass


class OriginalPackingModelCase(TestCase):
    def setUp(self):
        unit = models.Unit.objects.create(name="шт.")
        packing = models.Packing.objects.create(name="табл.")
        self.query = models.OriginalPacking.objects.create(
            packing=packing, quantity=10, unit=unit
        )

    def test_originalpacking_absolute_url(self):
        self.assertEqual(
            self.query.get_absolute_url(),
            reverse("goods:originalpacking-detail", args=[str(self.query.slug)]),
        )

    def test_originalpacking_str(self):
        self.assertEqual(
            self.query.__str__(),
            f"{self.query.packing} {self.query.quantity} {self.query.unit}",
        )

    def test_originalpacking_slug(self):
        self.assertEqual(self.query.slug, slugify(self.query.__str__()))

    def tearDown(self):
        pass


class DosagePackingModelCase(TestCase):
    def setUp(self):
        unit = models.Unit.objects.create(name="шт.")
        packing = models.Packing.objects.create(name="табл.")
        self.query = models.DosagePacking.objects.create(
            packing=packing, quantity=10, unit=unit
        )

    def test_dosagepacking_absolute_url(self):
        self.assertEqual(
            self.query.get_absolute_url(),
            reverse("goods:dosagepacking-detail", args=[str(self.query.slug)]),
        )

    def test_dosagepacking_str(self):
        self.assertEqual(
            self.query.__str__(),
            f"{self.query.packing} {self.query.quantity} {self.query.unit}",
        )

    def test_dosagepacking_slug(self):
        self.assertEqual(self.query.slug, slugify(self.query.__str__()))

    def tearDown(self):
        pass


class GoodModelCase(TestCase):
    def setUp(self):
        catalog = models.Catalog.objects.create(name="обезболивающие")
        trade_name = models.TradeName.objects.create(name="Анальгин")
        maker = models.Maker.objects.create(name="Sanofi")
        unit = models.Unit.objects.create(name="шт.")
        packing = models.Packing.objects.create(name="табл.")
        original = models.OriginalPacking.objects.create(
            packing=packing, quantity=10, unit=unit
        )
        dosage = models.DosagePacking.objects.create(
            packing=packing, quantity=10, unit=unit
        )

        self.query = models.Good.objects.create(
            catalog=catalog,
            trade_name=trade_name,
            maker=maker,
            original_packing=original,
            dosage_packing=dosage,
        )

    def test_good_absolute_url(self):
        self.assertEqual(
            self.query.get_absolute_url(),
            reverse("goods:goods-detail", args=[str(self.query.slug)]),
        )

    def test_good_str(self):
        self.assertEqual(
            self.query.__str__(),
            f"{self.query.maker.name}: {self.query.trade_name.name}, {self.query.dosage_packing.__str__()}, {self.query.original_packing.__str__()}",  # noqa
        )

    def test_good_fullname(self):
        self.assertEqual(self.query.__str__(), self.query.full_name)

    def test_good_slug(self):
        self.assertEqual(self.query.slug, slugify(self.query.__str__()))

    def tearDown(self):
        pass


class GoodImageModelCase(TestCase):
    def setUp(self):
        catalog = models.Catalog.objects.create(name="обезболивающие")
        trade_name = models.TradeName.objects.create(name="Анальгин")
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
            trade_name=trade_name,
            maker=maker,
            original_packing=original,
            dosage_packing=dosage,
        )
        self.query = models.GoodImage.objects.create(
            good=good,
            image=SimpleUploadedFile("small.gif", small_gif, content_type="image/gif"),
        )

    def test_good_image_str(self):
        self.assertEqual(self.query.__str__(), self.query.image.url)

    def tearDown(self):
        pass
