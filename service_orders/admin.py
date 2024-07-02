from django.contrib import admin
from service_orders.models import Brand, ServiceOrder


class ServiceOrderAdmin(admin.ModelAdmin):
    ordering = ['id']


class BrandAdmin(admin.ModelAdmin):
    search_fields = ['name']
    ordering = ['name']
  

admin.site.register(Brand, BrandAdmin)
admin.site.register(ServiceOrder, ServiceOrderAdmin)
