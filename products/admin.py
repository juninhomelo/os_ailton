from django.contrib import admin
from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'quantity',)
    search_fields = ('name',)


admin.site.register(Product, ProductAdmin)
