# Generated by Django 5.0.6 on 2024-06-18 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_orders', '0003_alter_serviceorder_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceorder',
            name='phone1',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
