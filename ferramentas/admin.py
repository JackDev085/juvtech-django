from django.contrib import admin
from .models import Formulario

@admin.register(Formulario)
class FormularioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cuca', 'data_atual', 'periodo']
