from django.contrib import admin
from .models import Categoria, Marca, Modelo, Cadastro

admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Cadastro)
