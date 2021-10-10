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
        "tradename/update/<slug:slug>",
        views.TradeNameUpdateView.as_view(),
        name="tradename-update",
    ),
    path(
        "tradename/delete/<slug:slug>",
        views.TradeNameDeleteView.as_view(),
        name="tradename-delete",
    ),
]
