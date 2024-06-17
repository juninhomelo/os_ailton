from django.contrib import admin
from customers.models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone1',)
    search_fields = ('name',)


admin.site.register(Client, ClientAdmin)
