from django.shortcuts import render, redirect
from django.urls import reverse
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if not cart:
        return redirect('cart:cart_detail')  # Если корзина пустая, перенаправляем обратно

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            # Очистка корзины
            cart.clear()
            return redirect(reverse('orders:order_success', args=[order.id]))  # Перенаправление на страницу успеха
    else:
        form = OrderCreateForm()

    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})


def order_success(request, order_id):
    """Отображает страницу успешного заказа"""
    order = Order.objects.get(id=order_id)
    return render(request, 'orders/order/created.html', {'order': order})

