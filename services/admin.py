from django.contrib import admin
from services.models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)
    search_fields = ('name',)

admin.site.register(Service, ServiceAdmin)
