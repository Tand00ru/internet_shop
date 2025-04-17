from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from shop.models import Product, Category
from orders.models import Order, OrderItem
from .forms import OrderForm, OrderItemFormSet, OrderItemForm

def is_staff(user):
    return user.is_authenticated and user.is_staff

# ========================================
# Управление категориями
# ========================================

@user_passes_test(is_staff)
def category_list(request):
    sort = request.GET.get('sort', 'name')
    query = request.GET.get('q')
    categories = Category.objects.all()

    if query:
        categories = categories.filter(name__icontains=query)

    categories = categories.order_by(sort)
    return render(request, 'admin_panel/tables/category/category_list.html', {'categories': categories})


@user_passes_test(is_staff)
def category_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        slug = request.POST.get('slug')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        Category.objects.create(name=name, slug=slug, description=description, image=image)
        return redirect('category_list')
    return render(request, 'admin_panel/tables/category/category_form.html')

@user_passes_test(is_staff)
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.name = request.POST.get('name')
        category.slug = request.POST.get('slug')
        category.description = request.POST.get('description')
        if 'image' in request.FILES:
            category.image = request.FILES.get('image')
        category.save()
        return redirect('category_list')
    return render(request, 'admin_panel/tables/category/category_form.html', {'category': category})

@user_passes_test(is_staff)
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('category_list')

@user_passes_test(is_staff)
def product_list(request):
    sort = request.GET.get('sort', 'name')
    query = request.GET.get('q')
    products = Product.objects.all()

    if query:
        products = products.filter(name__icontains=query)

    products = products.order_by(sort)
    return render(request, 'admin_panel/tables/product/product_list.html', {'products': products})


@user_passes_test(is_staff)
def product_create(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        slug = request.POST.get('slug')
        category_id = request.POST.get('category')
        description = request.POST.get('description')
        price = request.POST.get('price')
        currency = request.POST.get('currency')
        quantity = request.POST.get('quantity')
        measurement = request.POST.get('measurement')
        stock = request.POST.get('stock')
        available = request.POST.get('available') == 'on'
        is_new = request.POST.get('is_new') == 'on'
        image = request.FILES.get('image')
        category = Category.objects.get(id=category_id)

        Product.objects.create(
            name=name,
            slug=slug,
            category=category,
            description=description,
            price=price,
            currency=currency,
            quantity=quantity,
            measurement=measurement,
            stock=stock,
            available=available,
            is_new=is_new,
            image=image
        )
        return redirect('product_list')
    return render(request, 'admin_panel/tables/product/product_form.html', {'categories': categories})

@user_passes_test(is_staff)
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    categories = Category.objects.all()
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.slug = request.POST.get('slug')
        category_id = request.POST.get('category')
        product.description = request.POST.get('description')
        product.price = request.POST.get('price')
        product.currency = request.POST.get('currency')
        product.quantity = request.POST.get('quantity')
        product.measurement = request.POST.get('measurement')
        product.stock = request.POST.get('stock')
        product.available = request.POST.get('available') == 'on'
        product.is_new = request.POST.get('is_new') == 'on'
        if 'image' in request.FILES:
            product.image = request.FILES.get('image')
        product.category = Category.objects.get(id=category_id)
        product.save()
        return redirect('product_list')
    return render(request, 'admin_panel/tables/product/product_form.html', {'product': product, 'categories': categories})

@user_passes_test(is_staff)
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('product_list')

@user_passes_test(is_staff)
def order_list(request):
    sort = request.GET.get('sort', 'user__username')
    query = request.GET.get('q')
    orders = Order.objects.all()

    if query:
        orders = orders.filter(user__username__icontains=query)

    orders = orders.order_by(sort)
    return render(request, 'admin_panel/tables/order/order_list.html', {'orders': orders})


@user_passes_test(is_staff)
def order_create(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save()
            formset = OrderItemFormSet(request.POST, instance=order)
            if formset.is_valid():
                formset.save()
                return redirect('order_detail', pk=order.pk)
        else:
            formset = OrderItemFormSet(request.POST)
    else:
        order_form = OrderForm()
        formset = OrderItemFormSet()
    return render(request, 'admin_panel/tables/order/order_form.html', {'order_form': order_form, 'formset': formset})

@user_passes_test(is_staff)
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    orderitems = order.items.all()
    return render(request, 'admin_panel/tables/order/order_detail.html', {'order': order, 'orderitems': orderitems})

@user_passes_test(is_staff)
def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order_form = OrderForm(request.POST, instance=order)
        formset = OrderItemFormSet(request.POST, instance=order)
        if order_form.is_valid() and formset.is_valid():
            order_form.save()
            formset.save()
            return redirect('order_detail', pk=order.pk)
    else:
        order_form = OrderForm(instance=order)
        formset = OrderItemFormSet(instance=order)
    return render(request, 'admin_panel/tables/order/order_form.html', {'order_form': order_form, 'formset': formset})

@user_passes_test(is_staff)
def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return redirect('order_list')

@user_passes_test(is_staff)
def orderitem_list(request):
    sort = request.GET.get('sort', 'product__name')
    query = request.GET.get('q')
    orderitems = OrderItem.objects.all()

    if query:
        orderitems = orderitems.filter(product__name__icontains=query)

    orderitems = orderitems.order_by(sort)
    return render(request, 'admin_panel/tables/orderitem/orderitem_list.html', {'orderitems': orderitems})


@user_passes_test(is_staff)
def orderitem_update(request, pk):
    orderitem = get_object_or_404(OrderItem, pk=pk)
    if request.method == 'POST':
        form = OrderItemForm(request.POST, instance=orderitem)
        if form.is_valid():
            form.save()
            return redirect('orderitem_list')
    else:
        form = OrderItemForm(instance=orderitem)
    return render(request, 'admin_panel/tables/orderitem/orderitem_form.html', {'form': form})

@user_passes_test(is_staff)
def orderitem_delete(request, pk):
    orderitem = get_object_or_404(OrderItem, pk=pk)
    orderitem.delete()
    return redirect('orderitem_list')
