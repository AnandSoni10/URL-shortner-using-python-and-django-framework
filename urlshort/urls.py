from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from .views import home, createShortURL, redirect

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
    path("create/", createShortURL, name = 'create'),
    path("<str:url>", redirect, name = 'redirect')
]
