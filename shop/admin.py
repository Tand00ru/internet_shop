from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
            'name', 'slug',
            'description', 'image'
                   ]
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display =[
        'name', 'slug',
        'price', 'currency',
        'quantity', 'measurement',
        'stock', 'available',
        'created', 'updated',
        'is_new'
                  ]
    list_filter = ['available', 'created', 'updated', 'is_new']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)


