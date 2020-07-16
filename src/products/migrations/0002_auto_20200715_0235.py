# Generated by Django 3.0.8 on 2020-07-15 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cat',
            field=models.IntegerField(choices=[(1, 'Category 1'), (2, 'Category 2'), (3, 'Category 3')], default=1),
        ),
        migrations.AddField(
            model_name='product',
            name='disc',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='product',
            name='prov',
            field=models.IntegerField(choices=[(1, 'Prov 1'), (2, 'Prov 2'), (3, 'Prov 3')], default=1),
        ),
        migrations.AddField(
            model_name='product',
            name='stat',
            field=models.IntegerField(choices=[(1, 'Disponible'), (2, 'Not disponible')], default=1),
        ),
    ]
