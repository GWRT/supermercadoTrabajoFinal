# Generated by Django 2.1.5 on 2020-07-15 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200715_0235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='disc',
            field=models.IntegerField(),
        ),
    ]
