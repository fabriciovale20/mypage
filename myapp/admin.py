from django.contrib import admin
from .models import Categoria, Marca, Modelo, Cadastro, Situacao, Imagem

admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Situacao)
admin.site.register(Imagem)


@admin.register(Cadastro)
class CadastroAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'marca', 'modelo', 'macsn_name', 'valor', 'imagem', 'situacao')
    search_fields = ('macsn_name',)
    list_filter = ('modelo',)
