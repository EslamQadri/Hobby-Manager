"""
URL configuration for hobbymanager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, re_path

from hobby.ipfile import get_client_ip
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("know", get_client_ip),
    path("admin/", admin.site.urls),
    path("hobby/", include("hobby.urls")),
    path("user/", include("users.urls")),
    path("api/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(),
        name="swagger-ui",
    ),
    path(
        "",
        SpectacularSwaggerView.as_view(),
        name="swagger-ui",
    ),
    path("__debug__/", include("debug_toolbar.urls")),
]
