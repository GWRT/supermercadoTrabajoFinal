# Generated by Django 3.1 on 2020-08-12 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='units',
            field=models.IntegerField(default=0),
        ),
    ]
