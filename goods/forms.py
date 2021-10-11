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
