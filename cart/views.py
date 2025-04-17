from .models import Cart
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = request.POST.get('quantity')

    if quantity and quantity.isdigit():
        quantity = int(quantity)
        if 1 <= quantity <= 100:
            cart.add(product=product, quantity=quantity, update_quantity=True)

    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def increase_item(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.increase_quantity(product)
    return redirect('cart:cart_detail')


def decrease_item(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.decrease_quantity(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})
