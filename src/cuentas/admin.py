from django.contrib import admin
from .models import User, Client, Adm

# Register your models here.

admin.site.register(User)
admin.site.register(Client)
admin.site.register(Adm)
