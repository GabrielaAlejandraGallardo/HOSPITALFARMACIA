from django.contrib import admin

# Register your models here.
from .models import Deposito,Hueco,Supervisor

admin.site.register(Deposito)
admin.site.register(Hueco)
admin.site.register(Supervisor)