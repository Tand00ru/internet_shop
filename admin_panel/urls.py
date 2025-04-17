from django.urls import path
from . import views

urlpatterns = [
    # Управление категориями
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/update/<int:pk>/', views.category_update, name='category_update'),
    path('categories/delete/<int:pk>/', views.category_delete, name='category_delete'),

    # Управление товарами
    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/update/<int:pk>/', views.product_update, name='product_update'),
    path('products/delete/<int:pk>/', views.product_delete, name='product_delete'),

    # Управление заказами
    path('orders/', views.order_list, name='order_list'),
    path('orders/create/', views.order_create, name='order_create'),
    path('orders/detail/<int:pk>/', views.order_detail, name='order_detail'),
    path('orders/update/<int:pk>/', views.order_update, name='order_update'),
    path('orders/delete/<int:pk>/', views.order_delete, name='order_delete'),

    # Управление позициями заказа
    path('orderitems/', views.orderitem_list, name='orderitem_list'),
    path('orderitems/update/<int:pk>/', views.orderitem_update, name='orderitem_update'),
    path('orderitems/delete/<int:pk>/', views.orderitem_delete, name='orderitem_delete'),
]
