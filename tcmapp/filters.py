import django_filters
from .models import Cadastro

class ArticleFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    subtittle = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Cadastro
        fields = ('tittle', 'subtittle')
