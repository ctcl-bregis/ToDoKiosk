# ToDoKiosk - CTCL 2023
# File: app/urls.py
# Purpose: App URLs
# Created: October 31, 2023
# Modified: October 31, 2023

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("main.urls")),
]
