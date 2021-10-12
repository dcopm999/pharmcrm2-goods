from django.forms import ModelForm

from goods import models


class TradeNameForm(ModelForm):
    class Meta:
        model = models.TradeName
        fields = ["name"]


class MakerForm(ModelForm):
    class Meta:
        model = models.Maker
        fields = ["name"]


class PackingForm(ModelForm):
    class Meta:
        model = models.Packing
        fields = ["name"]


class UnitForm(ModelForm):
    class Meta:
        model = models.Unit
        fields = ["name"]


class CatalogForm(ModelForm):
    class Meta:
        model = models.Catalog
        fields = ["name", "parent"]


class OriginalPackingForm(ModelForm):
    class Meta:
        model = models.OriginalPacking
        fields = ["packing", "quantity", "unit"]


class DosagePackingForm(ModelForm):
    class Meta:
        model = models.DosagePacking
        fields = ["packing", "quantity", "unit"]
