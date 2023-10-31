# ToDoKiosk - CTCL 2023
# File: main/urls.py
# Purpose: Main app URLs
# Created: October 31, 2023
# Modified: October 31, 2023

from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.main),
]