from django import forms
from service_orders.models import ServiceOrder


class ServiceOrderModelForm(forms.ModelForm):

    class Meta:
        model = ServiceOrder
        fields = '__all__'
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
            'phone1': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'model_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'plate': forms.TextInput(attrs={'class': 'form-control'}),
            'services': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'products': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'finished_at': forms.DateInput(),
            'total': forms.NumberInput(),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'comments': forms.Textarea({'rows':'3'}),            
        }
        labels = {
            'client': 'Cliente',
            'phone1': 'Telefone',
            'model': 'Modelo',
            'model_year': 'Ano Modelo',
            'plate': 'Placa',
            'services': 'Serviços',
            'products': 'Produtos',
            'finished_at': 'Data Término',
            'total': 'Valor Total',
            'status': 'Status',
            'comments': 'Observações',
        }
