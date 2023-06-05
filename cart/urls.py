from django.contrib import admin
from django.urls import path
from .views import CartView, CartDetail


urlpatterns = [
    path('add/', CartView.as_view(), name='cart-add'),
    path('detail/', CartDetail.as_view(), name='cart-detail')
]
