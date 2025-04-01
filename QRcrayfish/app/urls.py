from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("generate_qr/", views.generate_qr, name="generate_qr"),
]
