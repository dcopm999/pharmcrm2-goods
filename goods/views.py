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


class MakerListView(mixins.PermissionRequiredMixin, generic.ListView):
    permission_required = "goods.view_maker"
    model = models.Maker


class MakerDetailView(mixins.PermissionRequiredMixin, generic.DetailView):
    permission_required = "goods.view_maker"
    model = models.Maker


class MakerCreateView(mixins.PermissionRequiredMixin, generic.CreateView):
    permission_required = "goods.add_maker"
    model = models.Maker
    form_class = forms.MakerForm
    success_url = reverse_lazy("goods:maker-list")


class MakerUpdateView(mixins.PermissionRequiredMixin, generic.UpdateView):
    permission_required = "goods.change_maker"
    model = models.Maker
    form_class = forms.MakerForm

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy("goods:maker-detail", kwargs={"slug": self.object.slug})


class MakerDeleteView(mixins.PermissionRequiredMixin, generic.DeleteView):
    permission_required = "goods.delete_maker"
    model = models.Maker
    success_url = reverse_lazy("goods:maker-list")


class PackingListView(mixins.PermissionRequiredMixin, generic.ListView):
    permission_required = "goods.view_packing"
    model = models.Packing


class PackingDetailView(mixins.PermissionRequiredMixin, generic.DetailView):
    permission_required = "goods.view_packing"
    model = models.Packing


class PackingCreateView(mixins.PermissionRequiredMixin, generic.CreateView):
    permission_required = "goods.add_packing"
    model = models.Packing
    form_class = forms.PackingForm
    success_url = reverse_lazy("goods:packing-list")


class PackingUpdateView(mixins.PermissionRequiredMixin, generic.UpdateView):
    permission_required = "goods.change_packing"
    model = models.Packing
    form_class = forms.PackingForm

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy("goods:packing-detail", kwargs={"slug": self.object.slug})


class PackingDeleteView(mixins.PermissionRequiredMixin, generic.DeleteView):
    permission_required = "goods.delete_packing"
    model = models.Packing
    success_url = reverse_lazy("goods:packing-list")


class UnitListView(mixins.PermissionRequiredMixin, generic.ListView):
    permission_required = "goods.view_unit"
    model = models.Unit


class UnitDetailView(mixins.PermissionRequiredMixin, generic.DetailView):
    permission_required = "goods.view_unit"
    model = models.Unit


class UnitCreateView(mixins.PermissionRequiredMixin, generic.CreateView):
    permission_required = "goods.add_unit"
    model = models.Unit
    form_class = forms.UnitForm
    success_url = reverse_lazy("goods:unit-list")


class UnitUpdateView(mixins.PermissionRequiredMixin, generic.UpdateView):
    permission_required = "goods.change_unit"
    model = models.Unit
    form_class = forms.UnitForm

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy("goods:unit-detail", kwargs={"slug": self.object.slug})


class UnitDeleteView(mixins.PermissionRequiredMixin, generic.DeleteView):
    permission_required = "goods.delete_unit"
    model = models.Unit
    success_url = reverse_lazy("goods:unit-list")
