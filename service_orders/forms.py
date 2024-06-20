from django import forms
from service_orders.models import ServiceOrder


class ServiceOrderModelForm(forms.ModelForm):
    #client = forms.CharField(max_length=100)

    class Meta:
        model = ServiceOrder
        fields = '__all__'
