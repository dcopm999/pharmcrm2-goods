from rest_framework import serializers

from goods import models


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Catalog
        fields = "__all__"


class TradeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TradeName
        fields = "__all__"


class MakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Maker
        fields = "__all__"


class PackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Packing
        fields = "__all__"


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Unit
        fields = "__all__"


class OriginalPackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OriginalPacking
        fields = "__all__"


class DosagePackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DosagePacking
        fields = "__all__"


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Good
        fields = "__all__"


class GoodImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GoodImage
        fields = "__all__"
