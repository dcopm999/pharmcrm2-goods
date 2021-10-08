# -*- coding: utf-8 -*-
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from reversion.admin import VersionAdmin
from sorl.thumbnail.admin import AdminImageMixin

from goods import models


class PharmProductImageInline(AdminImageMixin, admin.TabularInline):
    model = models.PharmProductImage


@admin.register(models.TradeName)
class TrandeNameAdmin(VersionAdmin):
    list_display = [
        "name",
    ]
    search_fields = ["name"]


@admin.register(models.Maker)
class MakerAdmin(VersionAdmin):
    list_display = [
        "name",
    ]
    search_fields = ["name"]


@admin.register(models.Packing)
class PackingAdmin(VersionAdmin):
    list_display = [
        "name",
    ]
    search_fields = ["name"]


@admin.register(models.OriginalPacking)
class OriginalPackingAdmin(VersionAdmin):
    list_display = ["packing", "quantity", "unit"]
    search_fields = ["name"]
    autocomplete_fields = ["unit"]


@admin.register(models.DosagePacking)
class DosagePackingAdmin(VersionAdmin):
    list_display = ["packing", "quantity", "unit"]


@admin.register(models.Unit)
class UnitAdmin(VersionAdmin):
    list_display = [
        "name",
    ]
    search_fields = ["name"]


@admin.register(models.Catalog)
class CatalogAdmin(VersionAdmin, MPTTModelAdmin):
    list_display = ["name", "updated", "created"]
    search_fields = ["name"]
    search_fields = [
        "name",
    ]


@admin.register(models.PharmProduct)
class PharmProductAdmin(VersionAdmin):
    inlines = [
        PharmProductImageInline,
    ]
    list_display = [
        "trade_name",
        "maker",
        "original_packing",
        "dosage_packing",
        "catalog",
    ]
    autocomplete_fields = ["trade_name", "maker", "catalog"]
    search_fields = [
        "trade_name__name",
        "full_name",
    ]
