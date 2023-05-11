from django.shortcuts import render
from django.http import request
from . import models

# Create your views here.


def index(request):
    dt = list()
    values = models.Dados.objects.all()
    for value in values:
        dt.append(value.value)

    ls = list()
    labels = models.Labels.objects.all()
    for label in labels:
        ls.append(label.value)

    return render(request, 'dashboard/index.html',  {'dtpy': dt, 'lspy': ls}) 

