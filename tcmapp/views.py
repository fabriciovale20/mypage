from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Cadastro

def home(request):
    data = {}
    data['cadastros'] = Cadastro.objects.all()
    return render(request, 'tcmapp/home.html', data)
