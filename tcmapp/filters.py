import django_filters
from .models import Cadastro

class CadastroFilter(django_filters.FilterSet):
    cadastro = django_filters.CharFilter(lookup_expr='icontains')
    cadastro.modelo = django_filters.CharFilter(lookup_expr='icontains')
    cadastro.marca = django_filters.CharFilter(lookup_expr='icontains')
    macsn_name = django_filters.CharFilter(lookup_expr='icontains')
    valor = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Cadastro
        fields = ('categoria', 'modelo', 'marca', 'macsn_name', 'valor')
