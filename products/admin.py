from django.contrib import admin
from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'formatted_price', 'quantity',)
    search_fields = ('name',)
    def formatted_price(self, obj):
        if obj.price is not None:
            return f"R$ {obj.price:.2f}"
        return "R$ 0.00"  # ou outro valor padrão
    formatted_price.short_description = 'Preço'

    readonly_fields = ('formatted_price',)  # Apenas leitura no formulário de detalhe


admin.site.register(Product, ProductAdmin)
