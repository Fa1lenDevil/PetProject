from django.db import models

class Ingredients(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(default=None)
    ingredient = models.ManyToManyField(Ingredients)
    weight = models.IntegerField()
    price = models.DecimalField(max_digits=3, decimal_places=1)
    size = models.IntegerField()

    def __str__(self):
        return self.name

    def get_ingredients(self):
        return ", ".join([ingredient.name for ingredient in self.ingredient.all()])

    get_ingredients.short_description = "Ingredients"


class Snack(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(default=None)
    ingredient = models.ManyToManyField(Ingredients)
    weight = models.IntegerField()
    price = models.DecimalField(max_digits=3, decimal_places=1)


class Soup(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(default=None)
    ingredient = models.ManyToManyField(Ingredients)
    weight = models.IntegerField()
    price = models.DecimalField(max_digits=3, decimal_places=1)

    def get_ingredients(self):
        return ", ".join([ingredient.name for ingredient in self.ingredient.all()])
    get_ingredients.short_description = "Ingredients"


class Drinks(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(default=None)
    price = models.DecimalField(max_digits=3, decimal_places=1)
