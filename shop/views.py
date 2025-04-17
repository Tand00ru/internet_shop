from django.shortcuts import render, get_object_or_404
from .models import Category, Product
import random
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages

def main(request):
    return render(request,
                  'shop/main.html')

def menu(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    query = request.GET.get('q')

    if query:
        products = products.filter(name__icontains=query)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    else:
        category = None

    new_products = list(products)
    random.shuffle(new_products)
    new_products = new_products[:3]

    context = {
        'products': products,
        'new_products': new_products,
        'categories': categories,
        'category': category,
        'query': query,
    }

    return render(request, 'shop/menu.html', context)



def about(request):
    return render(request,
                  'shop/about.html')

def cart(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    return render(request, 'shop/cart.html', {'product': product})

def registration(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        # Проверка: пароли совпадают?
        if password != password2:
            return render(request, "users/registration.html",
                          {"error": "Passwords do not match!"})

        # Проверка: существует ли пользователь?
        if User.objects.filter(username=username).exists():
            return render(request, "users/registration.html",
                          {"error": "User already exists!"})

        if len(password) < 4 or len(password) > 16:
            return render(request, "users/registration.html",
                          {"error": "Password must be between 4 and 16 characters long!"})

        answer = any([i in ("*", "&", "{", "}", "|", "+") for i in password])

        if answer:
            return render(request, "users/registration.html",
                          {"error": "Password must not contain the following characters: * & { } | +"})

        if password.lower() == password:
            return render(request, "users/registration.html",
                          {"error": "Password must contain capital letters"})

        answer = any([i in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9') for i in password])

        if answer == False:
            return render(request, "users/registration.html",
                          {"error": "Password must contain numbers"})

        # Создание пользователя вручную
        user = User.objects.create(username=username, email=email, password=make_password(password))
        login(request, user)  # Автовход после регистрации
        return redirect("shop:main")
    return render(request,
                  'users/registration.html')


class CustomLoginView(LoginView):
    template_name = "users/login.html"

    def form_invalid(self, form):
        messages.error(self.request, "Login error: Incorrect username or password.")
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy("shop:main")