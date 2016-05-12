from django.contrib import admin
from .models import Client, Record

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_display =  ('code','name', 'gender', 'phone', 'birthday', 'client_status', 'adress', 'created')
    list_filter = ('gender', 'client_status', 'active')


class RecordAmdin(admin.ModelAdmin):
    list_display = ('client', 'visit', 'title', 'created')



admin.site.register(Client, ClientAdmin)
admin.site.register(Record, RecordAmdin)