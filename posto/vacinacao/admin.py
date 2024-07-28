from django.contrib import admin
from .models import Crianca

class CriancaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_crianca', 'idade_crianca', 'nome_mae', 'vacina', 'bairro')

# Register your models here.
admin.site.register(Crianca, CriancaAdmin)
