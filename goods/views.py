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


class CatalogListView(mixins.PermissionRequiredMixin, generic.ListView):
    permission_required = "goods.view_catalog"
    model = models.Catalog


class CatalogDetailView(mixins.PermissionRequiredMixin, generic.DetailView):
    permission_required = "goods.view_catalog"
    model = models.Catalog


class CatalogCreateView(mixins.PermissionRequiredMixin, generic.CreateView):
    permission_required = "goods.add_Catalog"
    model = models.Catalog
    form_class = forms.CatalogForm
    success_url = reverse_lazy("goods:catalog-list")


class CatalogUpdateView(mixins.PermissionRequiredMixin, generic.UpdateView):
    permission_required = "goods.change_catalog"
    model = models.Catalog
    form_class = forms.CatalogForm

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy("goods:catalog-detail", kwargs={"slug": self.object.slug})


class CatalogDeleteView(mixins.PermissionRequiredMixin, generic.DeleteView):
    permission_required = "goods.delete_catalog"
    model = models.Catalog
    success_url = reverse_lazy("goods:catalog-list")


class OriginalPackingListView(mixins.PermissionRequiredMixin, generic.ListView):
    permission_required = "goods.view_originalpacking"
    model = models.OriginalPacking


class OriginalPackingDetailView(mixins.PermissionRequiredMixin, generic.DetailView):
    permission_required = "goods.view_originalpacking"
    model = models.OriginalPacking


class OriginalPackingCreateView(mixins.PermissionRequiredMixin, generic.CreateView):
    permission_required = "goods.add_originalpacking"
    model = models.OriginalPacking
    form_class = forms.OriginalPackingForm
    success_url = reverse_lazy("goods:originalpacking-list")


class OriginalPackingUpdateView(mixins.PermissionRequiredMixin, generic.UpdateView):
    permission_required = "goods.change_originalpacking"
    model = models.OriginalPacking
    form_class = forms.OriginalPackingForm

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy(
            "goods:originalpacking-detail", kwargs={"slug": self.object.slug}
        )


class OriginalPackingDeleteView(mixins.PermissionRequiredMixin, generic.DeleteView):
    permission_required = "goods.delete_originalpacking"
    model = models.OriginalPacking
    success_url = reverse_lazy("goods:originalpacking-list")


class DosagePackingListView(mixins.PermissionRequiredMixin, generic.ListView):
    permission_required = "goods.view_dosagepacking"
    model = models.DosagePacking


class DosagePackingDetailView(mixins.PermissionRequiredMixin, generic.DetailView):
    permission_required = "goods.view_dosagepacking"
    model = models.DosagePacking


class DosagePackingCreateView(mixins.PermissionRequiredMixin, generic.CreateView):
    permission_required = "goods.add_dosagepacking"
    model = models.DosagePacking
    form_class = forms.DosagePackingForm
    success_url = reverse_lazy("goods:dosagepacking-list")


class DosagePackingUpdateView(mixins.PermissionRequiredMixin, generic.UpdateView):
    permission_required = "goods.change_dosagepacking"
    model = models.DosagePacking
    form_class = forms.DosagePackingForm

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy(
            "goods:dosagepacking-detail", kwargs={"slug": self.object.slug}
        )


class DosagePackingDeleteView(mixins.PermissionRequiredMixin, generic.DeleteView):
    permission_required = "goods.delete_dosagepacking"
    model = models.DosagePacking
    success_url = reverse_lazy("goods:dosagepacking-list")


class PharmProductListView(mixins.PermissionRequiredMixin, generic.ListView):
    permission_required = "goods.view_pharmproduct"
    model = models.PharmProduct


class PharmProductDetailView(mixins.PermissionRequiredMixin, generic.DetailView):
    permission_required = "goods.view_pharmproduct"
    model = models.PharmProduct


class PharmProductCreateView(mixins.PermissionRequiredMixin, generic.CreateView):
    permission_required = "goods.add_pharmproduct"
    model = models.PharmProduct
    form_class = forms.PharmProductForm
    success_url = reverse_lazy("goods:pharmproduct-list")


class PharmProductUpdateView(mixins.PermissionRequiredMixin, generic.UpdateView):
    permission_required = "goods.change_pharmproduct"
    model = models.PharmProduct
    form_class = forms.PharmProductForm

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy(
            "goods:pharmproduct-detail", kwargs={"slug": self.object.slug}
        )


class PharmProductDeleteView(mixins.PermissionRequiredMixin, generic.DeleteView):
    permission_required = "goods.delete_pharmproduct"
    model = models.PharmProduct
    success_url = reverse_lazy("goods:pharmproduct-list")
