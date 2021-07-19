from django.shortcuts import render
from .models import Cadastro
from .filters import CadastroFilter


def filtro(request):
    context = {}
    filter = CadastroFilter(request.GET,
                            queryset=Cadastro.objects.select_related('categoria', 'modelo', 'marca'))
    context['filter'] = filter
    return render(request, 'tcmapp/filtro.html', context=context)
