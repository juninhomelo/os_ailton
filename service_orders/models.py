from django.db import models
from customers.models import Client
from services.models import Service
from products.models import Product


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Nome')

    class Meta:
        verbose_name = ('Marca')
        verbose_name_plural = ('Marcas')

    def __str__(self):
        return self.name


class ServiceOrder(models.Model):
    STATUS_CHOICES = (
        ('O', 'OPEN'),
        ('F', 'FINISHED'),
        ('C', 'CANCELED')
    )
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.PROTECT, verbose_name='Nome')
    phone1 = models.CharField(max_length=15, null=True, verbose_name='Telefone')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='brand', verbose_name='Marca')
    model = models.CharField(max_length=200, verbose_name='Modelo')
    model_year = models.CharField(max_length=4, verbose_name='Ano')
    plate = models.CharField(max_length=10, blank=True, null=True, verbose_name='Placa')
    services = models.ManyToManyField(Service, blank=True, verbose_name='Serviços')
    products = models.ManyToManyField(Product, blank=True, verbose_name='Produtos')
    created_at = models.DateField(auto_now_add=True, verbose_name='Criado em')
    finished_at = models.DateField(blank=True, null=True, verbose_name='Data Finalização')
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor Total')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='Status')
    comments = models.TextField(blank=True, null=True, verbose_name='Observações')

    class Meta:
        verbose_name = ('Ordem de Serviço')
        verbose_name_plural = ('Ordens de Serviços')
    
    def __str__(self):
        return f'Order # {self.pk} - {self.client} - {self.model}'
