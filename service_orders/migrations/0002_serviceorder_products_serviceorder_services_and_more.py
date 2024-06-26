# Generated by Django 5.0.6 on 2024-06-17 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('service_orders', '0001_initial'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceorder',
            name='products',
            field=models.ManyToManyField(blank=True, to='products.product'),
        ),
        migrations.AddField(
            model_name='serviceorder',
            name='services',
            field=models.ManyToManyField(blank=True, to='services.service'),
        ),
        migrations.AlterField(
            model_name='serviceorder',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='serviceorder',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
