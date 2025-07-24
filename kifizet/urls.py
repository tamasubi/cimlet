# penz/urls.py
from django.urls import path
from .views import penz_view

urlpatterns = [
    path('', penz_view, name="penz_view"),
]