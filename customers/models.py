from django.db import models


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500, verbose_name='Nome')
    address = models.CharField(max_length=500, blank=True, null=True, verbose_name='Endereço')
    address_number = models.CharField(max_length=20, blank=True, null=True, verbose_name='Número')
    phone1 = models.CharField(max_length=15, verbose_name='Telefone 1')
    phone2 = models.CharField(max_length=15, blank=True, null=True, verbose_name='Telefone 2')
    comments = models.TextField(blank=True, null=True, verbose_name='Observações')

    class Meta:
        verbose_name = ('Cliente')
        verbose_name_plural = ('Clientes')

    def __str__(self):
        return self.name
