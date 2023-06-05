from django.db import models
from django.contrib.auth.models import User
from menu.models import Product

class Cart(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="cart")
    products = models.ManyToManyField(Product, blank=True)

    def get_total_price(self):
        return sum([product.price for product in self.products.all()])

    def get_total_quantity(self):
        return len([product for product in self.products.all()])

    def display_products(self):
        return ", ".join([product.name for product in self.products.all()])