# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin
from django.urls import include, path
from drf_spectacular import views as specta_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("goods.urls", namespace="goods")),
    path("api/", include("goods.api.urls", namespace="goods-api")),
    path("api/schema/", specta_views.SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        specta_views.SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger",
    ),
]
