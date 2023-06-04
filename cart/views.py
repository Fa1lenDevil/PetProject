from django.shortcuts import redirect
from cart.models import Cart
from menu.models import Product
from django.views.generic import RedirectView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class CartView(RedirectView):

    def get(self, request):
        return redirect('menu-index')

    @method_decorator(login_required)
    def post(self, request):
        product = Product.objects.get(id=request.POST['product_id'])
        cart = Cart.objects.get(user=request.user)
        cart.products.add(product)

        return redirect('menu-index')
