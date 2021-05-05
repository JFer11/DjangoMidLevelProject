from django.contrib import admin
from .models import Service


class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'created')


admin.site.register(Service, ServiceAdmin)
