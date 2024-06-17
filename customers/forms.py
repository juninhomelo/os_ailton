from django import forms
from customers.models import Client


class ClientModelForm(forms.ModelForm):

    class Meta:    
        model = Client
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'address_number': forms.TextInput(attrs={'class': 'form-control'}),
            'phone1': forms.TextInput(attrs={'class': 'form-control'}),
            'phone2': forms.TextInput(attrs={'class': 'form-control'}),
            'comments': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'name': 'Nome',
            'address': 'Endereço',
            'address_number': 'Número',
            'phone1': 'Telefone Principal',
            'phone2': 'Telefone Secundário',
            'comments': 'Observações',
        }
