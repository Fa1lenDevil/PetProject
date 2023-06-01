from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Pizza, Soup, Snack, Drinks


class MenuView(TemplateView):
    template_name = 'catalog/pizza.html'

    def get(self, request):
        pizzas = Pizza.objects.all()

        params = {
            'pizzas': pizzas
        }
        return render(request, self.template_name, params)


class SoupView(TemplateView):
    template_name = 'catalog/soup.html'

    def get(self, request):
        soups = Soup.objects.all()

        params = {
            'soups': soups
        }
        return render(request, self.template_name, params)