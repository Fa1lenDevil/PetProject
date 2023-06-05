from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Product


class PizzaView(TemplateView):
    template_name = 'catalog/pizza.html'

    def get(self, request):
        products = Product.objects.filter(name__istartswith='Пицца')

        params = {
            'products': products
        }
        return render(request, self.template_name, params)

class SoupView(TemplateView):
    template_name = 'catalog/soup.html'

    def get(self, request):
        product = Product.objects.filter(name__istartswith='Суп')

        params = {
            'product': product
        }
        return render(request, self.template_name, params)\
