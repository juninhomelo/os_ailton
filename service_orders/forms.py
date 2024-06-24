from django.contrib.admin.widgets import AutocompleteSelect
from django import forms
from customers.admin import admin
from service_orders.models import ServiceOrder


class ServiceOrderModelForm(forms.ModelForm):

    class Meta:
        model = ServiceOrder
        fields = '__all__'
        widgets = {
            'client': AutocompleteSelect(
                ServiceOrder._meta.get_field('client').remote_field, 
                admin.site, 
                attrs={'placeholder': 'Nome...'},
            )
        }
