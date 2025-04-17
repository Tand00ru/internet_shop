from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView

app_name = 'shop'

urlpatterns = [
    path('', views.main, name='main'),
    path('menu/', views.menu, name='menu'),
    path('menu/category/<slug:category_slug>/', views.menu, name='menu_by_category'),
    path('about/', views.about, name='about'),
    path('<int:id>/<slug:slug>/', views.cart, name='cart'),
    path('registration/', views.registration, name='registration'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)





