from django.db import models


class Service(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500, verbose_name='Nome')
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Preço')
    estimated_time = models.IntegerField(default=0, blank=True, null=True, verbose_name='Tempo Estimado (horas)')
    comments = models.TextField(blank=True, null=True, verbose_name='Descrição')

    class Meta:
        verbose_name = ('Serviço')
        verbose_name_plural = ('Serviços')

    def __str__(self):
        return self.name
