from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Pais)
#admin.site.register(models.Cliente)

@admin.register(models.Cliente)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "fec_nac", "pais_origen")
    search_fields = ("nombre", "apellido")
    list_filter = ("pais_origen",)
    ordering = ("apellido", "nombre")
    date_hierarchy = ("fec_nac")