from django.contrib import admin
from .models import Pizza, Soup, Snack, Ingredients, Drinks


@admin.register(Ingredients)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'get_ingredients', 'weight', 'price', 'size')


@admin.register(Soup)
class SoupAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'get_ingredients', 'weight', 'price')
