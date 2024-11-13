from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500, verbose_name='Nome')
    description = models.TextField(blank=True, null=True, verbose_name='Descrição')
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Preço')
    quantity = models.IntegerField(default=0, verbose_name='Quantidade')
    comments = models.TextField(blank=True, null=True, verbose_name='Observações')

    class Meta:
        verbose_name = ('Produto')
        verbose_name_plural = ('Produtos')

    def __str__(self):
        return self.name
