# Generated by Django 3.1 on 2020-08-09 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persona', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
                ('estado', models.IntegerField(choices=[(1, 'Activo'), (2, 'Inactivo')], default=1)),
            ],
        ),
    ]
