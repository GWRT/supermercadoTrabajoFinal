# Generated by Django 3.1 on 2020-08-12 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0007_remove_client_ebooks'),
        ('pedidos', '0002_auto_20200812_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cuentas.client'),
        ),
    ]
