from django.contrib import admin
from django.urls import path
from .views import PizzaView, SoupView

urlpatterns = [
    path('', PizzaView.as_view(), name="menu-index"),
    path('soup/', SoupView.as_view(), name="menu-soup"),
]
