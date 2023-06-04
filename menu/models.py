from django.db import models
from django.urls import reverse

class Ingredients(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(default=None)
    ingredient = models.ManyToManyField(Ingredients)
    weight = models.IntegerField()
    price = models.DecimalField(max_digits=3, decimal_places=1)
    size = models.IntegerField(null=True, default=None)

    def __str__(self):
        return self.name

    def get_ingredients(self):
        return ", ".join([ingredient.name for ingredient in self.ingredient.all()])

    get_ingredients.short_description = "Ingredients"
