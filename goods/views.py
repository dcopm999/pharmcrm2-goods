from django.contrib.auth import mixins
from django.urls import reverse_lazy
from django.views import generic

from goods import forms, models


class HomeView(mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = "goods/base.html"


class TradeNameListView(mixins.PermissionRequiredMixin, generic.ListView):
    permission_required = "goods.view_tradename"
    model = models.TradeName


class TradeNameDetailView(mixins.PermissionRequiredMixin, generic.DetailView):
    permission_required = "goods.view_tradename"
    model = models.TradeName


class TradeNameCreateView(mixins.PermissionRequiredMixin, generic.CreateView):
    permission_required = "goods.add_tradename"
    model = models.TradeName
    form_class = forms.TradeNameForm
    success_url = reverse_lazy("goods:tradename-list")


class TradeNameUpdateView(mixins.PermissionRequiredMixin, generic.UpdateView):
    permission_required = "goods.change_tradename"
    model = models.TradeName
    form_class = forms.TradeNameForm

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy("goods:tradename-detail", kwargs={"slug": self.object.slug})


class TradeNameDeleteView(mixins.PermissionRequiredMixin, generic.DeleteView):
    permission_required = "goods.delete_tradename"
    model = models.TradeName
    success_url = reverse_lazy("goods:tradename-list")
