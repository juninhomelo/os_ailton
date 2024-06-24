from django.contrib import admin
from service_orders.models import Brand, ServiceOrder


class BrandAdmin(admin.ModelAdmin):
    search_fields = ('name'),
    ordering = ['name']


class ServiceOrderAdmin(admin.ModelAdmin):
    ordering = ['id']
    autocomplete_fields = ['brand']
    

admin.site.register(Brand, BrandAdmin)
admin.site.register(ServiceOrder, ServiceOrderAdmin)
