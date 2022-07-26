from rest_framework.permissions import DjangoObjectPermissions
from rest_framework.viewsets import ModelViewSet

from goods import models
from goods.api import serializers


class TradeNameViewSet(ModelViewSet):
    queryset = models.TradeName.objects.all()
    serializer_class = serializers.TradeNameSerializer
    permission_class = [DjangoObjectPermissions]


class MakerViewSet(ModelViewSet):
    queryset = models.Maker.objects.all()
    serializer_class = serializers.MakerSerializer
    permission_class = [DjangoObjectPermissions]


class PackingViewSet(ModelViewSet):
    queryset = models.Packing.objects.all()
    serializer_class = serializers.PackingSerializer
    permission_class = [DjangoObjectPermissions]


class UnitViewSet(ModelViewSet):
    queryset = models.Unit.objects.all()
    serializer_class = serializers.UnitSerializer
    permission_class = [DjangoObjectPermissions]


class OriginalPackingViewSet(ModelViewSet):
    queryset = models.OriginalPacking.objects.all()
    serializer_class = serializers.OriginalPackingSerializer
    permission_class = [DjangoObjectPermissions]


class DosagePackingViewSet(ModelViewSet):
    queryset = models.DosagePacking.objects.all()
    serializer_class = serializers.DosagePackingSerializer
    permission_class = [DjangoObjectPermissions]


class CatalogViewSet(ModelViewSet):
    queryset = models.Catalog.objects.all()
    serializer_class = serializers.CatalogSerializer
    permission_class = [DjangoObjectPermissions]


class GoodViewSet(ModelViewSet):
    queryset = models.Good.objects.all()
    serializer_class = serializers.GoodSerializer
    permission_class = [DjangoObjectPermissions]


class GoodImageViewSet(ModelViewSet):
    queryset = models.GoodImage.objects.all()
    serializer_class = serializers.GoodImageSerializer
    permission_class = [DjangoObjectPermissions]
