from django.shortcuts import render
from .models import Cadastro
from .filters import CadastroFilter

from django.core.paginator import Paginator

def home(request):
    data = Cadastro.objects.all()

    categoria = request.GET.get('categoria')

    if categoria:
        data = data.filter(categoria=categoria)
        print(categoria)

    context = {'data': data}

    return render(request, 'tcmapp/home.html', context)

def filtro(request):
    context = {}
    filter = CadastroFilter(request.GET, queryset=Cadastro.objects.all())
    context['filter'] = filter
    return render(request, 'tcmapp/filtro.html', context=context)

