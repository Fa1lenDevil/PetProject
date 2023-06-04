from django.contrib import admin
from .models import Product, Ingredients
from cart.models import Cart


@admin.register(Ingredients)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'get_ingredients', 'weight', 'price', 'size')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'display_products', 'get_total_price', 'get_total_quantity')
