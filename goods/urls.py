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
]
