# Generated by Django 2.1.5 on 2020-07-14 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('units', models.IntegerField()),
                ('price', models.IntegerField()),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
