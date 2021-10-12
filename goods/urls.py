# -*- coding: utf-8 -*-
from django.urls import path

from goods import views

app_name = "goods"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("tradename/list/", views.TradeNameListView.as_view(), name="tradename-list"),
    path(
        "tradename/detail/<slug:slug>/",
        views.TradeNameDetailView.as_view(),
        name="tradename-detail",
    ),
    path(
        "tradename/create/",
        views.TradeNameCreateView.as_view(),
        name="tradename-create",
    ),
    path(
        "tradename/update/<slug:slug>/",
        views.TradeNameUpdateView.as_view(),
        name="tradename-update",
    ),
    path(
        "tradename/delete/<slug:slug>/",
        views.TradeNameDeleteView.as_view(),
        name="tradename-delete",
    ),
    path("maker/list/", views.MakerListView.as_view(), name="maker-list"),
    path(
        "maker/detail/<slug:slug>/",
        views.MakerDetailView.as_view(),
        name="maker-detail",
    ),
    path("maker/create/", views.MakerCreateView.as_view(), name="maker-create"),
    path(
        "maker/update/<slug:slug>/",
        views.MakerUpdateView.as_view(),
        name="maker-update",
    ),
    path(
        "maker/delete/<slug:slug>/",
        views.MakerDeleteView.as_view(),
        name="maker-delete",
    ),
    path("packing/list/", views.PackingListView.as_view(), name="packing-list"),
    path(
        "packing/detail/<slug:slug>/",
        views.PackingDetailView.as_view(),
        name="packing-detail",
    ),
    path("packing/create/", views.PackingCreateView.as_view(), name="packing-create"),
    path(
        "packing/update/<slug:slug>/",
        views.PackingUpdateView.as_view(),
        name="packing-update",
    ),
    path(
        "packing/delete/<slug:slug>/",
        views.PackingDeleteView.as_view(),
        name="packing-delete",
    ),
    path("unit/list/", views.UnitListView.as_view(), name="unit-list"),
    path(
        "unit/detail/<slug:slug>/", views.UnitDetailView.as_view(), name="unit-detail"
    ),
    path("unit/create/", views.UnitCreateView.as_view(), name="unit-create"),
    path(
        "unit/update/<slug:slug>/", views.UnitUpdateView.as_view(), name="unit-update"
    ),
    path(
        "unit/delete/<slug:slug>/", views.UnitDeleteView.as_view(), name="unit-delete"
    ),
    path("catalog/list/", views.CatalogListView.as_view(), name="catalog-list"),
    path(
        "catalog/detail/<slug:slug>/",
        views.CatalogDetailView.as_view(),
        name="catalog-detail",
    ),
    path("catalog/create/", views.CatalogCreateView.as_view(), name="catalog-create"),
    path(
        "catalog/update/<slug:slug>/",
        views.CatalogUpdateView.as_view(),
        name="catalog-update",
    ),
    path(
        "catalog/delete/<slug:slug>/",
        views.CatalogDeleteView.as_view(),
        name="catalog-delete",
    ),
    path(
        "originalpacking/list/",
        views.OriginalPackingListView.as_view(),
        name="originalpacking-list",
    ),
    path(
        "originalpacking/detail/<slug:slug>/",
        views.OriginalPackingDetailView.as_view(),
        name="originalpacking-detail",
    ),
    path(
        "originalpacking/create/",
        views.OriginalPackingCreateView.as_view(),
        name="originalpacking-create",
    ),
    path(
        "originalpacking/update/<slug:slug>/",
        views.OriginalPackingUpdateView.as_view(),
        name="originalpacking-update",
    ),
    path(
        "originalpacking/delete/<slug:slug>/",
        views.OriginalPackingDeleteView.as_view(),
        name="originalpacking-delete",
    ),
    path(
        "dosagepacking/list/",
        views.DosagePackingListView.as_view(),
        name="dosagepacking-list",
    ),
    path(
        "dosagepacking/detail/<slug:slug>/",
        views.DosagePackingDetailView.as_view(),
        name="dosagepacking-detail",
    ),
    path(
        "dosagepacking/create/",
        views.DosagePackingCreateView.as_view(),
        name="dosagepacking-create",
    ),
    path(
        "dosagepacking/update/<slug:slug>/",
        views.DosagePackingUpdateView.as_view(),
        name="dosagepacking-update",
    ),
    path(
        "dosagepacking/delete/<slug:slug>/",
        views.DosagePackingDeleteView.as_view(),
        name="dosagepacking-delete",
    ),
    path(
        "pharmproduct/list/",
        views.PharmProductListView.as_view(),
        name="pharmproduct-list",
    ),
    path(
        "pharmproduct/detail/<slug:slug>/",
        views.PharmProductDetailView.as_view(),
        name="pharmproduct-detail",
    ),
    path(
        "pharmproduct/create/",
        views.PharmProductCreateView.as_view(),
        name="pharmproduct-create",
    ),
    path(
        "pharmproduct/update/<slug:slug>/",
        views.PharmProductUpdateView.as_view(),
        name="pharmproduct-update",
    ),
    path(
        "pharmproduct/delete/<slug:slug>/",
        views.PharmProductDeleteView.as_view(),
        name="pharmproduct-delete",
    ),
]
