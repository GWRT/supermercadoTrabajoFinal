# Generated by Django 3.1 on 2020-08-12 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0004_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='adm',
            name='photo',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='client',
            name='photo',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
