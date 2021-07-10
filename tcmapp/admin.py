from django.contrib import admin
from .models import Categoria, Marca, Modelo, Cadastro

admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Modelo)

@admin.register(Cadastro)
class CadastroAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'marca', 'modelo', 'macsn_name', 'valor', 'register_date')
    search_fields = ('macsn_name',)
    list_filter = ('categoria',)

    # def get_register_date(self, obj):
    #     if obj.register_date:
    #         return obj.register_date.strftime('%d/%m/%Y')
    #
    # get_register_date.short_description = 'Data de publicação'
