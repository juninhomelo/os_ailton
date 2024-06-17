from django import forms
from services.models import Service


class ServiceModelForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'estimated_time': forms.TextInput(attrs={'class': 'form-control'}),
            'comments': forms.Textarea( attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'name': 'Nome',
            'price': 'Valor',
            'estimated_time': 'Tempo estimado',
            'comments': 'Observações',
        }