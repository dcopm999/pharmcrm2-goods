from django.forms import ModelForm

from goods import models


class TradeNameForm(ModelForm):
    class Meta:
        model = models.TradeName
        fields = ["name"]
