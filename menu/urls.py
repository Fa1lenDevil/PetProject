from django.contrib import admin
from django.urls import path
from .views import MenuView, SoupView

urlpatterns = [
    path('', MenuView.as_view(), name="menu-index"),
    path('Soup', SoupView.as_view(), name="soup-menu")
]
