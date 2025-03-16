# filepath: c:\podval1\QRcrayfish\QRcrayfish\urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("app/", include("app.urls")),
    path("", include("app.urls")),  # Добавлено для корневого URL
]
