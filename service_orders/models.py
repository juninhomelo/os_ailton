from django.db import models
from customers.models import Client
from services.models import Service
from products.models import Product


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ServiceOrder(models.Model):
    STATUS_CHOICES = (
        ('O', 'OPEN'),
        ('F', 'FINISHED'),
        ('C', 'CANCELED')
    )
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    phone1 = models.CharField(max_length=15, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='brand')
    model = models.CharField(max_length=200)
    model_year = models.CharField(max_length=4)
    plate = models.CharField(max_length=10, blank=True, null=True)
    services = models.ManyToManyField(Service, blank=True)
    products = models.ManyToManyField(Product, blank=True)
    created_at = models.DateField(auto_now_add=True)
    finished_at = models.DateField(blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Order # {self.pk} - {self.client} - {self.model}'
