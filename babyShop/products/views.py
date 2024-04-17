from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from .models import Product
from babyShop.cart.models import Cart, CartItem

# Create your views here.


class HomeView(TemplateView):
    template_name = 'common/index.html'


def products_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    products = Product.objects.all()
    return render(request, 'products/product_detail.html', {'product': product, 'products': products})


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('product_detail', product_id=product_id)
