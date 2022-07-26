import factory
from factory.django import DjangoModelFactory

from goods import models

factory.Faker._DEFAULT_LOCALE = "ru_RU"


class TradeNameFactory(DjangoModelFactory):
    name = factory.Faker("word")

    class Meta:
        model = models.TradeName


class MakerFactory(DjangoModelFactory):
    name = factory.Faker("company")

    class Meta:
        model = models.Maker


class PackingFactory(DjangoModelFactory):
    name = factory.Faker("word")

    class Meta:
        model = models.Packing


class UnitFactory(DjangoModelFactory):
    name = factory.Faker("word")

    class Meta:
        model = models.Unit


class OriginalPackingFactory(DjangoModelFactory):
    packing = factory.SubFactory(PackingFactory)
    quantity = 10.00
    unit = factory.SubFactory(UnitFactory)

    class Meta:
        model = models.OriginalPacking


class DosagePackingFactory(DjangoModelFactory):
    packing = factory.SubFactory(PackingFactory)
    quantity = 10.00
    unit = factory.SubFactory(UnitFactory)

    class Meta:
        model = models.DosagePacking


class CatalogFactory(DjangoModelFactory):
    name = factory.Faker("word")

    class Meta:
        model = models.Catalog


class GoodFactory(DjangoModelFactory):
    trade_name = factory.SubFactory(TradeNameFactory)
    maker = factory.SubFactory(MakerFactory)
    original_packing = factory.SubFactory(OriginalPackingFactory)
    dosage_packing = factory.SubFactory(DosagePackingFactory)
    catalog = factory.SubFactory(CatalogFactory)

    class Meta:
        model = models.Good
        django_get_or_create = (
            "trade_name",
            "maker",
            "original_packing",
            "dosage_packing",
        )


class GoodImageFactory(DjangoModelFactory):
    good = factory.SubFactory(GoodFactory)
    image = factory.Faker("file_path")

    class Meta:
        model = models.GoodImage
