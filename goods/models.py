# -*- coding: utf-8 -*-
import reversion
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from mptt.models import MPTTModel, TreeForeignKey
from slugify import slugify
from sorl.thumbnail import ImageField


@reversion.register()
class TradeName(models.Model):
    name = models.CharField(max_length=250, unique=True, verbose_name=_("Name"))
    slug = models.SlugField(max_length=250, editable=False, verbose_name=_("slug"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))

    class Meta:
        ordering = ["-name"]
        verbose_name = _("Trade name")
        verbose_name_plural = _("Trade names")

    def get_absolute_url(self):
        return reverse("goods:tradename-detail", args=[str(self.slug)])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


@reversion.register()
class Maker(models.Model):
    name = models.CharField(max_length=250, unique=True, verbose_name=_("Name"))
    slug = models.SlugField(max_length=250, editable=False, verbose_name=_("slug"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))

    class Meta:
        ordering = ["-name"]
        verbose_name = _("Maker")
        verbose_name_plural = _("Makers")

    def get_absolute_url(self):
        return reverse("goods:maker-detail", args=[str(self.slug)])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


@reversion.register()
class Packing(models.Model):
    name = models.CharField(max_length=250, unique=True, verbose_name=_("Name"))
    slug = models.SlugField(max_length=250, editable=False, verbose_name=_("slug"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))

    class Meta:
        ordering = ["-name"]
        verbose_name = _("Packing type")
        verbose_name_plural = _("Packing types")

    def get_absolute_url(self):
        return reverse("goods:packing-detail", args=[str(self.slug)])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


@reversion.register()
class Unit(models.Model):
    name = models.CharField(max_length=250, unique=True, verbose_name=_("Name"))
    slug = models.SlugField(max_length=250, editable=False, verbose_name=_("slug"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))

    class Meta:
        ordering = ["-name"]
        verbose_name = _("Unit of measurement")
        verbose_name_plural = _("Units of measurement")

    def get_absolute_url(self):
        return reverse("goods:unit-detail", args=[str(self.slug)])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


@reversion.register()
class OriginalPacking(models.Model):
    packing = models.ForeignKey(
        Packing, on_delete=models.PROTECT, verbose_name=_("Packing type")
    )
    quantity = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Quantity")
    )
    unit = models.ForeignKey(
        Unit, on_delete=models.PROTECT, verbose_name=_("Unit of measurement")
    )
    slug = models.SlugField(
        max_length=250, blank=True, editable=False, verbose_name=_("slug")
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))

    def get_absolute_url(self):
        return reverse("goods:originalpacking-detail", args=[str(self.slug)])

    def __str__(self):
        return f"{self.packing} {self.quantity} {self.unit}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.__str__())
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ("packing", "quantity", "unit")
        verbose_name = _("Original Packing")
        verbose_name_plural = _("Original Packings")


@reversion.register()
class DosagePacking(models.Model):
    packing = models.ForeignKey(
        Packing, on_delete=models.PROTECT, verbose_name=_("Packing type")
    )
    quantity = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Quantity")
    )
    unit = models.ForeignKey(
        Unit, on_delete=models.PROTECT, verbose_name=_("Unit of measurement")
    )
    slug = models.SlugField(
        max_length=250, blank=True, editable=False, verbose_name=_("slug")
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))

    def get_absolute_url(self):
        return reverse("goods:dosagepacking-detail", args=[str(self.slug)])

    def __str__(self):
        return f"{self.packing} {self.quantity} {self.unit}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.__str__())
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ("packing", "quantity", "unit")
        verbose_name = _("Dosage packing")
        verbose_name_plural = _("Dosage packings")


@reversion.register()
class Catalog(MPTTModel):
    name = models.CharField(max_length=250, verbose_name=_("Name"))
    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name=_("children"),
    )
    slug = models.SlugField(
        max_length=250, blank=True, editable=False, verbose_name=_("slug")
    )
    created = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name=_("Created")
    )
    updated = models.DateTimeField(
        auto_now=True, editable=False, verbose_name=_("Updated")
    )

    class Meta:
        verbose_name_plural = _("Catalogs")
        verbose_name = _("Catalog")

    def get_absolute_url(self):
        return reverse("goods:catalog-detail", args=[str(self.slug)])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.__str__())
        super().save(*args, **kwargs)


@reversion.register()
class PharmProduct(models.Model):
    trade_name = models.ForeignKey(
        TradeName, on_delete=models.PROTECT, verbose_name=_("Trade name")
    )
    maker = models.ForeignKey(Maker, on_delete=models.PROTECT, verbose_name=_("Maker"))
    original_packing = models.ForeignKey(
        OriginalPacking, on_delete=models.PROTECT, verbose_name=_("Original packing")
    )
    dosage_packing = models.ForeignKey(
        DosagePacking,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Dosage packing"),
    )
    catalog = models.ForeignKey(
        Catalog, on_delete=models.PROTECT, verbose_name="Catalog"
    )
    slug = models.SlugField(
        max_length=250, blank=True, editable=False, verbose_name=_("slug")
    )
    full_name = models.CharField(
        max_length=300, blank=True, editable=False, verbose_name=_("Full name")
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))

    class Meta:
        unique_together = ("trade_name", "maker", "original_packing", "dosage_packing")
        verbose_name = _("Pharmaceutical product")
        verbose_name_plural = _("Pharmaceutical products")

    def get_absolute_url(self):
        return reverse("goods:pharmproduct-detail", args=[str(self.slug)])

    def __str__(self):
        result = f"{self.maker.name}: {self.trade_name.name}"
        if self.dosage_packing is not None:
            result += f", {self.dosage_packing}"
        if self.original_packing is not None:
            result += f", {self.original_packing}"
        return result

    def save(self, *args, **kwargs):
        self.slug = slugify(self.__str__())
        self.full_name = self.__str__()
        super().save(*args, **kwargs)


@reversion.register()
class PharmProductImage(models.Model):
    img = ImageField(upload_to="thumbnails", verbose_name=_("Image"))
    product_parent = models.ForeignKey(
        PharmProduct,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name=_("Parent"),
    )

    def __str__(self):
        return self.img.url
