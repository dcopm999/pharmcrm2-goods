# -*- coding: utf-8 -*-
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from sorl.thumbnail.admin import AdminImageMixin

from goods import models


class PharmProductImageInline(AdminImageMixin, admin.TabularInline):
    model = models.PharmProductImage


@admin.register(models.TradeName)
class TrandeNameAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]
    search_fields = ["name"]


@admin.register(models.Maker)
class MakerAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]
    search_fields = ["name"]


@admin.register(models.Packing)
class PackingAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]
    search_fields = ["name"]


@admin.register(models.OriginalPacking)
class OriginalPackingAdmin(admin.ModelAdmin):
    list_display = ["packing", "quantity", "unit"]
    search_fields = ["name"]
    autocomplete_fields = ["unit"]


@admin.register(models.DosagePacking)
class DosagePackingAdmin(admin.ModelAdmin):
    list_display = ["packing", "quantity", "unit"]


@admin.register(models.Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]
    search_fields = ["name"]


@admin.register(models.Catalog)
class CatalogAdmin(MPTTModelAdmin):
    list_display = ["name", "updated", "created"]
    search_fields = ["name"]
    search_fields = [
        "name",
    ]


@admin.register(models.PharmProduct)
class PharmProductAdmin(admin.ModelAdmin):
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
