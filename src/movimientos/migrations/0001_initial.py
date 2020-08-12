# Generated by Django 3.1 on 2020-08-12 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0002_order_orderitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry', models.IntegerField(choices=[(1, 'Entrada'), (2, 'Salida')], default=1)),
                ('quant', models.IntegerField()),
                ('prod', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='productos.producto')),
            ],
        ),
    ]
