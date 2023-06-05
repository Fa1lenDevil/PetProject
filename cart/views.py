from django.shortcuts import redirect, render
from cart.models import Cart
from menu.models import Product
from django.views.generic import RedirectView, TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


class CartView(RedirectView):

    def get(self, request):
        return redirect('menu-index')

    @method_decorator(login_required)
    def post(self, request):
        product = Product.objects.get(id=request.POST['product_id'])
        cart = Cart.objects.get(user=request.user)
        cart.products.add(product)

        return redirect('menu-index')


class CartDeleteView(RedirectView):

    def get(self, request):
        return redirect('menu-index')

    @method_decorator(login_required)
    def post(self, request):
        product = Product.objects.get(id=request.POST['product_id'])
        cart = Cart.objects.get(user=request.user)
        cart.products.remove(product)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

class CartDetail(TemplateView):
    template_name = 'catalog/cart.html'

    def get(self, request):
        cartdetail = Cart.objects.all()
        params = {
            'cartdetail': cartdetail
        }

        return render(request, self.template_name, params)
